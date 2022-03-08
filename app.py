from cgi import print_environ
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
# db = SQL("sqlite:///cityguide.db")

PLACES = [{
    'id': 1,
    'name': 'Museum of Illisuons',
    'url': 'https://hamburg.museumderillusionen.de/en/',
    'imgUrl': 'https://i.ibb.co/grRBM2d/icon-illus.png',
    'phone': '040 30707105',
    'img1': 'https://i.ibb.co/dbR6txJ/illus1.jpg',
    'img2': 'https://i.ibb.co/zHqygg3/IMG-4617.jpg',
    'img3': 'https://i.ibb.co/kx80Jv3/illus3.jpg',
    'img4': 'https://i.ibb.co/pR8WnS6/illus4.jpg',
    'text':
    'Enter the fascinating world of illusions! We will trick your senses and amaze you while doing it. Visit us and you learn that nothing is what it seems, especially not in the Museum of Illusions!',
    'lat': 53.55292,
    'lng': 10.0021,
    'address': 'Lilienstraße 14-16, 20095 Hamburg',
}, {
    'id': 2,
    'name': 'Hamburger Puppentheater',
    'url': 'https://hamburgerpuppentheater.de',
    'text':
    'The Hamburg Puppet Theatre is located under the roof of Haus Flachsland and offers a varied theatre programme for young and old.',
    'lat': 53.583240,
    'lng': 10.043950,
    'address': 'Bramfelder Straße 9, 22305 Hamburg',
}, {
    'id': 3,
    'name': 'Zoological Museum',
    'url':
    'https://hamburg.leibniz-lib.de/en/ausstellungen/museum-zoologie.html',
    'text': '',
    'lat': 53.567315,
    'lng': 9.978716,
    'address': '',
}, {
    'id': 4,
    'name': 'Indoor Playground Rabatzz',
    'url': 'https://www.rabatzz.de/',
    'text': '',
    'lat': 53.599832,
    'lng': 9.915805,
}, {
    'id': 5,
    'name': 'Emigration Museum',
    'url': 'https://www.ballinstadt.de/en/',
    'text': '',
    'lat': 53.520396,
    'lng': 10.016970,
    'address': '',
}, {
    'id': 6,
    'name': 'The Chocolate Museum ',
    'url': 'https://www.chocoversum.de/',
    'text': '',
    'lat': 53.547935,
    'lng': 10.002276,
    'address': '',
}, {
    'id': 7,
    'name': 'Miniature Wonderland',
    'url': 'https://www.miniatur-wunderland.com/',
    'text': '',
    'lat': 53.543729,
    'lng': 9.988516,
    'address': '',
}, {
    'id': 8,
    'name': 'The Puppenmuseum Falkenstein',
    'url': 'https://www.elke-droescher.de/',
    'text': '',
    'lat': 53.56599,
    'lng': 9.763900000000035,
    'address': '',
}]


@app.route('/')
def index():
    return render_template('index.html', places=PLACES)


@app.route('/places/<id>')
def places(id):
    for place in PLACES:
        if place['id'] == int(id):
            print(place['name'])
            name = place["name"]
            address = place["address"]
            text = place["text"]
            img1 = place["img1"]
            img2 = place["img2"]
            img3 = place["img3"]
            img4 = place["img4"]
            url = place["url"]
            phone = place["phone"]
            print(img1)

    # return f'Welcome to place'
    return render_template('place.html',
                           name=name,
                           address=address,
                           text=text,
                           img1=img1,
                           img2=img2,
                           img3=img3,
                           img4=img4,
                           url=url,
                           phone=phone)


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


# if __name__ == ‘__main__’:
#     app.run(host=”localhost”, port=8080, debug=True)

if __name__ == '__main__':
    app.run()
