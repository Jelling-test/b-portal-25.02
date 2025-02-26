from flask_babel import Babel
from flask import request, session

babel = Babel()

LANGUAGES = {
    'da': {'name': 'Dansk', 'flag': 'dk.png'},
    'en': {'name': 'English', 'flag': 'gb.png'},
    'nl': {'name': 'Nederlands', 'flag': 'nl.png'},
    'de': {'name': 'Deutsch', 'flag': 'de.png'},
    'no': {'name': 'Norsk', 'flag': 'no.png'},
    'sv': {'name': 'Svenska', 'flag': 'se.png'},
    'es': {'name': 'Español', 'flag': 'es.png'},
    'fr': {'name': 'Français', 'flag': 'fr.png'},
    'it': {'name': 'Italiano', 'flag': 'it.png'},
    'fi': {'name': 'Suomi', 'flag': 'fi.png'}
}

@babel.localeselector
def get_locale():
    if 'language' in session:
        return session['language']
    return request.accept_languages.best_match(LANGUAGES.keys(), default='da')
