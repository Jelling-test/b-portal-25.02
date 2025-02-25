from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from models.user import User

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'auth.login'

# Registrer blueprints her senere
# from app.auth import bp as auth_bp
# app.register_blueprint(auth_bp)

# User loader for Flask-Login
@login.user_loader
def load_user(user_id):
    # Her vil vi senere hente brugeren fra databasen
    # For nu returnerer vi bare None, hvilket betyder at ingen er logget ind
    return None

@app.route('/')
def index():
    return render_template('index.html', title='Velkommen')

if __name__ == '__main__':
    app.run(debug=True)
