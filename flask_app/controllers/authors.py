from flask_app import app
from flask_app.models import author, book
from flask import redirect, render_template, request

@app.route('/authors')
def authors():
    authors = author.Author.get_all_authors()
    return render_template('authors.html', authors=authors)

@app.route('/author/create', methods=['POST'])
def create_author():
    data = {
        "name" : request.form["name"]
    }
    author.Author.save(data)
    return redirect('/authors')

@app.route('/author/view/<int:id>')
def view_author(id):
    data = {
        'id' : id
    }
    one_author = author.Author.get_one_author(data)
    favorites = author.Author.get_favorites(data)
    non_favorites = author.Author.get_non_favorites(data)
    return render_template('one_author.html', one_author = one_author[0], favorites = favorites, non_favorites = non_favorites)

@app.route('/author/favorite', methods=['POST'])
def favorite():
    data = {
        "author_id" : request.form["author_id"],
        "book_id" : request.form["favorite_book"]
    }
    print(data["author_id"])
    author.Author.save_favorite(data)
    return redirect('/author/view/' + data["author_id"])

