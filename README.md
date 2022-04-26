## CITY GUIDE FOR MINIS
___

### Video Demo:  <https://www.youtube.com/watch?v=F0itNOsWQqg>
___

### Description
___
CITY GUIDE FOR MINIS is a simple web-based application which goal is to give young families from Hamburg, Germany, a helping hand with planning and organising family activities and kids entertainment. 
This application was designed and developed as a final project for [Harvard CS50](https://cs50.harvard.edu/x/2022/) course. 
 

### Functionality
___

+ The app provides the list of kids-friendly locations 
+ Main page contains an interactive map with icons
+ Detailed overview of each place with photos gallery
+ Ability to suggest a new location and upload pictures
+ Ability to contact the authors 
+ Places suggestion and contact form details are stored at database
+ Information about the project



### Technology Stack
___
* HTML
* CSS/Bootstrap
* JavaScript
* Python
* Flask 
* SQLite
* Leaflet JS library

The Back-end side is written in **Python**, using the **Flask** framework.

All the data is stored in **SQLite** databases:
* In table "Contact"  we store user information (name, last name, email address and text message).
* In table "Places" the information about the suggested location (name, address, contacts, description and pictures) is stored. 


The Front-end side is written with some **JavaScript** and **Leaflet** JS open-source library:
* To create a photos gallery slide for any location page.
* To create an interactive map, markers and pop-ups. 
* To create an interaction between the list of places and their location on the map


The **CSS** and **CSS Bootstrap** are used to make the user interface responsive on any device.

### Project Structure
___

#### Home page
___
This page contains the list of Hamburg kids-friendly places as well as an interactive map which shows the exact location of each place. 
Each marker at the map has a pop-up with some basic information about this place. When a user hovers over a place, the corresponding map marker is highlighted. 

![main page](https://i.ibb.co/rmPtg2H/main-page.png)

#### Location Page
___
When a user clicks on the location card at the main page, he/she is redirected to the location page. The page contains the photos gallery and detailed information of the place (such as place description and contact details).

![location example](https://i.ibb.co/rmH8QY0/location-example.png)

#### Add a Place
___
A user has an opportunity to add (suggest) a new location themselves. To do this he/she need to fill out the form with required fields (the correctness check is carried out at the back-end). Also a user needs to upload at least 4 pictured of a place (only allowed extensions: .jpeg, .jpg, .png). After submission the place suggestion will be stored at the database (table "Places") with the field "active" == "no", then it will be reviewed by project admin and in case of validity and correctness the place will be displayed at the main page.

![add place](https://i.ibb.co/N1sC41P/add-place.png)
#### About City4Minis
___
This page provides some information about the project, its main idea and its authors.

![about page](https://i.ibb.co/KVWHhKY/about.png)

#### Contact Us
___
The page Contact us provides contact details through social media as well as a contact form that can be used to send a message to the project creators. The message and the user details will be stored at the database (table "Contact").

![contact us page](https://i.ibb.co/825WFwS/contact-us.png)

### Installation
___

1. Star and clone the repository to your machine.

2. Run the command ```pip install -r requirements.txt```

3. Once all the dependancies have been installed, run the command ```flask run```

4. This should start a local server and you can access it on your browser.

If you are facing any issues, bugs or just have a question or suggestion, please feel free to contact me or to send a Pull Request on GitHub.

