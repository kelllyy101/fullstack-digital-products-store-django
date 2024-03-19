![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


# The_Best_Me
An online shop and community for people that what to become the best versions of themselves, through journaling, meditation and financial freedom.
Source code can be found [here](https://github.com/kelllyy101/pp5)
The live project can be viewed [here](https://herokuapp.com)
## Purpose of Project
The aim of the project is to help users on their journey to become the best versions of themselves. The website consists of guides and journals to aid users become the the best version of themselves by documenting their progress. By journaling and meditating, you set yourself up for a better future you, who doesn't need to stick to the norms of working 9-5. With focus and drive, you can use guides to provide a second income source so you have a lot less to worry about, focusing on becoming the best version of you.
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
Regular Users:

Register: Users can create an account by providing necessary details like username, email, and password.
Login: Registered users can log in using their credentials.
View Products: Users can browse through the collection of journals and guides available in the store.
Product Details: Users can view detailed information about each product, including its description, price, and available quantity.
Add to Bag: Users can add desired products to their shopping bag/cart.
View Bag: Users can view the contents of their shopping bag, update quantities, or remove items.
Checkout: Users can proceed to checkout, providing shipping and payment details for the order.
Order History: Users can view their order history, including past purchases and their status.
Blog: Users can access a blog section where they can find articles and guides on personal development and how to utilize the products effectively.

Product Management: Superusers can add new products to the store, edit existing product details such as name, description, price, and quantity, and delete products if necessary.
Order Management: Superusers can view all orders placed in the store, mark orders as processed/shipped, and manage order statuses.
User Management: Superusers can view user accounts, edit user details, and even deactivate user accounts if required.
Blog Management: Superusers can create, edit, and delete blog posts. They can also manage comments on blog posts, including approving, editing, or deleting them.

Email Notifications: Superusers can configure and send email notifications to users for order confirmations, shipping updates, and promotional campaigns.

### Future Features
Analytics: Superusers may have access to analytics tools to track sales, user engagement, and other metrics to optimize the store's performance.

Site Configuration: Superusers can manage site settings such as shipping options, payment methods, and other configurations.

Wishlist: Allow users to create and manage a wishlist of products they're interested in purchasing in the future. This can improve user engagement and retention.

Search Functionality: Implement a robust search feature that allows users to easily find products by name, category, or keyword. You can use filters and sorting options to enhance the search experience further.

Recommendation System: Integrate a recommendation engine that suggests relevant products to users based on their browsing history, purchase behavior, and preferences. This can personalize the user experience and increase sales.

Advanced User Profiles: Enhance user profiles with additional features such as profile pictures, bio sections, and social media integration. This can foster a sense of community among users and improve engagement.

Discounts and Coupons: Implement a system for offering discounts, promotions, and coupon codes to users. This can help boost sales and incentivize repeat purchases.

Multiple Payment Options: Expand the available payment options to include popular methods such as PayPal, Apple Pay, Google Pay, and cryptocurrency. Offering flexibility in payment methods can improve conversion rates.

Mobile App Integration: Develop a mobile app version of your store to reach users on mobile devices. Ensure seamless synchronization between the web and mobile platforms for a consistent user experience.

Localization and Internationalization: Support multiple languages and currencies to cater to a global audience. This can expand your customer base and increase sales from different regions.


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
Bootstrap was used extensively in the project. Code Institute's To-Do list walk through project was a big help setting the base of this project and to be able to understand the basics. Habit Tracker websites such as Habify and MyHabitTracker influenced the design. Bootstrap documentation was thoroughly used throughout the design. Stack Overflow provided much needed documentation when deploying this project. Official Django Documentation was all thoroughly used throughout.

# Acknowledgements
I would like to express my gratitude to Code Institute for their exceptional web development curriculum and to my mentor for their invaluable guidance and support throughout this project. Thank you for providing the resources and expertise that have helped me grow as a developer.

[Return to top](#pp5)