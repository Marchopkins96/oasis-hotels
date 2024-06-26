# Oasis Hotels

Our Django based website is a platform for users to explore and book a wide range of hotels. Oasis Hotels is an exclusive selection of stunning fine hotels and resorts spread all around the globe. Each one is unique, offering a combination of charm, character, and luxury. Also, they are all in excellent locations, whether you are looking for a quiet getaway or want something for the whole family.


![Home Screen](/documentation/readme_images/i-am-responsive.png)

[View Oasis Hotels live website here](https://oasis-hotels-a4728551ae39.herokuapp.com/)

## Table of Contents
### [User Experience](#user-experience-1)
* [Project Goals](#project-goals)
* [Agile Methodology](#agile-methodology)
* [User Stories](#user-stories)
* [Target Audience](#target-audience)
* [First Time User](#first-time-user)
* [Registered User](#registered-user)
* [Admin User](#admin-user)
### [Design](#design-1)
* [Color Scheme](#color-scheme)
* [Hotel Images](#hotel-images)
* [Wireframes](#wireframes)
* [Data Model](#data-models)
* [Database Scheme](#database-scheme)
### [Security Features](#security-features-1)
### [Features](#features-1)
* [Existing Features](#existing-features)
* [Features to Implement in Future](#features-to-implement-in-future)
### [Technologies Used](#technologies-used-1)
* [Languages Used](#languages-used)
* [Databases Used](#databases-used)
* [Frameworks Used](#frameworks-used)
* [Programs Used](#programs-used)
### [Deployment and Local Deployment](#deployment-and-local-developement)
* [Local Development](#local-developement)
* [ElephantSQL Database](#elephantsql-database)
* [Cloudinary](#cloudinary)
* [Heroku Deployment](#heroku-deployment)
### [Testing](#testing-1)
### [References](#references-1)
* [Docs](#docs)
* [Content](#content)
* [Acknowledgements](#acknowledgements)


## User Experience

Our website offers the user intuitive navigation, eye catching visuals, and a quick and easy booking process. Oasis Hotels website can be accessed on a range of devices making it easy to make a booking on the device of your choice. Discover your next holiday destination with Oasis Hotels who are here to make that proccess as enjoyable and stress free as possible.

### Project Goals

The goal of the Oasis Hotels project is to create a user-friendly online platform that allows visitors to browse, and book available hotels at their own leisure. The project aims to provide a stress free user experience, making navigation around the site as easy as possible to enhance the positive feeling for visitors to the site.

### Agile Methodology

Agile was used to help prioritize and organise the tasks that related to the creation of the project. User stories and Project Boards on GitHub providing the tools to do this. A template was created to help create user stories.

* User stories were created based on what will be included, should be included and could be included.
* Project Board is set to public view
* Project Board was used to track the project progress through the Todo, In progress and Done columns
* Labels used to catergorise issues based on importance

<details>
<summary> User Stories Template
</summary>

![User Stories Template](documentation/readme_images/user-story-template.png)
</details>

<details>
<summary> User Stories, Issues
</summary>

![User Stories, Issues](documentation/readme_images/user-story-issues.png)
</details>

<details>
<summary> Project Board
</summary>

![User Stories, Issues](documentation/readme_images/project-board.png)
</details>

### User Stories

1. Initial Deployment 
* Create a new Heroku application
* Link GitHub repository to the new Heroku app
2. Home Page
* Create a navigation bar
* Create a footer
3. User Registration
* Sign up page
* User registration, log in, log out functions
* Username displays on screen
4. Website Admin and Bookings
* Alert messages
* CRUD functionality
* Hotel pagination
* Admin panel
* Double bookings
* Book extras
4. Maintain consistent design with responsiveness in mind
* Maintain consistent design throughout the website
* Test responsiveness

For a more detailed look at user stories please see [project board](https://github.com/users/Marchopkins96/projects/6)

### Target Audience

* Couples & families planning their next getaway in the sun
* People who like to book things quickly and easily
* Mobile users who enjoy conveniently booking from their device
* People who enjoy a visually appealing experience

### First time user

* Users are greeted with a simple and intuitive navigation bar making it easy to explore the website
* Users are drawn in by eye catching color and design 
* content dispaying an overview of the company and what it has to offer a user
* Forms are easy to naviagate with clear validation messages to ensure accurate information in inputted
* quick and easy registration process

### Registered User

* Login process is quick and easy to navigate
* username displayed once logged in
* Browse available hotels
* Booking of hotels
* Ability to view booking history and any upcoming reservations
* Easily delete or modify bookings

### Admin user

* Secure login portal for admin users who have the rights to access it
* Access to the admin dashboard to manage hotels, extras and bookings
* Ability to add, edit and delete hotel listings
* Ability to add, edit and delete extras options
* Delete user accounts, providing the necessary control for managing user data
* Management of bookings, abiliity to view, delete or modify bookings

## Design

The Oasis Hotels website is invitiing and visually pleasing. Boasting a warm color pallette to give the feeling of a warm summers evening. The navigation bar features a company logo with clear easy to read textual content. Hotel photos are displayed in a bordered carousel to aid the user experience. The about section is placed on a white background the contrast the background of the home page nicely. Social links are featured in the footer section.

### Color Scheme
![Color Scheme](documentation/readme_images/colorscheme.png)

### Hotel Images 

All the hotel images were created using Artificial Inteligence, AI image generator [Craiyon](https://www.craiyon.com/)

### Logo 

The Logo was also created at [Craiyon](https://www.craiyon.com/)

### Typography 

The 'Quicksand' font is the primary font used with 'Serif' provided as a back up

### Wireframes 

<details>
<summary> Home Page
</summary>

![Home Page](documentation/wireframes/wf-homepage.png)
</details>

<details>
<summary> Home Page when logged in
</summary>

![Home Page when logged in](documentation/wireframes/wf-homepage-logged-in.png)
</details>

<details>
<summary> Contact Page
</summary>

![Contact Page](documentation/wireframes/wf-contact-page.png)
</details>

<details>
<summary> Hotel Booking Page
</summary>

![Hotel Booking Page](documentation/wireframes/wf-hotel-booking-page.png)
</details>

<details>
<summary> Make a Booking Page
</summary>

![Make a Booking Page](documentation/wireframes/wf-make-a-booking.png)
</details>

<details>
<summary> My Booking Page
</summary>

![My Booking Page](documentation/wireframes/wf-my-booking-page.png)
</details>

<details>
<summary> Edit Booking Page
</summary>

![Edit Booking Page](documentation/wireframes/wf-edit-booking-page.png)
</details>

<details>
<summary> Delete Booking Page
</summary>

![Delete Booking Page](documentation/wireframes/wf-delete-booking-page.png)
</details>

<details>
<summary> User Login Page
</summary>

![User Login Page](documentation/wireframes/wf-user-login-page.png)
</details>

<details>
<summary> User Logout Page
</summary>

![User Logout Page](documentation/wireframes/wf-user-logout-page.png)
</details>

<details>
<summary> User Sign Up Page
</summary>

![User Sign Up Page](documentation/wireframes/wf-user-signup-page.png)
</details>

### Data Models

1. AllAuth User Model
    * Django Allauth, the User model is the default user model provided by the Django authentication system
    * The User entity has a one-to-many relationship with the Booking entity. This means that a User can have multiple Bookings, but each Booking is associated with only one User.
---
2. Extras Model
    * Data model created so admin can add extras to the hotel booking, and control the names of extras
    * Only Admin can change the data in the backend.
    * User can book those extras through the Booking Model
    * An extra can be associated with multiple Hotels, and a Hotel can have multiple extras. This is represented by the many-to-many relationship between Extras and Hotel.
    * There are two extras set up, which are breakfast included and kids club tickets
---
3. Hotel Model
    * A Hotel can have multiple Bookings, but each Booking is associated with only one Hotel. This is represented by the foreign key relationship between Hotel and Booking.
    * Admin can add Hotels through djangos admin panel.
    * Only Admin can change the data in the backend.
    * User can see the hotel information and image based on the chosen hotel.
    * Information provided is image, description, maximum guests, extras
---
4. Booking Model
    * A User can have multiple Bookings, but each Booking is associated with only one User. This is represented by the foreign key relationship between User and Booking.
    * Booking model has a feature that prevents overlapping bookings, so users dont book on the same dates
    * Full CRUD functionality is available to the user.
    * User in order to book has to fill check-in, check-out dates, number of guests and optional extras
    ---

### Database Scheme

Entity Relationship Diagram (ERD)

![DataScheme](documentation/readme_images/erd-diagram.png)

* The Extras entity represents extras that can be associated with hotels, with fields id as the primary key, name for the extras's name
* The Hotel entity represents individual hotel listings, with fields id as the primary key, name for the hotel's name, description for the hotel's description, image for the hotel's image and max_guests for the maximum number of guests allowed
* The Booking entity represents a booking made by a user for a specific hotel, with fields id as the primary key, hotel_id as a foreign key referencing the Hotel entity, user_id as a foreign key referencing the User entity, check_in_date for the booking's check-in date, check_out_date for the booking's check-out date, num_guests for the number of guests in the booking, breakfast_included for the optional quantity of breakfast's included, kids_club_tickets for the optional quantity of kids club tickets within the booking.

This data scheme allows for the management of users, extras, hotels, and bookings. Users can make bookings for specific hotels, and each booking can have associated details such as the check-in and check-out dates, number of guests, and optional extras.

## Security Features 

### User Authentication

* Django Allauth is a popular authentication and authorization library for Django, which provides a set of features for managing user authentication, registration, and account management.

### Login Decorator

* booking_create, booking_success, booking_overview, edit_booking, and delete_booking: These views involve operations related to user bookings and require authentication with the login_required decorator.
* This ensures that only authenticated users can access these views.

### CSRF Protection

* Django provides built-in protection against Cross-Site Request Forgery (CSRF) attacks. CSRF tokens are generated for each user session, and they are required to submit forms or perform state-changing actions. When a user logs out, the session and associated CSRF token are invalidated, making it difficult for an attacker to forge a valid request using a copied URL.

### Form Validation

* The booking_create view validates form input using the BookingForm class. It checks for various validation errors, such as the number of guests, check-in and check-out dates, overlapping bookings, and additional validations for breakfast incldued and kids club tickets

### Overlapping Booking

* In the booking_create view, the code checks for overlapping bookings by querying the database for existing bookings that match certain conditions. It compares the selected check-in and check-out dates with the dates of existing bookings for the same hotel. If any overlapping bookings are found, an error message is added to the form, and a warning message is displayed to the user

### Custom error pages

* 404 Error Page, provides user with a button the redirect to home page
* 500 Error Page, provides user with a button the redirect to home page

## Features

* Home page showcases a rotating carousel that contains the hotels available
* The Home page features a reasons section stating why to choose Oasis Hotels with an about section at the bottom of the page
* User can make an account and login
* When logged in, users get access to the hotel overview and are able to book hotels
* Users can edit and delete their bookings
* Every user action is accompanied by a corresponding message to ensure that users are promptly notified of any changes or updates

### Existing Features

* Home Page
    * Displays a navigation bar with logo, main heading, reasons section, carousel of hotels available, about section, footer with social links

![Home Page](documentation/readme_images/home-page.png)

* Once a user is logged in the Sign Up button changes to Book Now button

* Logo
    * Logo was created using [Craiyon](https://www.craiyon.com/) AI image generator, palm trees and sun being the key words

![Logo](documentation/readme_images/logo.png)

* Navigation Bar
    * It differs depending on if its a user, admin or just a visitor visiting the site

    * Navigation bar for a visitor

    ![Visitor](documentation/readme_images/visitor-nav.png)

    * Navigation bar for a user
    ![User](documentation/readme_images/user-nav.png)
    * Drop down menu allows users to make a booking and view existing bookings

    * Navigation bar for admin
    ![Admin](documentation/readme_images/admin-nav.png)
    * Admin bar accessible via dropdown option

* Reasons section
    * Section with a few reasons on why a user should use Oasis Hotels

    ![Reasons](documentation/readme_images/reasons.png)

* Hotel Carousel
    * When on home page there is a carousel that displays all available hotels for booking, it also has controls to move left or right, name and description of the hotel, when its clicked it redirects users to hotel overview page and visitors are asked to create an account or login in order to view the hotels in more detail.

![Hotel Carousel](documentation/readme_images/carousel.jpeg)

* About Section
    * It contains a description about Oasis Hotels

![About](documentation/readme_images/about-us.png)

* Footer
    * Contains copyright information, creator and social links

![Footer](documentation/readme_images/footer.png)

* Contact Page
    * For educational purposes, the website includes fictional contact information such as an address, phone number, and email.

![Contact](documentation/readme_images/contact-page.png)

* Sign up
    * User can create an account

![Sign Up](documentation/readme_images/user-signup.png)

* Login
    * User can login into an account, if they have created one

![Login](documentation/readme_images/user-signin.png)
![Login Message](documentation/readme_images/signin-succesful.png)

* Logout
    * User can logout

![Logout](documentation/readme_images/user-signout.png)

* Browse Available Hotels
    * Admin can create hotels through django admin panel
    * Hotels are paginated to display 6 hotels per page

![Browse Hotels](documentation/readme_images/available-hotels.jpeg)

* Hotel pagination
    * On the bottom of the page

![Pagination](documentation/readme_images/pagination.png)

* Make a Booking
    * Users can make a booking by clicking the hotel they want and then read details and fill in the booking form
    * Form validation is implemented to make sure form are submitted correctly and if there is an error user will be notified with alert message, also if everything is okay, user gets a message to notifiy them of that
    * Form contains extras which are completely optional and they dont have to be selected by the user

    ![Message](documentation/readme_images/booking-succesful-banner.png)

![Make a Booking](documentation/readme_images/make-a-booking.png)

* Booking Succesful
    * If booking is succesfull, user gets a notified message and an overview of the booking they just made, which includes all the details and also there is a button for the contact page and my bookings that takes the user to a list of all user bookings

![Booking Succesful](documentation/readme_images/Booking-succesful.png)

* Booking Overview
    * Includes all of the user bookings, which have buttons to edit or delete bookings.

![Booking Overview](documentation/readme_images/booking-overview.jpeg)

* Already booked dates
    * User won't be able to book dates that are already booked.
    * Dates in the past are unavailable.
    * Booked dates blanked out on the calendar

![Booked Dates](documentation/readme_images/already-booked-dates.png)

* Edit Booking
    * User can edit their booking and save changes

![Edit Booking](documentation/readme_images/edit-booking.png)

* Delete Booking
    * User can delete their booking, before it is deleted it has to be confirmed.

![Delete Booking](documentation/readme_images/confirm-delete.png)

* Alert messages
    * For every action by a user there is an alert message to notify them
    * Here is an example 

![Alert Message](documentation/readme_images/alert-message.png)

* Error Pages
    * There are custom 404 and 500 error pages
    * They contain buttons to redirect to home page if an error is encountered

![Error 404](documentation/readme_images/404.png)
![Error 500](documentation/readme_images/500.png)

* Admin Features
    * Django built in admin panel allows admin control over the website.
    * Admin can access admin panel through the navigation bar
    * Can add, update, delete hotels.
    * Create extras, update existing extras which are connected to the hotels on the website.
    * Delete accounts, verifiy emails, delete bookings

### Features To Implement In Future

* User Reviews: Allow users to leave reviews and ratings for hotels they have booked, providing valuable feedback for other users
* Add a pricing scale to hotels and extras
* Advanced Search: Implement an advanced search functionality, enabling users to search for hotels based on specific criteria such as price range and availability
* Add an online payment option to allow for easy payment to coinside with the ease of booking

## Technologies Used

### Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Databases Used

* [ElephantSQL](https://www.elephantsql.com/) - Postgres database
* [Cloudinary](https://cloudinary.com/) - Online static file storage

### Frameworks Used

* [Django](https://www.djangoproject.com/) - Python framework
* [Bootstrap 4.6.1](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - CSS framework

### Programs Used

* [Github](https://github.com/) - Storing the code online
* [Gitpod](https://www.gitpod.io/) - To write the code.
* [Heroku](https://www.heroku.com/) - Used as the cloud-based platform to deploy the site.
* [Google Fonts](https://fonts.google.com/) - Import main font the website.
* [Balsamiq](https://balsamiq.com/wireframes/) - Used to create wireframes
* [Lucid Chart](https://lucidchart.com/) - Used to create ERD diagram
* [Craiyon](https://www.craiyon.com/) - Generate AI images of hotels and logo
* [Am I Responsive](https://ui.dev/amiresponsive) - To show the website image on a range of devices.
* [Git](https://git-scm.com/) - Version control
* [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) - Templating engine
* [Favicon Generator](https://realfavicongenerator.net/) - Used to create a favicon
* [JSHint](https://jshint.com/) - Used to validate JavaScript
* [W3C Markup Validation Service](https://validator.w3.org/) - Used to validate HTML
* [CSS Validation Service](https://jigsaw.w3.org/css-validator/) - Used to validate CSS
* [CI Python Linter](https://pep8ci.herokuapp.com/#) - Used to validate Python
* [Coolers](https://coolors.co/) - Color Scheme

## Deployment and Local Developement

Live deployment can be found on this [View Oasis Hotels live website here](https://oasis-hotels-a4728551ae39.herokuapp.com/)

### Local Developement

#### How to Fork
1. Log in(or Sign Up) to Github
2. Go to repository for this project [Oasis Hotels](https://oasis-hotels-a4728551ae39.herokuapp.com/)
3. Click the fork button in the top right corner

#### How to Clone
1. Log in(or Sign Up) to Github
2. Go to repository for this project [Oasis Hotels](https://github.com/Marchopkins96/oasis-hotels)
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type the following command in the terminal (after the git clone you will need to paste the link you copied in step 3 above)
6. Set up a virtual environment (this step is not required if you are using the Code Institute Template in GitPod as this will already be set up for you).
7. Install the packages from the requirements.txt file - run Command pip3 install -r requirements.txt

### ElephantSQL Database
[Oasis Hotels](https://github.com/Marchopkins96/oasis-hotels) is using [ElephantSQL](https://www.elephantsql.com/) PostgreSQL Database

1. Click Create New Instance to start a new database.
2. Provide a name (this is commonly the name of the project: tribe).
3. Select the Tiny Turtle (Free) plan.
4. You can leave the Tags blank.
5. Select the Region and Data Center closest to you.
6. Once created, click on the new database name, where you can view the database URL and Password.

### Cloudinary
[Oasis Hotels](https://github.com/Marchopkins96/oasis-hotels) is using [Cloudinary](https://cloudinary.com/)
1. For Primary interest, you can choose Programmable Media for image and video API.
2. Optional: edit your assigned cloud name to something more memorable.
3. On your Cloudinary Dashboard, you can copy your API Environment Variable.
4. Be sure to remove the CLOUDINARY_URL= as part of the API value; this is the key.

### Heroku Deployment
* Log into [Heroku](https://www.heroku.com/) account or create an account.
* Click the "New" button at the top right corner and select "Create New App".
* Enter a unique application name
* Select your region
* Click "Create App"

#### Prepare enviroment and settings.py
* In your GitPod workspace, create an env.py file in the main directory.
* Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
* Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
* Comment out the default database configuration.
* Save all files and make migrations.
* Add the Cloudinary URL to env.py
* Add the Cloudinary libraries to the list of installed apps.
* Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
* Link the file to the templates directory in Heroku.
* Change the templates directory to TEMPLATES_DIR
* Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com']

#### Add the following Config Vars in Heroku:

* SECRET_KEY - This can be any Django random secret key
* CLOUDINARY_URL - Insert your own Cloudinary API key
* PORT = 8000
* DISABLE_COLLECTSTATIC = 1 - this is temporary, and can be removed for the final deployment
* DATABASE_URL - Insert your own ElephantSQL database URL here

#### Additional files needed for Heroku to deploy properly

* requirements.txt
* Procfile

#### Deploy

1. Make sure DEBUG = False in the settings.py
2. Go to the deploy tab on Heroku and connect to GitHub, then to the required repository.
3. Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the GitHub repository is updated.
4. Click 'Open App' to view the deployed live site.

Site is now live

## Testing
Please see  [TESTING.md](TESTING.md) for all the detailed testing performed.

## References
### Docs

* [Stack Overflow](https://stackoverflow.com/)
* [Code Institute](https://learn.codeinstitute.net/dashboard)
* [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
* [Django docs](https://docs.djangoproject.com/en/4.2/releases/3.2/)
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)
* [Django and Static Assets](https://devcenter.heroku.com/articles/django-assets)
* [Cloudinary](https://cloudinary.com/documentation/diagnosing_error_codes_tutorial)
* [Google](https://www.google.com/)
* [W3 Schools](https://www.w3schools.com/)

### Code & Content 

* Code from [Woodland Whispers Retreat](https://github.com/Thomas-Tomo/woodland-whispers-retreat) was used and adapted in the making of this project
* All images were generated with Artificial intelligence (AI) using unique keywords

### Acknowledgements

* I would like to thank my mentor for the support and feedback throughout this project, Mitko Bachvarov.
* I would also like to thank my fellow students of the slack community who will also look to help where possible and share knowledge