# Head2Head API Readme
This is the readme for the **Head2Head** react appliction.


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

### API EndPoints
#### Categories
The /categories/ endpoint allows to manage categories for the products. Categories helps organize products into specific groups.
  - **GET**
    - Fetches the list of all categories
    
    - Returns a list of categories and its details:
      |||
      |--|--|
      |![Categories JSON](/images/readme_img/cateogories.png)|In here we can see the categories returned from the get. We got: id: Identified for the actual category. Description: Description of a category. Image: the actual path to the image.|
  - **GET /categories/{id}/**
    - Fetches the datails of a specific category by ID.
      |||
      |--|--|
      |![Categories GET by ID](/images/readme_img/categoriesid.png)|In here the response is a single category and the details inserted from the POST or PUT.|
  - **POST**
    - Creates a new category.
    - The creation of a category is accessible only in the API due to   the high risk of deleting a huge amount of data.
    - Request Body: You need to provide the name , description for the new category  and the image.
    - The ID is set automatically on creation.
      |||
      |--|--|
      |![Categories POST](/images/readme_img/postcategory.png)|This is the view from the admin panel with a simple form Name,Description and image input.|
  - **PUT /categories/{id}/**
    - Changes a category.
    - As the POST the creation of a category is allowed only in the API admin panel.
    - Request body:(First we need to select the category that we want to change) You need to provide the name , description for the selected category and the image. To have a better view of modified categories you can have a look at the history of it.
      |||
      |--|--|
      |![Categories PUT](/images/readme_img/changecat.png)|As you can see we have already the existing details in the form.|
  - **DELETE /categories/{id}/**
    - Deletes a category
      - To note that when a category can be deleted only when no products are associated with it to prevent loss of data and data integrity. If the deleting a category fails the reason is only the one just explained. (Later explained in the product modes.)
      - The deletion is very simple, select the category that you want to delete and confirm. When succesfully deleted you will have a confirmation feedback. 
       |||
        |--|--|
        |![Categories Delete](/images/readme_img/deletecat.png)|This is the message after a succesfful delete action.|
  -**Filtering, Search, and Ordering**
  -  Search: You can search categories by name or description using query parameters. For example:
     -  GET /categories/?search=tech
     -  Ordering: Categories can be ordered by name or description.
     -  GET /categories/?ordering=name
     -  Filtering: You can filter categories based on specific fields such as name or description.
     -  GET /categories/?name=tech
