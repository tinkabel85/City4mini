from cgi import print_environ
from unicodedata import name
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.utils import secure_filename
from flask import send_from_directory
import os, re

# Ensure email validation
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Configure application
app = Flask(__name__)
app.secret_key = b'\xd2%\\\xb6\x89g\xee\r\xce\x1f\x8b\x10u\xd1|\xa0'
app.config['ALLOWED_EXTENSIONS'] = set(['jpg', 'png', 'jpeg'])
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024


def allowed_file(filename):
    return '.' in filename and filename.rsplit(
        '.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///cityguide.db")


@app.route('/')
def index():
    places = db.execute("SELECT * FROM places WHERE active = 'yes'")
    markers = db.execute("SELECT id, name, url, imgUrl, lat, lng FROM places")
    print(markers)
    return render_template('index.html', places=places, data=markers)


@app.route('/places/<id>')
def places(id):
    places = db.execute("SELECT * FROM places")
    for place in places:
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
        if not name:
            message = "You must provide your name"
            return render_template('contact.html', message=message)
        elif not lastName:
            message = "You must provide your last name"
            return render_template('contact.html', message=message)
        elif not email:
            message = "You must provide your email"
            return render_template('contact.html', message=message)
        elif not (re.fullmatch(regex, email)):
            print("Invalid Email")
            message = "You must provide valid email"

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
    message = ''
    if request.method == "POST":
        name = request.form.get("name")
        address = request.form.get("address")
        phone = request.form.get("phone")
        web = request.form.get("web")
        text = request.form.get("text")

        uploaded_files = request.files.getlist("file[]")
        print(uploaded_files)
        counter = 0
        print(len(uploaded_files))
        photos = []
        if len(uploaded_files) < 4:
            message = "Please upload at least four (4) photos"
            return render_template('add.html', message=message)
        for file in uploaded_files:
            filename = secure_filename(file.filename)
            extension = str(filename.split(".")[1])
            print(extension)
            img_name = name.replace(" ", "_").lower()
            counter += 1
            number = str(counter)
            if extension not in app.config['ALLOWED_EXTENSIONS']:
                message = "You can only upload .jpeg, .jpg, .png files"
                return render_template('img.html', message=message)
            # Move the file form the temporal folder to the upload folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            source = UPLOAD_FOLDER + '/' + filename
            destination = UPLOAD_FOLDER + '/' + img_name + number + '.' + extension

            photos.append(destination)
            os.rename(source, destination)
        print(photos)

        # Insert to database the place info
        db.execute(
            "INSERT INTO places (name, url, imgUrl, phone, address, img1, img2, img3, img4, text, active) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )",
            name, web, ('/' + photos[0]), phone, address, ('/' + photos[0]),
            ('/' + photos[1]), ('/' + photos[2]), ('/' + photos[3]), text,
            "yes")

        flash("Your submission was successful!")
        return redirect(url_for('add'))
    else:
        return render_template('add.html')


@app.route('/img.html', methods=["GET", "POST"])
def upload_file():
    message = ''
    if request.method == "POST":
        name = request.form.get("name")
        name = name.replace(" ", "_").lower()
        print(name)
        uploaded_files = request.files.getlist("file[]")
        print(uploaded_files)
        filenames = []
        counter = 0
        print(len(uploaded_files))
        if len(uploaded_files) < 4:
            message = "Please upload at least four (4) photos"
            return render_template('img.html', message=message)
        for file in uploaded_files:
            filename = secure_filename(file.filename)
            extension = filename.split(".")
            extension = str(extension[1])
            print(extension)
            counter += 1
            number = str(counter)
            print(counter)
            if extension not in app.config['ALLOWED_EXTENSIONS']:
                message = "You can only upload .jpeg, .jpg, .png files"
                return render_template('img.html', message=message)
            # Move the file form the temporal folder to the upload folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            source = UPLOAD_FOLDER + '/' + filename
            destination = UPLOAD_FOLDER + '/' + name + number + '.' + extension
            os.rename(source, destination)
            # Save the filename into a list, we'll use it later
            filenames.append(filename)

            # filename = secure_filename(file.filename)
            # if filename != '':
            #     file_ext = os.path.splitext(filename)[1]
            #     if file_ext not in app.config['ALLOWED_EXTENSIONS']:
            #         message = "You can only upload .jpeg, .jpg, .png files"
            #         return render_template('img.html', message=message)
            #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], "temp.jpg"))

            # flash("Your submission was successful!")
        return redirect(url_for('index'))
    else:
        return render_template("img.html")


if __name__ == '__main__':
    app.run()
