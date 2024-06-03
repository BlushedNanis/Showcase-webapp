# Showcase Website (Django)

The website was made to be simple to use and minimalistic, with a focus on showcasing projects and user profile. In order to make the website dynamic and simple for the administrator to maintain, it is built using Django models. Additionally, there's a contact form that, when completed, sends an email to both the administrator and the user.

Because Bootstrap 5 is so user-friendly and produces archivable visual results, all of the HTML style is done with it.

## Django models

1.**Profile data****:** intended to have a single entry that allows the administrator to add and modify user profile details.

Fields:

* Name
* Description
* Title
* Extra1
* Extra2
* Image
* Created date
* Updated date

*Note: The two extra fields, extra1 and extra2, are designed to supplement the profile data with additional information and format it according to the administrator's preferences. In this example, I use extra1 to show bullet points and extra2 to add a paragraph below the bullet points.*

2.**Projects data:** Here the administrator can store all the projects to showcase which will be dinamically displayed in the website on 3 columns in a descendent order from the updated date.

Fields:

* Title
* Description
* Link
* Image
* Created date
* Updated date

*Note: Given that the website has a github icon for every project, the link field is intended to be a github link.*

3.**Contact form:** To keep track of them, all completed forms will be kept here.

Fields:

* Name
* Email
* Subject *predefined subjects list*
* Message
* Timestamp
* Email sent
* Email received

*Note: The purpose of email sent and received tracking is to monitor email delivery success and identify any technical issues.*

## How to use?

* Install requirements.txt
* Create a *.env* file and set the next environment variables:

  * *email:* Gmail address which will serve as the sender
  * *password:* *Gmail app password*
* Create a new admin account with the command *python manage.py createsuperuser*
* Run with the command *python manage.py runserver*
* Add your information to the Djando models through */admin*
* Optional: Customize the website to your linkings, this can be done by modifying the *html files* located at *showcase/templates*
* Optional: Customize the Django models, you can add or delete fields from the models through showcase/models.py

*Important: Please remember to abide by [Django&#39;s security recommendations](https://docs.djangoproject.com/en/5.0/topics/security/) if you intend to utilize this project! *

## Essential resources


[The web framework for perfectionists with deadlines | Django (djangoproject.com)](https://www.djangoproject.com/)

[Bootstrap · The most popular HTML, CSS, and JS library in the world. (getbootstrap.com)](https://getbootstrap.com/)

## Screenshots

* Home page:
* Projects page:
* Contact form page:
* Django admin:
