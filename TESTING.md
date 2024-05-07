# Welcome to Oasis Hotels Testing 

Return to [README](README.md)

Comprehensive testing has been performed to ensure the website's functionality meets expectations.

## Table of Contents

### [Responsiveness Testing](#responsiveness-testing-1)
### [Browser and Device Compatibility Testing](#browser-and-device-compatibility-testing-1)
### [Code Validation](#code-validation-1)
* [HTML Validation](#html-validation)
* [CSS Validation](#css-validation)
* [JavaScript Validation](#javascript-validation)
* [Python Validation](#python-validation)
### [Lighthouse Report](#lighthouse-report-1)
### [Bugs](#bugs-1)
### [Site Features Testing](#site-features-testing-1)

## Responsiveness Testing

The deployed website underwent testing on multiple devices and screen sizes to ensure its responsiveness and adaptability. Chrome Developer Tools were utilized to simulate various screen sizes. Bootstrap classes and media queries were implemented to help achieve the desired design, ensuring that the website maintains its visual and functional integrity on all platforms, in turn enhancing the user experience.

![I Am Responsive](/documentation/readme_images/i-am-responsive.png)

<details>
<summary> Desktop PC
</summary>

![Desktop PC](documentation/validation/desktop.png)
</details>

<details>
<summary> Laptop
</summary>

![Laptop](documentation/validation/laptop.png)
</details>

<details>
<summary> Tablet
</summary>

![Tablet](documentation/validation/tablet.png)
</details>

<details>
<summary> Mobile
</summary>

![Mobile](documentation/validation/mobile.png)
</details>

## Browser and Device Compatibility Testing

The project was tested on multiple web browsers to check for compatibility issues and ensure it functions as expected no matter the browser used. This testing process ensures that users will have a smooth and consistent user experience.

The site has been tested on the following browsers & devices:
* Google Chrome
* Safari
* Microsoft Edge
* Mozilla Firefox
* Iphone 12 Safari

The site functions as expected on all of the above browsers. I have tested the site on all browsers ans devices at my disposal to ensure the site is functional on different devices and platforms.

## Code Validation 

### HTML Validation

<details>
<summary> Home Page
</summary>

![Home Page](documentation/validation/html-validation-homepage.png)
</details>

<details>
<summary> Contact Page
</summary>

![Contact Page](documentation/validation/html-validation-contact.png)
</details>

<details>
<summary> Sign Up Page
</summary>

![Sign Up Page](documentation/validation/html-signup-validation.png)
</details>

<details>
<summary> Login Page
</summary>

![Login Page](documentation/validation/html-login-validation.png)
</details>

<details>
<summary> Logout Page
</summary>

![Logout Page](documentation/validation/html-logout-validation.png)
</details>

<details>
<summary> Browse Hotels Page
</summary>

![Browse Hotels Page](documentation/validation/html-hotel-booking-validation.png)
</details>

<details>
<summary> Make a Booking Page
</summary>

![Make a Booking Page](documentation/validation/html-make-a-booking-validation.png)
</details>

<details>
<summary> Booking Success Page
</summary>

![Booking Success Page](documentation/validation/html-booking-success-validation.png)
</details>

<details>
<summary> Booking Overview Page
</summary>

![Booking Overview Page](documentation/validation/html-booking-overview-validation.png)
</details>

<details>
<summary> Edit Booking Page
</summary>

![Edit Booking Page](documentation/validation/html-edit-booking-validation.png)
</details>

<details>
<summary> Delete Booking Page
</summary>

![Delete Booking Page](documentation/validation/html-delete-booking-validation.png)
</details>

<details>
<summary> 404 Error Page
</summary>

![404 Error Page](documentation/validation/html-404-validation.png)
</details>

<details>
<summary> 500 Error Page
</summary>

![500 Error Page](documentation/validation/html-500-validation.png)
</details> 

### CSS Validation

<details>
<summary> Custom CSS (style.css)
</summary>

![Custom CSS (style.css)](documentation/validation/css-validation.png)
</details>

### JavaScript Validation

<details>
<summary> Custom JS (script.js)
</summary>

![Custom JS (script.js)](documentation/validation/custom-js-validation.png)
</details>

<details>
<summary> Edit Booking Inline Script
</summary>

![Edit Booking Inline Script](documentation/validation/edit-booking-js-validation.png)
</details>

<details>
<summary> Make a Booking Inline Script
</summary>

![Make a Booking Inline Script](documentation/validation/make-booking-js-validation.png)
</details>

### Python Validation 

#### hotel_bookings app

<details>
<summary> admin.py
</summary>

![admin.py](documentation/validation/admin.py-validation.png)
</details>

<details>
<summary> forms.py
</summary>

![forms.py](documentation/validation/forms.py-validation.png)
</details>

<details>
<summary> models.py
</summary>

![models.py](documentation/validation/models.py-val.png)
</details>

<details>
<summary> views.py
</summary>

![views.py](documentation/validation/views.py-validation.png)
</details>

<details>
<summary> urls.py
</summary>

![urls.py](documentation/validation/urls.py-validation.png)
</details>

#### oasis_hotels app

<details>
<summary> settings.py
</summary>

![settings.py](documentation/validation/settings.py-validation.png)
</details>

<details>
<summary> urls.py
</summary>

![urls.py](documentation/validation/oasis-urls.py-validation.png)
</details>

## Lighthouse Report

<details>
<summary> Home Page
</summary>

![Home Page](documentation/lighthouse/lighthouse-homepage.png)
</details>

<details>
<summary> Home Page Logged in
</summary>

![Home Page Logged in](documentation/lighthouse/lighthouse-homepage-logged-in.png)
</details>

<details>
<summary> Contact Page
</summary>

![Contact Page](documentation/lighthouse/lighthouse-contact.png)
</details>

<details>
<summary> Sign Up Page
</summary>

![Sign Up Page](documentation/lighthouse/lighthouse-signup.png)
</details>

<details>
<summary> Login Page
</summary>

![Login Page](documentation/lighthouse/lighthouse-login.png)
</details>

<details>
<summary> Logout Page
</summary>

![Logout Page](documentation/lighthouse/lighthouse-logout.png)
</details>

<details>
<summary> Browse Hotels Page
</summary>

![Browse Hotels Page](documentation/lighthouse/lighthouse-browse-hotels.png)
</details>

<details>
<summary> Make a Booking Page
</summary>

![Make a Booking Page](documentation/lighthouse/lighthouse-make-booking.png)
</details>

<details>
<summary> Booking Success Page
</summary>

![Booking Success Page](documentation/lighthouse/lighthouse-booking-success.png)
</details>

<details>
<summary> Booking Overview Page
</summary>

![Booking Overview Page](documentation/lighthouse/lighthouse-booking-overview.png)
</details>

<details>
<summary> Edit Booking Page
</summary>

![Edit Booking Page](documentation/lighthouse/lighthouse-edit-booking.png)
</details>

<details>
<summary> Delete Page
</summary>

![Delete Page](documentation/lighthouse/lighthouse-delete-booking.png)
</details>

## Bugs 

### Recieving an IntegrityError when clicking on the 'Book Now' button on the Make a Booking page

* It appears that this error occured after i had added a new optional error to the booking model. Shortly after adding this new extra i removed all trace of it from the workspace and database. It seems that the data had casued a violation in the databses constraints. I was advised to perform a full databse reset using the **python3 manage.py dumpdata > fullDB.json** command. This resolved the issue and the site returned to a fully functional state.

### On some devices when viewing the bookings calendar, dates that have not been booked for a particular hotel are blanked out looking like they are booked dates

* This appears to be an intermitent issue that will not occur on the majority of the bookings made but has occured on a few. The Flatpick code seems to function as it should so this issue occuring in the low frequency that it has occured during testing is a slight mystery.

## Site Features Testing

| Page          | User Action   | Expected Result  | Notes            |
|---------------|---------------|------------------|------------------|
| Home Page     |               |                  |                  |
|               | Click on Logo | Redirect to Home Page | PASS        |
|               | Click on Sign Up button | Redirect to Sign Up page | PASS |
|               | Click on Login Button | Redirect to Login page | PASS |
|               | Click on Sign Up button (Navigation bar) | Redirect to Sign Up page | PASS |
|               | Click on About (Navigation bar) | Move to about section | PASS |
|               | Click on Contact (Navigation bar) | Redirect to Contact page | PASS |
|               | Click on Login (Navigation bar) | Redirect to Login page | PASS |
|               | Click on carousel | Redirect to sign up page | PASS |
|               | Click on carousel control | Move left, move right | PASS |
|               | Click on social links in footer | Open new tab with appropriate link | PASS |
| Home Page (Logged In - User)  |                 |          |  |
|               | After a user has Logged in | Sign Up/Login button is now Book Now button | PASS |
|               | Click on Book Now | Redirect to browse hotels page | PASS |
|               | Click on hotel carousel | Redirects to browse hotels page | PASS |
|               | After Login/Sign Up | Users name is displayed in navigation bar | PASS |
|               | Click on users name | dropdown menu opens | PASS |
|               | Click on My Booking in dropdown | Redirect to Booking Overview page | PASS |
|               | Click on Make a Booking in dropdown | Redirect to browse hotels page | PASS |
|               | Click on Logout | Redirect to Logout Page | PASS |
| Home Page (Logged In - Admin)    |               |                  |                  |
|               | Click on admin name | Open dropdown menu | PASS |
|               | Click on My Booking in dropdown | Redirect to Booking Overview page | PASS |
|               | Click on Admin Panel | Redirect to Django Admin Panel | PASS |
| Sign Up Page  |                  |                  |                  |
|               | Enter invalid email | Field will only accept email address format | PASS |
|               | Enter valid email | No error | PASS |
|               | Email field left empty | Email is optional | PASS |
|               | Type invalid password | Must contain atleast 8 char | PASS |
|               | Type valid password | No error | PASS |
|               | Type password again (different) | Password must be the same | PASS |
|               | Click Sign Up with empty form | Fill in the form fields | PASS |
|               | Click Sign In if you have an account | Redirect to Login page | PASS |
|               | Fill all the form fields | Account created, alert message that you Signed in | PASS |
| Login Page  |                  |                  |                  |
|               | Click on Sign Up, if you don't have an account | Redirect to Sign Up page | PASS |
|               | Try invalid username | Username is not correct | PASS |
|               | Try invalid password | Password is not correct | PASS |
|               | Valid password and username | Logs in, message that you signed in | PASS |
|               | Click Sign In with empty form | Fill in the form fields | PASS |
| Logout Page  |                  |                  |                  |
|               | Click on Sign Out button | Sign user out, message that user signed out | PASS |
| Browse Hotels Page  |                  |                  |                  |
|               | Click on Book Now on any Hotel | Redirects to selected hotel booking form | PASS |
|               | Click on Next button | Moves to another page, displays next page of hotels | PASS |
|               | Click on Previous button | Goes back to previous page | PASS |
| Make a Booking Page  |                  |                  |                  |
|               | Click on Book Now button while form is empty | Fill in the form fields, alert message | PASS |
|               | Try to select dates in the past | They are disabled | PASS |
|               | Try to select already booked dates | They are disabled, unavailable until dates become available is someone deletes their booking         | PASS |
|               | Try to overlap your booking around the already booked dates | Hotels already booked for those dates, alert message | PASS |
|               | Input more guests than maximum guests | Can't exceed maximum guests, alert message | PASS |
|               | Input 0 guests | Guests must be  1 minimum, alert message | PASS |
|               | Input more breakfasts than number of guests | Can't buy more breakfasts than number of guests | PASS |
|               | Input less than 0 breakfasts | Can't select less than 0 breakfasts, alert message | PASS |
|               | Input less than 0 kids club tickets | Can't select less than 0 tickets, alert message | PASS |
|               | Input 0 breakfasts | breakfasts are optional, no error | PASS |
|               | Input 0 kids club tickets | tickets are optional, no error | PASS |
|               | maximum amount of kids club tickets is 10 | Anything over 10 will not be accepted, alert message | PASS |
|               | Try to make check out date be before check in date | Check out can't be before check in, alert message | PASS |
|               | Enter valid form data | Booking Succesful, alert message | PASS |
|               | User fills in only check in, check out and number of guests | Booking Succesful, extras are optional | PASS |
| Booking Succesful Page |  |    |    |
|               | Read the booking details | Details are as expected, match users booking | PASS |
|               | Click on Contact Us button | Redirect to Contact page | PASS |
|               | Click on My Booking button | Redirects to Booking Overview page | PASS |
| Booking Overview Page |  |    |    |
|               | Read the bookings | Results match users bookings and details of bookings | PASS |
|               | Click on Edit button | Redirect to Edit Booking page | PASS |
|               | Click on Delete button | Redirect to Delete Booking page | PASS |
| Edit Booking Page |  |    |    |
|               | Try to select dates in the past | They are disabled | PASS |
|               | Try to select already booked dates | They are disabled, unavailable until dates become available is someone deletes their booking         | PASS |
|               | Try to overlap your booking around the already booked dates | Cabins already booked for those dates, alert message | PASS |
|               | Input more guests than maximum guests | Can't exceed maximum guests, alert message | PASS |
|               | Input 0 or less than 0 guests | Guests can't be less than 0, alert message | PASS |
|               | Input more breakfasts than number of guests | Can't buy more breakfasts than number of guests | PASS |
|               | Input less than 0 breakfasts | Can't select less than 0 breakfasts, alert message | PASS |
|               | Input less than 0 kids club tickets | Can't select less than 0 tickets, alert message | PASS |
|               | Input 0 kids club tickets | tickets are optional, no error | PASS |
|               | Input 0 tickets | tickets are optional, no error | PASS |
|               | maximum amount of kids club tickets is 10 | Anything over 10 will not be accepted, alert message | PASS |
|               | Try to make check out date be before check in date | Check out can't be before check in, alert message | PASS |
|               | Click on Save Changes button | Booking updated succesfully | PASS |
|               | Enter valid form data | Booking succesfully updated | PASS |
|               | User fills in only check in, check out and number of guests | Booking succesfully updated, extras are optional | PASS |
| Delete Booking Page |  |    |    |
|               | Read the booking ID number | It displays correct Id number of chosen hotel booking user wants to delete | PASS |
|               | Click on Confirm Delete button | Booking is deleted and user is returned to Booking Overview, alert message | PASS |
|               | Click on Cancel button | Redirect back to Booking Overview page | PASS |
| 404 Error Page |  |    |    |
|               | Type in URL that does not exists | Custom 404 Error page is displayed | PASS |
|               | Click on Home button | Redirect to Home page | PASS |
| 500 Error Page |  |    |    |
|               | Admin raise exception in views.py | Custom 500 Error page is displayed, local development testing | PASS |
|               | Click on Home button | Redirect to Home page | PASS |
| Admin Panel |  |    |    |
|               | CRUD functionality | Working as expected | PASS |

Return to [README](README.md)