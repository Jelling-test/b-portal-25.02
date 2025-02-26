from flask import Flask, render_template, session, redirect, url_for, request
from flask_babel import Babel

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['BABEL_DEFAULT_LOCALE'] = 'da'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

babel = Babel(app)

LANGUAGES = {
    'da': {'name': 'Dansk', 'flag': 'dk.png'},
    'en': {'name': 'English', 'flag': 'gb.png'}
}

def get_locale():
    if 'language' in session:
        return session['language']
    return request.accept_languages.best_match(list(LANGUAGES.keys()), default='da')

babel.init_app(app, locale_selector=get_locale)

@app.route('/change-language/<language>')
def change_language(language):
    if language in LANGUAGES:
        session['language'] = language
    return redirect(request.referrer or url_for('index'))

@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)

if __name__ == '__main__':
    app.run(debug=True)
