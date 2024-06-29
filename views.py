from flask import render_template


main_menu = {'Main page': 'main_page', 'Add film': 'add_film', 'Get the list of film': 'get_films'}

def main_page():
    return render_template('main_page.html', main_menu=main_menu, title='Main page')


def film_page(film_id):
    return render_template('film_page.html', main_menu=main_menu, title='Film page', film_id=film_id)


def add_film():
    res = render_template('add_film.html', main_menu=main_menu, title='Add film')
    return res


def get_films():
    return render_template('films_list.html', main_menu=main_menu, title='List of added films')


def page_not_found(error):
    return render_template('404.html', main_menu=main_menu)