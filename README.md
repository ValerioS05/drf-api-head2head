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
  - **Filtering, Search, and Ordering**
  -  Search: You can search categories by name or description using query parameters. For example:
     -  GET /categories/?search=tech
     -  Ordering: Categories can be ordered by name or description.
     -  GET /categories/?ordering=name
     -  Filtering: You can filter categories based on specific fields such as name or description.
     -  GET /categories/?name=tech
  - **Notes**
    - The category model at the start was designed to display a category on its own page as per the creation ,modification and deletion. During the development of the client side this part was left out due to overwelm on the user. The user should only be able to see the category of a product but there is not need of a literal explanation or any way to modify the category and especially delete it. I opted to leave the full code as it was from the start for future features over this part of the API.
#### Products
The /products/ endpoint allows the user to manage products. Each product belongs to a category and has many attributes like price, location, keywords etc..
  - **GET /products/**
    - Fetches a list of all products.
    - Accessible to all authenticated users or read-only for non-authenticated users.
    - Returns a list of products with details like id, name, category, price, location, average_rating, and other information.
      |||
      |--|--|
      |![Products GET](/images/readme_img/products.png)|The products are returned from the get in this format. Every product is defined by its primary key followed but the rest of the properties. When the database is populated by many product we have them paginated as you can see on the top side of the image.|
  - **POST /products/**
    - Creates a new product.
    - Accessible to authenticated users only.(To note that in the Front end the creation of the product is allowed to staff users only.)
    - Requires name, category, description, price, location, keywords, and features. The other fields will set depending on the user and the interacions on the   product for the average rating and the vote_id.
      |||
      |--|--|
      |![Products POST](/images/readme_img/prodpost.png)| The post admits this props to be created.(The create_at is automatically set upon creation).|
  - **GET /products/{id}/**
    - Fetches the details of a specific product by id.
    - Accessible to all authenticated users.
    - Returns detailed information about a signle product.
      |||
      |--|--|
      |![Products GET by ID](/images/readme_img/getprod.png)|In here we get a signle product detailed to note that average rating and vote id are null when no data has been submitted for those two properties.|
  - **PUT /products/{id}/**
    - Updates the details of a specific product by id.
    - Accessible only by the owner of the product or staff users.
    - You can update the product’s name, category, description, price, location, keywords, features and image.
      |||
      |--|--|
      |![Products PUT](/images/readme_img/prodput.png)|In this image seen from the admin panel , you can see how the product is already populated by its actual details, we can change any of these details at our delight.| 
  - **DELETE /products/{id}/**
    - Deletes a specific product by id.
    - Accessible only by the owner of the product or staff users.
    - Returns a success message
      |||
      |--|--|
      |![Products PUT](/images/readme_img/prodel.png)|In here is the response that we get once a product is deleted and no data is anymore available.|