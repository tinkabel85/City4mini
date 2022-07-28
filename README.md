# CITY GUIDE FOR MINIS
___

### [Video Demo](https://www.youtube.com/watch?v=F0itNOsWQqg)
___

### About The Project

CITY GUIDE FOR MINIS is a simple web-based application which goal is to give young families from Hamburg, Germany, a helping hand with planning and organising family activities and kids entertainment. 
This application was designed and developed as a final project for [Harvard CS50](https://cs50.harvard.edu/x/2022/) course. 
 
___

### Functionality

+ The app provides the list of kids-friendly locations 
+ Main page contains an interactive map with icons
+ Detailed overview of each place with photos gallery
+ Ability to suggest a new location and upload pictures
+ Ability to contact the authors 
+ Places suggestion and contact form details are stored at database
+ Information about the project

___

### Built With

![JavaScript](https://img.shields.io/badge/-JavaScript-black?style=flat-square&logo=javascript) &nbsp;
![HTML5](https://img.shields.io/badge/-HTML5-E34F26?style=flat-square&logo=html5&logoColor=white) &nbsp;
![CSS3](https://img.shields.io/badge/-CSS3-1572B6?style=flat-square&logo=css3) &nbsp;
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=flat-square&llogo=bootstrap&logoColor=white) &nbsp;
![Python](https://img.shields.io/badge/-Python-black?style=flat-square&logo=Python) &nbsp;
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white) &nbsp;
![Leaflet](https://img.shields.io/badge/Leaflet_JS-green?style=flat-square&llogo=leaflet&logoColor=white) &nbsp;
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=flat-square&logo=sqlite&logoColor=white) &nbsp;


The Back-end side is written in **Python**, using the **Flask** framework.

All the data is stored in **SQLite** databases:
* In table "Contact"  we store user information (name, last name, email address and text message).
* In table "Places" the information about the suggested location (name, address, contacts, description and pictures) is stored. 


The Front-end side is written with **JavaScript** and **Leaflet** JS open-source library:
* To create a photos gallery slide for any location page.
* To create an interactive map, markers and pop-ups. 
* To create an interaction between the list of places and their location on the map


The **CSS** and **CSS Bootstrap** are used to make the user interface responsive on any device.
___

### Project Structure

#### Home page

This page contains the list of Hamburg kids-friendly places as well as an interactive map which shows the exact location of each place. 
Each marker at the map has a pop-up with some basic information about this place. When a user hovers over a place, the corresponding map marker is highlighted. 

![main page](https://i.ibb.co/rmPtg2H/main-page.png)

#### Location Page

When a user clicks on the location card at the main page, he/she is redirected to the location page. The page contains the photos gallery and detailed information of the place (such as place description and contact details).

![location example](https://i.ibb.co/rmH8QY0/location-example.png)

#### Add a Place

A user has an opportunity to add (suggest) a new location themselves. To do this he/she need to fill out the form with required fields (the correctness check is carried out at the back-end). Also a user needs to upload at least 4 pictured of a place (only allowed extensions: .jpeg, .jpg, .png). After submission the place suggestion will be stored at the database (table "Places") with the field "active" == "no", then it will be reviewed by project admin and in case of validity and correctness the place will be displayed at the main page.

![add place](https://i.ibb.co/N1sC41P/add-place.png)

#### About City4Minis

This page provides some information about the project, its main idea and its authors.

![about page](https://i.ibb.co/KVWHhKY/about.png)

#### Contact Us

The page Contact us provides contact details through social media as well as a contact form that can be used to send a message to the project creators. The message and the user details will be stored at the database (table "Contact").

![contact us page](https://i.ibb.co/825WFwS/contact-us.png)

___
###  Getting Started 

#### `Step 1` - clone the repo
```bash
$ git clone https://github.com/tinkabel85/City4mini.git
```

#### `Step 2` - cd in the repo

```bash
$ cd City4mini
```

#### `Step 3` - install dependencies

+ Run the command ```pip install -r requirements.txt```

#### `Step 4` - run application

+ Once all the dependancies have been installed, run the command ```flask run```
```bash
$ flask run
```

This should start a local server and you can access it on your browser.

---
<div align="center">
    <sub>If you found a bug or some improvments, feel free to raise an issue and send a PR!</sub>
</div>