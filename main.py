from flask import Flask, url_for
import db, views



app = Flask(__name__)

app.add_url_rule('/', view_func=views.main_page)
app.add_url_rule('/film-page', view_func=views.film_page)
app.add_url_rule('/add-film', view_func=views.add_film, methods=['GET', 'POST'])
app.add_url_rule('/films-library', view_func=views.get_films)

app.register_error_handler(404, views.page_not_found)
    
# db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
