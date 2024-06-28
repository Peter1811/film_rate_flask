from flask import Flask, render_template, url_for

app = Flask(__name__)

main_menu = {'Main page': 'main_page', 'Add film': 'add_film', 'Get the list of film': 'get_films'}


@app.route('/')
def main_page():
    return render_template('main_page.html', main_menu=main_menu)

@app.route('/film/<int:film_id>')
def film_page(film_id):
    return render_template('film_page.html', main_menu=main_menu, film_id=film_id)

@app.route('/add-film')
def add_film():
    return render_template('add_film.html', main_menu=main_menu)

@app.route('/films-library')
def get_films():
    return render_template('films_list.html', main_menu=main_menu)

@app.route('/about')
def about():
    return render_template('about.html', main_menu=main_menu)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', main_menu=main_menu)


if __name__ == '__main__':
    app.run(debug=True)