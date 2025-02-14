# DRF-API-HEAD2HEAD Readme
This is the readme for the **API Head2Head** react application.
## Goal of the API
- This API has been built following the user stories created for the front end. I needed a good API that would let me handle the manipulation of datas for a comparison site. Firstly the though was about how the Comparison would be created
  - For a comparison I needed Products. So the Product model was planned.
  - During the planning of the Product I opted to create the categories as a separate model, it's more efficient and easier to handle.
  - The categories were developed to group/ wrap the products.
  - Now we could be set for a comparison, having products and categories. But, for a comparison we need a user that makes the actual comparison.
  - So the Profiles were created to be connected to the User model. In this case the product and the comparison would be owned by an actual person.
  - We could be set like this, but in a comparison site only displaying two products would be the minimum, so what I implemented was votes.
  - The votes are connected to users and voting on a product is a good UX, we all know how it feels to leave a bad review on something (LOL).
  - Oh review? Leaving only a Vote is not enough, let me share my thought on this product,and so the comments were implemented.
  - Now the user stories for a common user are fulfilled. We have an API that let us manipulate products, comment and vote on them, group them by categories and finally compare them! (I also added favourites for more personalization but it was not implemented in the front end side.)
  - The goal for this project is achieved.
## Readme Map:
- [DRF-API-HEAD2HEAD Readme](#drf-api-head2head-readme)
  - [Goal of the API](#goal-of-the-api)
  - [Readme Map:](#readme-map)
  - [Separate sections](#separate-sections)
  - [Design of the database](#design-of-the-database)
    - [Overview](#overview)
    - [Features](#features)
    - [Plan](#plan)
    - [Models](#models)
    - [Relationships Between Models:](#relationships-between-models)
      - [How They Work Together:](#how-they-work-together)
      - [CRUD](#crud)
  - [Deployment](#deployment)
  - [Dependencies (Requirements.txt) and technologies](#dependencies-requirementstxt-and-technologies)
  - [Languages](#languages)
  - [Bugs and fixes](#bugs-and-fixes)
  - [Credits](#credits)

## Separate sections
- Sections for the readme were made to help on the reading.  
[Endpoint](/endpoints.md) Section.  
[Testing](/testing.md) Section.  

## Design of the database

### Overview
- **drf-api-head2head** is a backend API build using DRF (Django Rest Framework). 
  This API serves request from the front end, its necessities ,logic interaction and data processing required.
- The API built for a comparison site, provides a range of data for:
  - Categories:
    - Handle different categories where products will be included.
  - Comments:
    - Manage user comments on products.
  - Comparison
    - Manage the logic and data for product comparisons.
  - Products:
    - Manages product datas and its interactions with the overall.
  - Profiles:
    - Manage user profiles directly connected to the User model.
### Features
  - Filtering, sorting and searching:
    - The models are built to allow the user to be able to perform this actions giving a better experience when the database gets overpopulated.
  - Authentication:
    - JWT has been implemented to give the user security and session based authentication.

### Plan
|||
|--|--|
|![Models Diagram](/images/readme_img/diagram.png)|This is the initial diagram used to plan out the API. As we can see we have 5 different models. First model is the categories, created first to wrap around the main model that is the product. The product model is the center of those models directly connected to all the other models via PK. The third model planned was the profile that takes count to the default user model offered by the framework. The profile is connected to the Vote,Comment and Product model.|The vote and the Comment model are conneted to the Product as 1 to many where a product can have multiple votes and comments.Last but not least is the comparison model, the comparison models is connected to product as a many to many where a product can have multiple comparison and viceversa.
  - **To note** is that this diagram was made before the development of the API and as so , some of the model may have been improved for data integrity / efficiency.
### Models

1. Category Model
   - The Category model represents a category under which products can be wrapped. It includes:

   - Fields:

   - name: A CharField for the category name (unique).
   - description: A TextField for providing a description of the category.
   - image: A CloudinaryField used for storing an image related to the category. It defaults to 'default_h2h' if no image is provided.
   - Meta class:

   - Orders categories by name.
   - Method:

   - The __str__() method returns the category name.
2. Comment Model
   - The Comment model represents a comment made by a user on a product. It includes:

   - Fields:

   - product: A ForeignKey to the Product model.
   - owner: A ForeignKey to the User model (the user who made the comment).
   - content: A TextField containing the comment content.
   - created_at: A DateTimeField to track when the comment was created.
   - Meta class:

   - Orders comments by creation (latest first).
   - Method:

   - The __str__() method returns a string representation of the comment, including the user and product associated with the comment.
3. Product Model
   - The Product model represents the details of a product. It includes:

   - Fields:

   - name: A CharField representing the product name.
   - category: A ForeignKey to the Category model.
   - description: A TextField for describing the product.
   - price: A DecimalField for storing the price, with a minimum value of 0.01.
   - location: A CharField indicating where the product is located.
   - image: A CloudinaryField to store an image of the product.
   - keywords: A TextField to store keywords related to the product.
   - features: A TextField that contains features of the product.
   - created_at: A DateField representing when the product was created.
   - owner: A ForeignKey to the User model(user who created the product).
   - Meta class:

   - Orders products by name, location, category (in descending order), and price (in descending order).
   - Methods:

   - The __str__() method returns a string representation of the product, including the product name, owner, and price.
   - The get_average_rating() method calculates the average rating for the product based on Vote objects.
4. Profile Model
   - The Profile model is a user profile that stores additional information about a user. It includes:

   - Fields:

   - owner: A OneToOneField to the User model, creating a one to one relationship between the user and their profile.
   - bio: A TextField for the user bio.
   - location: A CharField for the user location.
   - profile_picture: A CloudinaryField for the user profile image.
   - favourites: A ManyToManyField to the Product model, representing the products that the user has favourited.
   - Meta class:

   - Orders profiles by location in descending order.
   - Methods:

   - The __str__() method returns a string representation of the profile.
   - The new_user() function is a signal that automatically creates a Profile when a new User is created.
5. Vote Model
   - The Vote model represents a vote (or rating) given by a user to a product. It includes:

   - Fields:

   - owner: A ForeignKey to the User model, the user who gave the vote.
   - product: A ForeignKey to the Product model, the product that received the vote.
   - created_at: A DateTimeField to track when the vote was created.
   - vote: An IntegerField for the vote value, limited to be between 1 and 5.
   - Meta class:

   - Orders votes first by the owner, then by product, and by the creation time (latest first).
   - The unique_together constraint ensures that a user can only vote once on a product.
   - Method:

   - The __str__() method returns a string representation of the vote.
6. Comparison Model
  - The Comparison model represents a comparison between multiple products. It includes:

  - Fields:

  - products: A ManyToManyField linking to the Product model. This field indicates the products that are being compared.
  - owner: A ForeignKey relationship to the User model, the user who owns the comparison.
  - created_at: A DateTimeField that tracks when the comparison was created.
  - Meta class:

  - Orders comparisons by creation time (latest first).
  - Method:

  - The "__str__()" method returns a string representation of the comparison.

### Relationships Between Models:
  - Comparison to Products: The Comparison model has a ManyToManyField to Product, which means a comparison can have multiple products.  
    The Comparison model also has a ForeignKey to the User model, which means each comparison belongs to a specific user.

  - Comment to Product: The Comment model has a ForeignKey to the Product model, connecting comments to specific products.  
    It also has a ForeignKey to the User model, so each comment is connected to a user.

  - Product to Category: The Product model has a ForeignKey to the Category model, so each product is assigned to a category.

  - Profile to User: The Profile model has a OneToOneField to the User model, ensuring that each user has a corresponding profile with additional infos.  
    The Profile is created automatically with the help of a signal that get the user instance when created.

  - Vote to Product and User: The Vote model links a user to a product they have voted. Each vote is associated with a Product and a User.

  - Profile to Product (Favourites): The Profile model includes a ManyToManyField to the Product model, which means that users can set multiple products as favourites.  
    This allows users to access their favourite products. **To note** is that the favourite is implemented but is not used in the frontend side of the app. It's only for demostration porpouses.

#### How They Work Together:
- Users can create products, comment on products, vote on products, and compare products.  
  Products are organized into categories, can be rated, and are associated with comments and votes.  
  Profiles allow users to maintain additional information, such as their bio, location, and favourite products.  
  Comparisons allow users to compare products side by side and are associated with a user.  
  This system allows for a comprehensive product evaluation platform with features like product reviews, ratings, comparisons, and personalized user profiles.  



  #### CRUD
  - Create:
    - All functionalities are available to create any of the objects following the proper restrictions.
  - Read:
    - All functionalities are available to read any of the object following proper restrictions.
  - Update:
    - All functionalities are available to update any of the objects following proper restrictions.
  - Delete:
    - All functionalites are available to delete any of the objects. A different approach was taken for the categories.
      - The categories follow a on delete.PROTECT in case a category is being deleted when containing products and in cascade the products contains votes and comments. This prevent corruption of data and mainly safeguarding the hard work put on adding all the products.  
## Deployment
- This API is hosted in Heroku and it uses a Postgres DB. The api is also connected to Cloudinary.
- Before starting the deployment make sure you have created account for your Database and Cloudinary as for this project.
  - **How to deploy on Heroku**
    - Login on  Heroku and select Create New App
    - Choose a name for the App that is consistent with your repository/ies.
    - Select region based on where is you location (Europe for Head2Head)
    - Once you did these two steps click on Create App
    - Direct yourself to Settings in the menu.
    - Scroll down to reveal config vars
    - Once open enter these variables (key : value)
    - CLOUDINARY_URL: your cloudinary URL
      - To get this url you need to login in your cloudinary copy the url that you found in **API enviroment variable**
    - DATABASE_URL: your database url (Postgres in this case)
      - This url was provided by CodeInstitute form and the url was receive via confirmation mail.
    - SECRET_KEY: the secret key choose by you
    - ALLOWED_HOST: the url of your Heroku application
    - CLIENT_ORIGIN: the complete URL of your Heroku app
    - CLIENT_ORIGIN_DEV: the URL of your development (ex: http:localhost:3000)
    - Once finished with this select Deploy in the menu
    - Select GitHub from the options and Connect to GitHub selecting the repository of your app
    - Find the Manual Deploy section and select Deploy Branch (Make sure is Main).
    - Once Deployed you can eaither click on View or Open App to see your deployed App.
    - Well done!
    - (Note that you can also choose Automatic deploy to deploy your app automatically after each time you push code to your repo!!)
  
## Dependencies (Requirements.txt) and technologies
- **asgiref=3.8.1**
  - A Python package required for Django's support of asynchronous views and middleware.
    - [Asgi](https://asgi.readthedocs.io/en/latest/)
- **cloudinary==1.41.0**
  - Cloudinary provides cloud-based media management used to integrate Cloudinary with Django.
    - [Cloudinary](https://cloudinary.com/documentation)
- **dj-database-url==0.5.0**
  - A utility that helps configure Django database settings from a URL. Used in production environment (Heroku) to configure database connection via URL.
    - [dj-database](https://github.com/jazzband/dj-database-url)
- **dj-rest-auth==2.1.9**
  - A Django package used for handling authentication in Django REST Framework. It simplifies the implementation of login, registration, and token authentication.
    - [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/)
- **Django==5.1.4**
  - The framework for Python used to build this application.
    - [Django](https://docs.djangoproject.com/en/5.1/)
- **django-allauth==0.54.0**
  - A Django package for handling authentication.
    - [Allauth](https://django-allauth.readthedocs.io/en/latest/)
- **django-cloudinary-storage==0.3.0**
  - A Django storage backend for Cloudinary. This package simplifies the integration of Cloudinary storage with Django applications.
    - [Cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/)
- **django-cors-headers==4.6.0**
  - A Django app for handling Cross Origin Resource Sharing (CORS). It allows your backend to specify which front end domains are permitted to interact with the api, preventing security issues when making requests from different domains.
    - [Cors-headers](https://pypi.org/project/django-cors-headers/)
- **django-filter==24.3**
  - A package for adding filtering capabilities to Django REST Framework views.
    - [Django-filter](https://django-filter.readthedocs.io/en/stable/guide/usage.html)
- **djangorestframework==3.15.2**
  - A toolkit for building Web APIs in Django. Provides tools for serialization, views, authentication, and more.
    - [DRF](https://www.django-rest-framework.org/)
- **djangorestframework_simplejwt==5.4.0**
  - A Django REST Framework extension for handling JWT (Web Token) authentication.
    - [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- **gunicorn==23.0.0**
  - Gunicorn is used to serve Django applications in production environments. It's a server that interacts with Django’s WSGI interface.
    - [Gunicorn](https://docs.gunicorn.org/en/stable/)
- **oauthlib==3.2.2**
  - It's often used with requests-oauthlib to facilitate OAuth integration in Python applications.
    - [OAuthlib](https://readthedocs.org/projects/oauthlib/downloads/pdf/latest/)
- **pillow==11.0.0**
  - A image processing library for Python. Pillow is used to handle image upload.
    - [Pillow](https://pillow.readthedocs.io/en/stable/releasenotes/11.0.0.html)
- **psycopg2==2.9.10**
  - A PostgreSQL adapter for Python. It allows your Django application to connect to and interact with a PostgreSQL database.
    - [Psycopg2](https://www.psycopg.org/docs/install.html)
- **PyJWT==2.10.1**
  - A Python library used to work with Web Tokens (JWT). PyJWT is used for encoding and decoding JWTs,used in conjunction with Django simplejwt.
    - [PyJWT](https://readthedocs.org/projects/pyjwt/)
- **python3-openid==3.2.0**
  - A library that support for python 3. Used for integrations with services like Google, Facebook, etc.(Note that in this app is not used even if setup.)
    - [Openid](https://pypi.org/project/python3-openid/)
- **requests-oauthlib==2.0.0**
  - A library that adds OAuth support to the requests HTTP library. 
    - [Requests OAuthlib](https://requests-oauthlib.readthedocs.io/en/latest/)
- **sqlparse==0.5.3**
  - sqlparse is a non-validating SQL parser for Python.
    - [Sqlparse](https://sqlparse.readthedocs.io/en/stable/)
- **whitenoise==6.8.2**
  - A package that allows your Django application to serve static files.
    - [Whitenoise](https://whitenoise.readthedocs.io/en/latest/index.html)
- **Cloudinary**
  - Used to handle the image database
    - [Link to cloudinary](https://cloudinary.com/)
- **PostgreSQL**
  - Was used for the database. 
    - [Link to PostrgreSQL](https://www.postgresql.org/)
- These dependecies are taken from the requirements.txt (A reminder that once the dependencies or any toolking , helper etc.. are installed you need to follow the installation with the command pip freeze > requirements.txt)
- **React extention for the Browser**
  - It could be a simple extentions for the browser but the use of this extention helped the development of this project very much.
 
## Languages
  - Python
    - [Python Doc](https://www.python.org/doc/)

## Bugs and fixes
- One of the most problematic bugs was the implementation of the authorization. When trying to access the Production site from Heroku the authorization was never given.
  - Solution: The issue has been fixed by changing the setup in the main folder and the env.py variables matching the actual config vars in heroku.
- Issue when trying to give image size restriction with cloudinary.
  -  The issue has been solved by Implementing the restriction in the Front End, leaving the standard restriction by cloudinary in the backend.
- Another problem arised when I moved from GitPod to VSCode.
  -  The problem was again with authorization and I solved the issue changing again the Heroku config vars.
- Mainly all the bugs and issues encoutered were about small fixes like missing commas or small typos. Even if small going through all that code was quite a  challenge.
  - To help myself to identify the problems I found very helpfull the use of DevTools in Chrome and the default Debug set to True during development.
 
|||
|--|--|
|![Fix](/images/readme_img/fix.png)|In here I was not receiving the right message from my comment. Even if not a large issue it took me a bit to spot.|



## Credits
- The Repository was generated using the Code-Institute-Org/ci-full-template
  - [Template](https://github.com/Code-Institute-Org/ci-full-template)
    - Open the link click on use this template.
    - Select Create New Repository
    - Choose a great name
    - Select public or private, your choice.
    - Click on Create Repository.
- Default image was made with Canva (https://www.canva.com/)
- Diagram was made with LucidArt (https://lucid.app/)
- Some of the code written here followed the moments walkthrough for example the User and Profile chain.
- The set up for authorizations and tokens is fully taken from Moments.
- Also thanks for the CI Tutoring team and Mentor for helping when some issues arised and for the Feedbacks provided.