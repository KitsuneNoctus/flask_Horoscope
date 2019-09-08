from flask import Flask, request
from flask import render_template
from random import choice, sample

app = Flask(__name__)

horoscopes = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely', 'tenacious', 'Pythonic']

@app.route('/')
def index():
    """Show the homepage and ask the user's name."""
    return render_template('index_HC.html')

@app.route('/compliment')
def get_horoscope():
    """Give the user their horoscope"""
    name = request.args.get('name')
    num_compliments = int(request.args.get('num_horoscopes'))
    show_compliments = request.args.get('show_horoscopes')
    nice_things = ', '.join(sample(compliments, num_compliments))

    return render_template(
        'horoscopes.html',
        name=name,
        show_horoscopes=show_horoscopes,
        horoscopes=horoscopes_to_show)

if __name__ == '__main__':
    app.run(debug=True)
