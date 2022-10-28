from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"
        return connectToMySQL('books_schema').query_db(query, data)
    
    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        return connectToMySQL('books_schema').query_db(query)
    
    @classmethod
    def get_one_book(cls, data):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        return connectToMySQL('books_schema').query_db(query, data)
    
    @classmethod
    def save_favorite(cls, data):
        query = "INSERT INTO favorites (book_id, author_id) VALUES (%(book_id)s, %(author_id)s)"
        return connectToMySQL('books_schema').query_db(query, data)
    
    @classmethod
    def get_favorites(cls, data):
        query = """SELECT authors.name FROM books
                    JOIN favorites ON books.id = favorites.book_id
                    JOIN authors ON favorites.author_id = authors.id
                    WHERE books.id = %(id)s"""
        results = connectToMySQL('books_schema').query_db(query, data)
        return results

    @classmethod 
    def get_non_favorites(cls, data):
        query = """
        SELECT * FROM authors WHERE authors.id NOT IN (SELECT author_id FROM favorites WHERE book_id = %(id)s);
        """
        results = connectToMySQL("books_schema").query_db(query, data)
        print("THIS IS THE NON FAVORITES", results)
        return results