from flask_app import app
from flask_app.controllers import authors, books, main_controller




if __name__ == '__main__':
    app.run(debug=True)