from flask import abort, render_template, request, url_for
from typing import Any

import db

main_menu = {'Main page': 'get_main_page', 'Add film': 'add_film', 'Get the list of film': 'get_films'}
genres = ['Comedy', 'Drama', 'Thriller', 'Horror']


def get_main_page() -> str:
    return render_template('main_page.html', main_menu=main_menu, title='Main page')


def get_film_page(film_id: int) -> str:
    return render_template('film_page.html', main_menu=main_menu, title='Film page', film_id=film_id)


def add_film() -> str:

    if request.method == 'POST':
        name = request.form['film_name']
        director = request.form['film_director']
        short_description = request.form['description']
        genre = request.form['genre']

        connection, cursor = db.create_connection()
        if connection is None or cursor is None:
            abort(500)

        cursor.execute(
            '''INSERT INTO film (film_name, director, short_description, genre) VALUES (%s, %s, %s, %s)''',
            (name, director, short_description, genre)
        )
        connection.commit()

        db.close_connection(connection, cursor)

    return render_template('add_film.html', main_menu=main_menu, genres=genres, title='Add film')


def get_films() -> str:
    connection, cursor = db.create_connection()
    print(connection, cursor)

    if connection is None or cursor is None:
        abort(500)

    cursor.execute(
        '''SELECT * FROM film'''
    )
    films = cursor.fetchall()
    
    if len(films) == 0:
        films = None

    connection.commit()

    db.close_connection(connection, cursor)

    return render_template('films_list.html', main_menu=main_menu, title='List of added films', films=films)


def get_page_not_found_page(error: Any) -> str:
    return render_template('error_pages/page_404.html', main_menu=main_menu)

def get_internal_server_error_page(error: Any) -> str:
    return render_template('error_pages/page_500.html', main_menu=main_menu)
