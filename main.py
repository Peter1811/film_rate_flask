import os
import sqlite3

from flask import Flask, url_for
import views

app = Flask(__name__)

app.add_url_rule('/', view_func=views.main_page)
app.add_url_rule('/film-page', view_func=views.film_page)
app.add_url_rule('/add-film', view_func=views.add_film, methods=['GET', 'POST'])
app.add_url_rule('/films-library', view_func=views.get_films)

app.register_error_handler(404, views.page_not_found)

app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'films.db')))

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn_row_factory = sqlite3.Row
    return conn

def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())

    db.commit()
    db.close()
    

if __name__ == '__main__':
    app.run(debug=True)
