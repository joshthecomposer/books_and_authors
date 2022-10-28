from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors (name) VALUES (%(name)s)"
        return connectToMySQL("books_schema").query_db(query, data)
    
    @classmethod 
    def get_all_authors(cls):
        query = "SELECT * FROM authors;"
        return connectToMySQL("books_schema").query_db(query)
    
    @classmethod
    def get_one_author(cls, data):
        query = "SELECT * FROM authors WHERE id = %(id)s;"
        return connectToMySQL("books_schema").query_db(query, data)
    
    @classmethod 
    def save_favorite(cls, data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL("books_schema").query_db(query, data)
    
    @classmethod
    def get_favorites(cls, data):
        query = """SELECT books.title, books.num_of_pages FROM authors 
                    JOIN favorites ON authors.id = favorites.author_id
                    JOIN books ON favorites.book_id = books.id 
                    WHERE authors.id = %(id)s;"""
        results = connectToMySQL("books_schema").query_db(query, data)
        return results
    @classmethod 
    def get_non_favorites(cls, data):
        query = """
        SELECT * FROM books WHERE books.id NOT IN (SELECT book_id FROM favorites WHERE author_id = %(id)s);
        """
        results = connectToMySQL("books_schema").query_db(query, data)
        print("THIS IS THE NON FAVORITES", results)
        return results
        