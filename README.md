![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


# The_Best_Me
An online shop and community for people that what to become the best versions of themselves, through journaling, meditation and financial freedom.
Source code can be found [here](https://github.com/kelllyy101/pp5)
The live project can be viewed [here](https://the-best-me-38fd42c32230.herokuapp.com/)
## Purpose of Project
The aim of this project, built using Django, Bootstrap, and incorporating elements of JQuery, is to empower users on their journey towards self-improvement. The website serves as a platform offering guides and journals designed to facilitate personal growth and development as well as the blog which offers insightful information. By leveraging tools such as journaling and meditation, users can document their progress, ultimately striving to become the best version of themselves.

Additionally, the integration of the Stripe CLI enables users to explore opportunities for financial independence leaving them stress free. Through focus and determination, users can utilise the provided guides to establish alternative income streams, thereby reducing reliance on traditional 9-5 employment. This approach empowers individuals to prioritise personal growth and fulfillment, paving the way for a brighter and more fulfilling future
![responsivenes_screenshot](/media/testing/all-devices-black.png)
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
The design is simple and classic using black and white as seen in the walkthrough project. Keeping the design simple and minimalistic should attract any woman who is looking to become the best version of themselves.

### Fonts 
Simple Monsterrat font is used so there is easy quick reading, focusing on the journals and actual content of the store, making it quicker and easier to become the best version of you.

### Colour
The colours are simple and classic using black and white, so the colourful journals stand out and catch the eye of the viewer.

### Wireframes
![products_display wireframe](/static/)
![products_detail wireframe](/static/)
![display_basket wireframe](/static/)
[Return to top](#Strings_Attached)
# Development Process
## Project planning and documentation in GitHub
GitHub Issues were used to document the development steps undertaken in the project and [User Stories]() were used. Various labels were employed to enable quick identification of issue type including Bugs, User Epics, User Stories and Style. MoSCoW prioritisation was employed using the labels must-have, should-have and could-have. 
To break the project into manageable sprints, GitHub Projects was used to provide a Kanban board onto which the issues were posted, moving them from 'Todo' to 'In Progress' to 'Done' as they 
were completed as seen [here](https://github.com/users/kelllyy101/projects/3)

## Data Model
**Deploying My Database with ElephantSQL**

1. **Sign Up and Create an Instance:**
   - Visit the ElephantSQL website and sign up for an account.
   - Once logged in, create a new database instance. Choose a plan that suits your project requirements.

2. **Connection Details:**
   - After creating the instance, ElephantSQL provides you with connection details such as the hostname, username, password, and database name.
   - These details will be used to configure your Django project to connect to the ElephantSQL database.

3. **Update Django Settings:**
   - In your Django project settings (`settings.py`), update the `DATABASES` configuration with the connection details provided by ElephantSQL.
   - Replace the default database configuration with the PostgreSQL configuration provided by ElephantSQL.

4. **Migrate Your Database:**
   - Once the settings are updated, migrate your Django project to create the necessary database schema.
   - Run `python manage.py makemigrations` followed by `python manage.py migrate` to apply the migrations to the ElephantSQL database.

5. **Test Connection and Deploy:**
   - Ensure that your Django project can successfully connect to the ElephantSQL database by running your project locally.
   - Test database operations such as creating, reading, updating, and deleting records to confirm that the integration is working as expected.

6. **Monitor and Scale:**
   - ElephantSQL provides monitoring tools and scalability options to manage your database efficiently.
   - Monitor database performance, usage, and health using the ElephantSQL dashboard.
   - Scale your database instance as needed to accommodate increasing traffic and data volume.

7. **Backup and Security:**
   - ElephantSQL offers automated backups and security features to safeguard your data.
   - Enable automatic backups to ensure data integrity and implement security measures such as SSL encryption and access controls.

8. **Run Querys:**
    - I ran queries for different data to make sure that they were saved correctly in the database as seen in the below photos as examples.
    ![Blog Posts](/media/testing/Screenshot%20(953).png)
    ![Products](/media/testing/Screenshot%20(954).png)


### Products App
![Entity-relationship diagram for models](image)
### Checkout App
![Entity-relationship diagram for models](image)
- Data validation

### Blog App


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
#### _products app_



#### _checkout app_

#### _blog app_


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
The User Stories of this project are documented in a GitHub Project, corresponding 
to the iterations that comprised the development work of the project. These can be found [here](https://github.com/users/kelllyy101/projects/3).

# Payments Integration
I have integrated Stripe with the aid the the final walk through project with Code-Institute.

## Stripe Webhook Testing
### Stripe Payment Flow
The payment flow handling is direct from the Boutique Ado project. 

---
## Automated Testing
### Testing django views, models and forms.
Tests were created for each of the apps to ensure top functionality which can be found in the following files: 

[bag/tests.py](https://github.com/kelllyy101/pp5/blob/main/bag/tests.py) -
1. **test_admin_url**: This test checks whether accessing the admin URL redirects to the login page. It sends a GET request to the admin index page (`admin:index`) using the `reverse` function to resolve the URL. Then, it asserts that the response status code is 302, indicating redirection.

2. **test_accounts_url**: This test ensures that the login page URL is accessible. It sends a GET request to the URL resolved by the name `account_login` using the `reverse` function. It expects the response status code to be 200, indicating a successful access to the login page.

3. **test_home_url**: This test verifies the accessibility of the home page URL. It sends a GET request to the URL resolved by the name `home` using the `reverse` function. Similar to the previous test, it expects the response status code to be 200, indicating that the home page is accessible.


[best_me/tests.py](https://github.com/kelllyy101/pp5/blob/main/best_me/tests.py) -
1. **test_admin_url**: Checks if the admin URL (`/admin/`) redirects to the login page. It sends a GET request to the admin index page using the reverse URL resolution mechanism, and then asserts that the response status code is 302, indicating redirection to the login page.

2. **test_accounts_url**: Verifies if the accounts login URL (presumably `/accounts/login/`) is accessible. It sends a GET request to the login page using the reverse URL resolution mechanism and asserts that the response status code is 200, indicating the page is accessible.

3. **test_home_url**: Tests the accessibility of the home page URL (`/home/` or similar). Similar to the previous tests, it sends a GET request to the home page using the reverse URL resolution mechanism and asserts that the response status code is 200, ensuring the page is accessible.


[blog/tests.py](https://github.com/kelllyy101/pp5/blob/main/blog/tests.py) -
1. **setUpTestData**: Sets up initial data for the tests. It creates a user (`u1`) and a post with the title "This is a test!" authored by that user.

2. **test_model_content**: Checks if the title of the post created in `setUpTestData` matches the expected value ("This is a test!").

3. **test_url_exists_at_correct_location**: Verifies that the URL "/blog/" exists and returns a status code of 200 (OK).

4. **test_blog_view**: Tests the blog view. It checks if accessing the blog page via its reverse URL returns a status code of 200, ensures that the correct template ("blog.html") is used, and confirms that the post title "This is a test!" is present in the response.

5. **test_blog_post_view**: Checks the blog post detail view. It creates a new post, accesses its detail page via its reverse URL with its primary key (`pk`), verifies that the status code is 200, ensures that the correct template ("blog_post.html") is used, and confirms that the post title "Test Post" is present in the response.

6. **test_add_blog_post_view**: Tests the view for adding a new blog post. It accesses the add blog post page via its reverse URL, checks if the status code is 200, and ensures that the correct template ("add_blog_post.html") is used.


[checkout/tests.py](https://github.com/kelllyy101/pp5/blob/main/checkout/tests.py) -
1. CheckoutPageTests:
   - **test_checkout_page_loads_correctly**: Checks if the checkout page loads correctly. It verifies that the HTTP response status code is 200 (OK) and ensures that the correct template ("checkout/checkout.html") is used.

2. CheckoutProcessTests:
   - **test_successful_checkout_redirects_to_success_page**: Simulates a successful checkout process by sending a POST request to the checkout endpoint. It expects a redirect status code (302), indicating a successful checkout. Additionally, it checks that the user is redirected to the checkout success page.

3. CheckoutSuccessPageTests:
   - **test_checkout_success_page_loads_correctly**: Tests if the checkout success page loads correctly. It constructs a mock order number, retrieves the checkout success page using the order number in the URL, and checks that the HTTP response status code is 200 (OK). It also ensures that the correct template ("checkout/checkout_success.html") is used.


[home/tests.py](https://github.com/kelllyy101/pp5/blob/main/home/tests.py) - 
1. **test_url_exists_at_correct_location**: Checks if the homepage URL ("/") returns a status code of 200 (OK).

2. **test_url_available_by_name**: Tests if the homepage URL is accessible using its name ("home") and returns a status code of 200.

3. **test_template_name_correct**: Ensures that the correct template ("home/index.html") is used when rendering the homepage. Additionally, it verifies that the base template ("base.html") is used.

4. **test_main_heading_present**: Checks if the main heading "Get ready to be the Best You!" is present on the homepage.

5. **test_shop_now_button_present**: Verifies the presence of the "SHOP NOW" button on the homepage.

6. **test_carousel_present**: Ensures that the carousel with the ID "carouselExampleIndicators" is present on the homepage.

7. **test_product_images_present**: Checks if specific product images are present on the homepage. It verifies the presence of three images using their URLs.

8. **test_product_names_present**: Verifies the presence of specific product names ("Journaling" and "Meditation") on the homepage.


[profiles/tests.py](https://github.com/kelllyy101/pp5/blob/main/profiles/tests.py) -
1. **setUp**: This method sets up initial data for the tests. It creates a user with the username 'testuser' and password '12345'. If the user does not already have a UserProfile associated with it, it creates one.

2. **test_profile_view_template**: This test checks if the profile view template is rendered correctly. It logs in as the test user, sends a GET request to the profile view URL (`reverse('profile')`), and asserts that the response status code is 200. Additionally, it ensures that the correct template ('profiles/profile.html') is used.

3. **test_profile_update_form**: This test verifies the functionality of updating a user's profile. It logs in as the test user, sends a POST request to the profile view URL (`reverse('profile')`) with some form data (such as default phone number and country), and assumes that it successfully redirects after form submission (status code 200).

4. **test_profile_view_with_orders**: This test checks if the profile view displays order history correctly. It assumes that orders related to the user profile exist in the database. It logs in as the test user, sends a GET request to the profile view URL, and asserts that the response status code is 200. It also checks if the correct template ('profiles/profile.html') is used.

5. **test_order_history_view**: This test verifies the functionality of the order history view. It assumes that there is an Order model in the application and creates an order to test the order history view. It logs in as the test user, sends a GET request to the order history view URL (`reverse('order_history', args=['12345'])`), and checks if the response status code is 200. It also ensures that the correct template ('checkout/checkout_success.html') is used.


# Bugs
- A number of other bugs and their solution are documented in the issues tracker on GitHub, such as :
    - https://github.com/users/kelllyy101/projects/3
    
## Remaining Bugs
There are (hopefully) no remaining bugs in the project. One thing I would have liked to change is the back to top arrow on medium size screens as the cursor changes because of the GitHub Icon in the footer.


# Libraries and Programs Used
1. [Heroku](https://www.heroku.com/)
    - Heroku was used to deploy the project
2. [Git](https://git-scm.com/)
    - Version control was implemented using Git through the Github terminal.
3. [Github](https://github.com/)
    - Github was used to store the projects after being pushed from Git and its cloud service [Github Pages](https://pages.github.com/) was used to serve the project on the web. GitHub Projects was used to track the User Stories, User Epics, bugs and other issues during the project.
4. [Visual Studio Code](https://code.visualstudio.com/)
    - VS Code was used locally as the main IDE environment, with the JSHint and Flake8 linters installed for JavaScript and Python code validation respectively.
5. [Bootstrap](https://getbootstrap.com/docs/4.0/)
    - Bootrap was extensively used in the layout and design of this project.
6. [AWS](https://aws.amazon.com/)
    - Aws was used to store the downloadable digital products and the images of the products.
7. [ElephantSQL](elephantsql.com)
    - ElephantSQL was the database used to store categories, products, orders, user profiles, blogs, blog reviews and product reviews.

# Deployment
## Setting up an AWS account for static storage.
Setting up an AWS account for static storage involves several steps. Here's a summary of the process I took to store the static files of my project:

1. **Create an AWS Account**: Go to the AWS website and sign up for an account if you don't already have one. You'll need to provide some basic information and a payment method.

2. **Sign in to the AWS Management Console**: Once you have an account, sign in to the AWS Management Console using your credentials.

3. **Navigate to S3 (Simple Storage Service)**: In the AWS Management Console, find the S3 service. You can search for it in the services search bar or locate it under the "Storage" section.

4. **Create a Bucket**: Once in the S3 dashboard, click the "Create bucket" button. Give your bucket a unique name (bucket names must be globally unique across all of AWS) and select the region where you want your bucket to be located.

5. **Configure Bucket Properties**: You can configure various properties for your bucket, such as versioning, logging, and tags. For static website hosting, you'll want to enable static website hosting under the "Properties" tab.

6. **Set Up Static Website Hosting**: Under the "Properties" tab of your bucket, find the "Static website hosting" section. Enable it and specify the index document (e.g., index.html) and error document if needed.

7. **Upload Your Files**: Once your bucket is set up, you can upload your static files (HTML, CSS, JavaScript, images, etc.) using the AWS Management Console, AWS CLI, or an SDK.

8. **Set Permissions**: By default, all objects in your bucket are private. If you want to make them publicly accessible (which you typically do for a static website), you'll need to adjust the bucket policy or the permissions of individual objects.

9. **Testing**: After uploading your files and setting permissions, you can test your static website by accessing the endpoint provided in the static website hosting configuration. It should serve your web content.

10. **DNS Configuration (Optional)**: If you want to use a custom domain for your static website, you'll need to configure DNS settings to point to the S3 endpoint. This involves creating a CNAME record or an Alias record pointing to the S3 endpoint URL.


## Deploying the app on Heroku

## Making a local clone
1. Open a terminal/command prompt on your local machine.
2. Navigate to the folder on your local machine where you would like to clone the project.
3. Enter the command : `git clone 'https://github.com/johnrearden/just-beats.git'`

## Running the app in your local environment
Heroku Deployment:

Heroku is a platform that allows you to deploy and host your applications, including the expense tracker project. Here are the steps I took to deploy the expense tracker on Heroku:

1. Logged in to my Heroku account at https://www.heroku.com/.
2. Installed the Heroku Command Line Interface (CLI) on my system to manage and deploy Heroku apps from the command line.
3. Ensured that my project was in a Git repository and connected Heroku to GitHub successfully by copying and pasting the repository name.
4. Added a requirements.txt file and a Procfile from Code Institute's template to ensure successful deployment of the project. Additionally, removed DEBUG for production.
5. Created a new Heroku app using the Heroku CLI after logging into my account and connecting my Git repository. Also enabled automatic deployment.
6. Before creating the app, added two buildpacks from the Settings tab, ensuring that heroku/python was added first, followed by heroku/nodejs. Additionally, configured production settings by creating: if DEBUG: ALLOWED_HOSTS = [] else: ALLOWED_HOSTS = [''the-best-me-38fd42c32230.herokuapp.com'].
7. Add the Provided Config Vars: Copy the provided config vars (AWS_ACCESS_KEY_ID, AWS_SECRET_KEY_ID, DATABASE_URL, EMAIL_HOST_PASS, EMAIL_HOST_USER, SECRET_KEY, USE_AWS) 
8. Deployed the project to Heroku by pushing the Git repository to Heroku's remote. This setup ensured that the project updates with every git push, as selected in the settings, successfully integrating and deploying the project for use through the Heroku URL.

Database Setup:

For this project, database configuration on Heroku is essential if it relies on a database. After adding the required database add-on, I updated the application settings to use the database URL provided by Heroku. Additionally, I managed sensitive information such as API keys and database credentials using environment variables on Heroku, either through the Heroku dashboard or the Heroku CLI.

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
Bootstrap was used extensively in the project. Code Institute's Boutique walk through project was a big help setting the base of this project and to be able to understand the basics. eCommerce stores such as BooHoo and Dunnes influenced the design. Stack Overflow provided much needed documentation when deploying this project. Official Django Documentation was all thoroughly used throughout. Stripe CLI documentation was followed while integrating it.

# Acknowledgements
I would like to express my gratitude to Code Institute for their exceptional web development curriculum and to my mentor for their invaluable guidance and support throughout this project. Thank you for providing the resources and expertise that have helped me grow as a developer.

[Return to top](#pp5)