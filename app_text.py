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
db = SQL("sqlite:///cityguide.db")

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
    'imgUrl': 'https://i.ibb.co/7X0TsGT/puppen.jpg',
    'phone': '040 3346507-80',
    'img1': 'https://i.ibb.co/W6Y8Gqh/theater1.jpg',
    'img2': 'https://i.ibb.co/VTskrp2/theater2.jpg',
    'img3': 'https://i.ibb.co/XYMgNQ3/theater3.jpg',
    'img4': 'https://i.ibb.co/61DKkzy/theater4.jpg',
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
    'imgUrl': 'https://i.ibb.co/H2nBYJV/zoo.jpg',
    'phone': '040 428382276',
    'img1': 'https://i.ibb.co/Q68ZDYt/zoo1.jpg',
    'img2': 'https://i.ibb.co/pbd7X5M/zoo2.jpg',
    'img3': 'https://i.ibb.co/Vtc00MP/zoo3.jpg',
    'img4': 'https://i.ibb.co/Vw7HWhZ/zoo4.jpg',
    'text':
    'The Zoological Museum presents specimens of different animals over some 2,000 sq m of floor space. The Museum is popular both as a learning space for school groups and a venue for art classes.',
    'lat': 53.567315,
    'lng': 9.978716,
    'address': 'Martin-Luther-King Platz 3 20146 Hamburg',
}, {
    'id': 4,
    'name': 'Indoor Playground Rabatzz',
    'url': 'https://www.rabatzz.de/',
    'imgUrl': 'https://i.ibb.co/fXV7JH9/rabatzz4.jpg',
    'phone': '040 54709690',
    'img1': 'https://i.ibb.co/wKYcQtg/rabatzz.jpg',
    'img2': 'https://i.ibb.co/Pj9s3jj/rabatzz2.jpg',
    'img3': 'https://i.ibb.co/hK8j4Dh/rabatzz3.jpg',
    'img4': 'https://i.ibb.co/fXV7JH9/rabatzz4.jpg',
    'text':
    '365 days a year the Rabatzz promises variety and adventure. Children can let off steam to their heart\'s content on two levels. And even the big ones get their money\'s worth.',
    'lat': 53.599832,
    'lng': 9.915805,
    'address': 'Kieler Straße 575a 22525 Hamburg',
}, {
    'id': 5,
    'name': 'Emigration Museum',
    'url': 'https://www.ballinstadt.de/en/',
    'imgUrl': 'https://i.ibb.co/V9MHHrr/ballin.jpg',
    'phone': '040 3197916-0',
    'img1': 'https://i.ibb.co/LhjTXXW/ballin.jpg',
    'img2': 'https://i.ibb.co/7XhrC15/ballin1.jpg',
    'img3': 'https://i.ibb.co/ZX0N8Nb/ballin3.jpg',
    'img4': 'https://i.ibb.co/m52PDH0/ballin4.jpg',
    'text':
    'The Emigrant Museum is great for understanding things in the world. Also a MUST for the younger generation, to experience the history of fellow human beings. Uniquely designed rooms, fascinating documentaries, some with short films. What hurdles people had to endure in some cases before they were allowed to enter the country of their choice.',
    'lat': 53.520396,
    'lng': 10.016970,
    'address': 'Veddeler Bogen 2, 20539 Hamburg',
}, {
    'id': 6,
    'name': 'The Chocolate Museum',
    'url': 'https://www.chocoversum.de/',
    'imgUrl': 'https://i.ibb.co/HCTdf7Q/choco.jpg',
    'phone': '040 41912300',
    'img1': 'https://i.ibb.co/87VMKSQ/choco1.jpg',
    'img2': 'https://i.ibb.co/sbHNfp7/choco2.jpg',
    'img3': 'https://i.ibb.co/NFwkxg8/choco3.jpg',
    'img4': 'https://i.ibb.co/jMwQKjb/choco4.jpg',
    'text':
    'This irresistible experience in Hamburg’s Chocolate Museum really packs a punch!  Our ChoColleagues will take you on 90 sweet minutes through the museum while encouraging you to learn everything about chocolate making and have a nibble, snack or taste along the way.',
    'lat': 53.547935,
    'lng': 10.002276,
    'address': 'Veddeler Bogen 2, 20539 Hamburg',
}, {
    'id': 7,
    'name': 'Miniature Wonderland',
    'url': 'https://www.miniatur-wunderland.com/',
    'imgUrl': 'https://i.ibb.co/3W4fDBw/miniatur.jpg',
    'phone': '040 3006800',
    'img1': 'https://i.ibb.co/rbrwdxn/miniatur1.jpg',
    'img2': 'https://i.ibb.co/12tYDy4/miniatur2.jpg',
    'img3': 'https://i.ibb.co/kHW2QLk/miniatur3.jpg',
    'img4': 'https://i.ibb.co/Snd3qYS/miniatur4.jpg',
    'text':
    'The world\'s largest model railroad system has become one of the tourist highlights of Hamburg.​​​​​​​ Visitors can admire different countries and even an airport in miniature size. Hamburg’s miniature replica comprises no less than 200 square metres. ',
    'lat': 53.543729,
    'lng': 9.988516,
    'address': 'Kehrwieder 2/Block D, 20457 Hamburg',
}, {
    'id': 8,
    'name': 'The Puppenmuseum Falkenstein',
    'url': 'https://www.elke-droescher.de/',
    'imgUrl': 'https://i.ibb.co/HC8h2J7/dolls2.jpg',
    'phone': '040 810582',
    'img1': 'https://i.ibb.co/Gd3P9vt/dolls.jpg',
    'img2': 'https://i.ibb.co/WPNkv4J/dolls1.jpg',
    'img3': 'https://i.ibb.co/k1rvVv9/dolls3.jpg',
    'img4': 'https://i.ibb.co/vBkf58q/dolls4.jpg',
    'text':
    'High above the Elbe river stands Hamburg\'s most impressive country house in Bauhaus style, a doll museum with over 500 dolls, 60 doll\'s houses and children\'s portraits. The antique dolls reflect the development of fashion and the change in the ideal of beauty.',
    'lat': 53.56599,
    'lng': 9.763900000000035,
    'address': 'Grotiusweg 79, 22587 Hamburg',
}]


@app.route('/')
def index():
    places = db.execute("SELECT name FROM places")
    print(places)
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
