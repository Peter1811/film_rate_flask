from flask import render_template, request

import db

main_menu = {'Main page': 'get_main_page', 'Add film': 'add_film', 'Get the list of film': 'get_films'}
genres = ['Comedy', 'Drama', 'Thriller', 'Horror']


def get_main_page():
    return render_template('main_page.html', main_menu=main_menu, title='Main page')


def get_film_page(film_id):
    return render_template('film_page.html', main_menu=main_menu, title='Film page', film_id=film_id)


def add_film():
    if request.method == 'POST':
        
        name = request.form['film_name']
        director = request.form['film_director']
        short_description = request.form['description']
        genre = request.form['genre']

        connection, cursor = db.create_connection()

        cursor.execute(
            '''INSERT INTO film (film_name, director, short_description, genre) VALUES (%s, %s, %s, %s)''',
            (name, director, short_description, genre)
        )

        db.close_connection(connection, cursor)

    return render_template('add_film.html', main_menu=main_menu, genres=genres, title='Add film')


def get_films():
    connection, cursor = db.create_connection()

    cursor.execute(
        '''SELECT * FROM film'''
    )
    films = cursor.fetchall()
    
    if len(films) == 0:
        films = None

    db.close_connection(connection, cursor)

    return render_template('films_list.html', main_menu=main_menu, title='List of added films', films=films)


def get_page_not_found_page(error):
    return render_template('404.html', main_menu=main_menu)
