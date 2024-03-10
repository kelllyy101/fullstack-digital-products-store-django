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
[**eCommerce Business Model**](#eCommerce-business-model)
[**Credits**](#Credits)
[**Acknowledgements**](#acknowledgements)
---
## Features
### Future Features
[Return to top](#The_Best_Me)
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


# eCommerce Business Model
1. Introduction
I believe that achieving personal growth and fulfillment requires a balanced approach that addresses both physical and mental aspects of wellness. My mission at is to empower individuals to lead healthier, more fulfilling lives by providing access to high-quality products and resources that support their physical and mental well-being.
I envision a world where everyone has the tools and support they need to prioritize their health and happiness. Through our ecommerce platform, we aim to create a community of individuals committed to self-improvement and mutual support. We deeply care about the well-being of our customers and strive to create a supportive and empathetic community. We are committed to offering only the highest quality products that promote physical and mental wellness.We believe in empowering individuals to take control of their health and happiness through education, resources, and support.

2. Business Model Canvas
a. We offer a curated selection of products designed to support physical and mental well-being, including:
- Journals for self-reflection, goal-setting, and gratitude practice.
- Meditation guides and tools to promote mindfulness and stress relief.
- Financial freedom resources to empower individuals to take control of their financial health.
- Wellness products such as essential oils, meditation cushions, and relaxation aids.

b. Customer Focus:
We understand that everyone's journey to well-being is unique, which is why we prioritize personalized customer experiences. Our team is dedicated to providing support and guidance to help our customers find the products and resources that best suit their needs.

c. Community Engagement:
Beyond selling products, we are committed to fostering a sense of community and connection among our customers. Through our blog, social media channels, and online forums, we provide valuable content, resources, and opportunities for interaction and support. 

3. Product Catalog
   - Detailed overview of the products you offer, including:
     - Journals: Types, designs, sizes for yearly and weekly and all are downloadable and can be used again.
     - Meditation Guides and Financial Freedom Guides: Cannot be resold but can be downloaded. Each guide has a section for your notes, thought, goals and improvements.

4. Target Audience
   - Identify and describe your target audience segments, including:
     - Individuals interested in personal growth and self-improvement.
     - Meditation enthusiasts seeking guidance and resources.
     - Individuals striving for financial independence and wealth management.
     - Wellness and mindfulness practitioners.
     - People trying to lose weight and improve their fitness and overall health.
  
5. Marketing and Sales Strategy
   - Outline your marketing and sales strategy, covering:
     - Online Marketing: SEO, content marketing, social media, email marketing - MailChimp newletters has been configured in the footer and appears on every page. Meta tags have been added to the base template for SEO purposes and a Facebook account has also been created for social media reach.
     - Offline Marketing: Events, partnerships, collaborations, (future events).
     - Sales Channels: Website sales, third-party platforms (Amazon, eBay), retail partnerships, (future events and possibilities).
  
6. Website and User Experience
   - Describe your ecommerce website and user experience, including:
     - Website Design: Layout, navigation, aesthetics are all simple and effective, a nice rich shade of maroon was used.
     - Product Pages: Descriptions, images, videos, reviews, etc.
     - Checkout Process: Cart management, payment gateways, security measures, etc.
     - Customer Support: Contact options- via email, FAQs, return policies, etc.

7. Fulfillment and Logistics
   - Explain your fulfillment and logistics strategy, covering:
     - Inventory Management: Stock levels, replenishment, tracking, etc.
     - Order Processing: Order placement, processing times, order status updates, (if products were ever printed).
     - Shipping: Shipping carriers, shipping options, shipping costs, delivery times, (if products were ever printed).
     - Returns and Refunds: Return policies, return process, refunds, (if products were ever printed), refunds are not allowed for digital downloads.

8. Customer Support and Engagement
   - Detail your customer support and engagement approach, including:
     - Customer Service: Contact methods, response times, issue resolution, etc.
     - Community Building: Blog posts and comment sections, social media engagement on Facebook, user-generated content, etc.
     - Loyalty Programs: Rewards, discounts, referrals, etc.
  
9. Performance Metrics and KPIs that could be implemented in the future
   - Identify and track key performance metrics and KPIs, such as:
     - Sales Revenue
     - Conversion Rate
     - Customer Acquisition Cost (CAC)
     - Customer Lifetime Value (CLV)
     - Website Traffic
     - Average Order Value (AOV)
     - Customer Satisfaction (CSAT) Score
  
10. Future Plans and Growth Strategies
   - Discuss your future plans and growth strategies, including:
     - Expansion: New product lines and guides, new markets, international expansion, etc.
     - Innovation: Product innovations, technological advancements, etc.
     - Partnerships: Collaborations with influencers, brands, organisations, etc.
     - Scalability: Infrastructure improvements, automation, etc.

11. Conclusion
   In conclusion, The Best Me is positioned as a premier destination for individuals seeking personal growth, holistic well-being, and financial empowerment. Through our meticulously curated collection of journals, meditation guides, financial freedom resources, and related products, we aim to empower our customers to unlock their full potential and lead fulfilling lives. Throughout this ecommerce model documentation, I have outlined a comprehensive plan that encompasses every aspect of our business operations. From our business model canvas to our marketing and sales strategy, website and user experience, fulfillment and logistics, customer support and engagement, and future growth strategies, I have carefully crafted a roadmap for success. I am committed to understanding and serving our target audience effectively, providing them with valuable resources and exceptional customer experiences. Our dedication to excellence extends to every aspect of our operations, from product selection and website design to order fulfillment and customer support. .

# Credits


# Acknowledgements

[Return to top](#pp5)