import dotenv
import os
import psycopg2

from flask import render_template, request


dotenv.load_dotenv('.env')


main_menu = {'Main page': 'main_page', 'Add film': 'add_film', 'Get the list of film': 'get_films'}

def main_page():
    return render_template('main_page.html', main_menu=main_menu, title='Main page')


def film_page(film_id):
    return render_template('film_page.html', main_menu=main_menu, title='Film page', film_id=film_id)


def add_film():
    res = render_template('add_film.html', main_menu=main_menu, title='Add film')

    if request.method == 'POST':
        print(request.form['film_name'])
        connection = psycopg2.connect(
            database=os.getenv('DATABASE'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            host=os.getenv('HOST'),
            port=os.getenv('PORT')
        )

        cur = connection.cursor()
        name = request.form['film_name']
        director = request.form['film_director']
        short_description = request.form['description']

        cur.execute(
            '''INSERT INTO film (film_name, director, short_description) VALUES (%s, %s, %s)''',
            (name, director, short_description)
        )

        connection.commit()

        cur.close()
        connection.close()
    
    return res


def get_films():
    return render_template('films_list.html', main_menu=main_menu, title='List of added films')


def page_not_found(error):
    return render_template('404.html', main_menu=main_menu)