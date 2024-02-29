![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for Codeanywhere. If you are using Gitpod then you need [this template](https://github.com/Code-Institute-Org/gitpod-full-template) instead.  We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Codeanywhere and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **August 30th, 2023**

## Codeanywhere Reminders

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere, in the terminal, type:

`python3 -m http.server`

A button should appear to click: _Open Preview_ or _Open Browser_.

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere with no-cache, you can use this alias for `python3 -m http.server`.

`http_server`

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A button should appear to click: _Open Preview_ or _Open Browser_.

In Codeanywhere you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In Codeanywhere, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

---

Happy coding!


# Strings_Attached
An online shop and community for people that what to become the best versions of themselves, through journaling, meditation and financial freedom.
Source code can be found [here](https://github.com/kelllyy101/pp5)
The live project can be viewed [here](https://herokuapp.com)
## Purpose of Project
The aim of the project is to help users on their journey to become the best versions of themselves. The website consists of a shop where instruments and accessories can be purchased, and subscriptions to music lesson videos 
can be signed up to. There is also a community on the site, within which users can post videos, sound
clips and comment on their progess.
![responsivenes_screenshot]()
---
## Links to content
[**Features**](#Features)
[**User Experience**](#User-Experience)
- [Design](#design)
    - [Fonts](#fonts)
    - [Colour](#colour)
    - [Wireframes](#wireframes)
[**Development Process**](#Development-Process)
- [Project Planning](#project-planning-and-documentation-in-github)
- [Inline JavaScript](#inline-javascript-and-event-handlers)
- [Data Model](#data-model)
[**Testing**](#Testing)
- [Manual Testing](#manual-testing)
    - [Feature Testing](#feature-testing)
    - [Responsiveness](#responsiveness)
    - [Browser Compatibility](#browser-compatibility)
    - [Lighthouse](#lighthouse)
    - [Code Validation](#code-validation)
        - [Python](#python-code)
        - [JavaScript](#javascript-code)
        - [HTML](#html-validation)
        - [CSS](#css-validation)
    - [User Stories](#user-stories)
- [Automated Testing](#automated-testing)
    - [Django testing](#testing-django-views-models-and-forms)
    - 
[**Bugs**](#Bugs)
[**Libraries and Programs Used**](#libraries-and-programs-used)
[**Deployment**](#Deployment)
- [Deploying the app on Heroku](#deploying-the-app-on-heroku)
- [Making a local clone](#making-a-local-clone)
- [Running the app in your local environment](#running-the-app-in-your-local-environment)
[**Credits**](#Credits)
[**Acknowledgements**](#acknowledgements)
---
## Features
### Future Features
[Return to top](#Strings_Attached)
# User Experience
## Design
### Fonts 
### Colour
### Wireframes
![products_display wireframe](/static/)
![products_detail wireframe](/static/)
![display_basket wireframe](/static/)
[Return to top](#Strings_Attached)
# Development Process
## Project planning and documentation in GitHub
GitHub Issues were used to document the development steps undertaken in the project. Two issue templates, 
for [User Epics]() and [User Stories]() were used. Various labels were employed to enable quick identification of issue type including Bugs, User Epics, User Stories and Style. MoSCoW prioritisation was employed using the labels must-have, should-have and could-have. 
To break the project into manageable sprints, GitHub Projects was used to provide a Kanban board
onto which the issues were posted, moving them from 'Todo' to 'In Progress' to 'Done' as they 
were completed in turn. The iterations are documented here - [Iteration 1]
The User Epics and their related User Stories are as follows:
- Epic : [).
    - Story : [)
    - Story : [)
## Data Model
### Products App
![Entity-relationship diagram for models](image)
### Checkout App
![Entity-relationship diagram for models](image)
- Data validation
# Payments Integration
I have integrated Stripe with the aid the the final walk through project with Code-Institute
# Testing
- Manual testing
- Automated testing
- In-app testing
- User story testing
- Validator testing
---
## Manual Testing
### Feature Testing
The manual testing of features is organised by app below.
#### _Basket App_



#### _products app_



### Responsiveness
### Browser Compatibility
| Feature | Chrome | Firefox | Safari(mobile) |
--- | --- | --- | --- | 
### Lighthouse
![loop_rating_page](media/docs/create_review_lighthouse_report.png)
### Code Validation
#### Python code : 
- All Python code is validated by the external CodeInstitute validator @ https://pep8ci.herokuapp.com/. 
#### JavaScript code :
- All JavaScript code in the project was validated during development with the JSHint plugin for VSCode.
#### HTML Validation :
- All HTML files in the project were validated using the W3C Narkup Validation Service.
https://validator.w3.org/
#### CSS Validation :
- No errors were found when the single CSS file style.css was passed through the W3C Validation Service.
https://jigsaw.w3.org/css-validator/
### User Stories
The User Epics and Stories in this project are documented in three GitHub Projects, corresponding 
to the iterations that comprised the development work of the project. These can be found here :
- [Iteration 1]()
Alternitively, the Epics and Stories are individually linked here :
- [Epics and Stories](#development-process)
---
## Stripe Webhook Testing
### Stripe Payment Flow
The payment flow handling is direct from the Boutique Ado project. 

---
## Automated Testing
### Testing django views, models and forms.
[Return to top](#Strings_attached)
# Bugs
- A number of other bugs and their solution are documented in the issues tracker on GitHub, such as :
    - https://github.com/
    
## Remaining Bugs
There are (hopefully) no remaining bugs in the project.
[Return to top](#Strings_attached)
# Libraries and Programs Used
1. [Heroku](https://www.heroku.com/)
    - Heroku was used to deploy the project
2. [Git](https://git-scm.com/)
    - Version control was implemented using Git through the Github terminal.
3. [Github](https://github.com/)
    - Github was used to store the projects after being pushed from Git and its cloud service [Github Pages](https://pages.github.com/) was used to serve the project on the web. GitHub Projects was used to track the User Stories, User Epics, bugs and other issues during the project.
4. [Visual Studio Code](https://code.visualstudio.com/)
    - VS Code was used locally as the main IDE environment, with the JSHint and Flake8 linters installed for JavaScript and Python code validation respectively.

# Deployment
## Setting up a cloudinary account for static storage.
## Deploying the app on Heroku

## Making a local clone
1. Open a terminal/command prompt on your local machine.
2. Navigate to the folder on your local machine where you would like to clone the project.
3. Enter the command : `git clone 'https://github.com/johnrearden/just-beats.git'`
## Running the app in your local environment

## Testing the app locally


# Credits


# Acknowledgements

[Return to top](#pp5)