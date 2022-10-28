from flask_app import app
from flask_app.models import book, author
from flask import redirect, render_template, request

@app.route('/books')
def books():
    books = book.Book.get_all_books()
    return render_template('books.html', books = books)

@app.route('/book/create', methods=['POST'])
def create_book():
    data = {
        'title': request.form["title"],
        'num_of_pages': request.form["num_of_pages"]
    }
    book.Book.save(data)
    return redirect('/books')

@app.route('/book/view/<int:id>')
def view_book(id):
    data = {
        'id' : id,
    }
    one_book = book.Book.get_one_book(data)
    favorites = book.Book.get_favorites(data)
    non_favorites = book.Book.get_non_favorites(data)
    
    return render_template('one_book.html', one_book = one_book[0], favorites = favorites, non_favorites = non_favorites)

@app.route('/book/favorite', methods=['POST'])
def _favorite():
    data = {
        'book_id' : request.form["book_id"],
        'author_id' : request.form["favorite_author"]
    }
    book.Book.save_favorite(data)
    return redirect('/book/view/' + data['book_id'])
