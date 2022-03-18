from cgi import print_environ
from unicodedata import name
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)
app.secret_key = b'\xd2%\\\xb6\x89g\xee\r\xce\x1f\x8b\x10u\xd1|\xa0'

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///cityguide.db")


@app.route('/')
def index():
    places = db.execute("SELECT * FROM places WHERE active = 'yes'")
    return render_template('index.html', places=places)


@app.route('/places/<id>')
def places(id):
    places = db.execute("SELECT * FROM places")
    for place in places:
        print(place["active"])
        if int(place['id']) == int(id):
            name = place["name"]
            address = place["address"]
            text = place["text"]
            img1 = place["img1"]
            img2 = place["img2"]
            img3 = place["img3"]
            img4 = place["img4"]
            url = place["url"]
            phone = place["phone"]

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


@app.route('/contact.html', methods=["GET", "POST"])
def contact():
    message = ''
    if request.method == "POST":
        name = request.form.get("name")
        lastName = request.form.get("lastName")
        email = request.form.get("email")
        text = request.form.get("message")
        print(name)
        print(text)
        if not name:
            message = "You must provide your name"
            return render_template('contact.html', message=message)
        elif not lastName:
            message = "You must provide your last name"
            return render_template('contact.html', message=message)
        elif not email:
            message = "You must provide your email"
            return render_template('contact.html', message=message)

        db.execute(
            "INSERT INTO contact (first_name, last_name, email, message) VALUES (?, ?, ?, ?)",
            name, lastName, email, text)

        flash("Your message was sent!")
        return redirect("contact.html")
    else:
        return render_template('contact.html')


@app.route('/add.html', methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form.get("name")
        address = request.form.get("address")
        phone = request.form.get("phone")
        web = request.form.get("web")
        text = request.form.get("text")
        photo1 = request.form.get("photo1")
        photo2 = request.form.get("photo2")
        photo3 = request.form.get("photo3")
        photo4 = request.form.get("photo4")
        print(photo1)

        db.execute(
            "INSERT INTO places (name, phone, address, url, img1, img2, img3, img4, text, active) VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ? )",
            name, phone, address, web, photo1, photo2, photo3, photo4, text,
            "no")

        flash("Your submission was successful!")
        return redirect("/")

    else:
        return render_template('add.html')


# if __name__ == ‘__main__’:
#     app.run(host=”localhost”, port=8080, debug=True)

if __name__ == '__main__':
    app.run()
