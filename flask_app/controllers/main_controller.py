from flask import render_template, redirect
from flask_app import app

@app.route('/')
def index():
    return redirect('/authors')