# API EndPoints
## EndPoint Map

- [API EndPoints](#api-endpoints)
  - [EndPoint Map](#endpoint-map)
    - [Categories](#categories)
    - [Products](#products)
    - [Profiles](#profiles)
    - [Comments](#comments)
    - [Votes](#votes)
    - [Comparisons](#comparisons)
    - [Serializers and Views](#serializers-and-views)
- [Back To Main Page](#back-to-main-page)
- [Go to Testing](#go-to-testing)

### Categories
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
### Products
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

### Profiles
The /profiles/ endpoint allows users to manage their profiles. Each profile is linked to a user and includes bio, location, and profile picture. Users can also mark products as favourites.
The profile gets created automatically anytime a User is added to the database. To note is that when a user is created from the API the details of the profile are not fully set, and it will contain the profile_picture (default if not selected), the owner (User username), and the id.  
To learn more about the User model you can follow this link --> [Django doc for the User model.](https://docs.djangoproject.com/en/5.1/ref/contrib/auth/)
  - **GET /profiles/**
    - Fetches all profiles.
    - Accessible to all authenticated users or read only for non authenticated users.
    - Returns a list of profiles with id, owner, bio, profile_picture, location, and favourites.
      |||
      |--|--|
      |![Profiles GET](/images/readme_img/profget.png)|In here we see the returned profiles. We have all the properties returned from the profile model with the addition of the is_staff that is used to give authorization to certain users to perform a series of actions.| 
  - **GET /profiles/{id}/**
    - Fetches details of a specific profile by ID.
    - Returns  a single profile with its details.
      |||
      |--|--|
      |![Profiles GET](/images/readme_img/profgetid.png)|In here we have a single profile returned.|
  - **POST /profiles/**
    - Creates a new profile.
    - Profiles are automatically created when a new user is registered.
    - To note is that creating a profile from the admin panel is not an option due to restriction on the owner (User username) and it will return a message       explaining that a profile for that owner already exists.
    - |||
      |--|--|
      |![Profiles POST](/images/readme_img/profpost.png).|We can see here an example of posting a profile. This restriction works perfectly to manage data integrity and clutter of datas.|
     
  - **PUT /profiles/{id}/**
    - Updates a profile.
    - Only the profile owner or staff users can edit profiles.
      |||
      |--|--|
      |![Profiles PUT](/images/readme_img/profput.png)|As we can see here we have a form to change the profile with all its details. The image shows the current picture selected for this profile, under it a input to change the image to a new one.|
  - **DELETE /profiles/{id}/**
    - Deletes a profile.
    - Only the profile owner or staff users can delete a profile.
    - To mention is that this operation is handled only in the API admin panel and when a profile is deleted the user instance will still be preserved for data integrity.
      |||
      |--|--|
      |![Profiles DELETE](/images/readme_img/profdel.png)|A message is returned by the panel upon successfull deletion.|
  - **Filtering, Search, and Ordering**
    -  Search:
       -  You can search profiles by owner, bio, or location:
       -  GET /profiles/?search=London
    -  Ordering:
       -  Profiles can be ordered by username or location:
       -  GET /profiles/?ordering=owner__username
    -  Filtering:
       -  You can filter profiles by location or owner__username:
       -  GET /profiles/?location=London
    - **Notes**
      - A profile is automatically created when a new user registers.
      - The favourites field stores many to many relationships between profiles and products.

### Comments 
The /comments/ endpoint allows users to add, view, edit, and delete comments on products. A comment is connected to a product and a user.
- GET **/comments/**
  - Fetches a list of all comments.
  - Accessible to all, read only for non authenticated users.
  - Returns a list of comments with id, product, owner, content, created_at, and profile_picture.
    |||
    |--|--|
    |![Comments GET](/images/readme_img/comget.png)|In here we can see the comment objects fetched, each of the comments returns the details specified before, to note is that the profile_id profile_picture and created_at are set automatically upon creation.|
- **GET /comments/{id}/**
  - Fetches the details of a specific comment returning a single comment in the same format as the picture above.
- **POST /comments/**
  - Creates a new comment on a product.
  - Only authenticated users can post comments.
  - Requires a product and content.
    |||
    |--|--|
    |![Comments POST](/images/readme_img/compost.png)|An example of a comment can be created from the admin panel requiring these elements.|
- **PUT /comments/{id}/**
  -  Updates the content of a comment.
  -  Only the comment owner can edit.
  -  Request require the content field.
  -The form is the same as the POST with the only difference is that the fields are already populated with the existing data.
- **DELETE /comments/{id}/**
  - Deletes a specific comment.
  - Only the comment owner/staff users can delete comments.
    |||
    |--|--|
    |![Comments DELETE](/images/readme_img/comdel.png)|Upon successfull deletion a message is returned and data is destroyed.|
- **Filtering, Search, and Ordering**
  - Search:
    - You can search comments by owner, content, or product name:
    - GET /comments/?search=great
  - Ordering:
    - Comments can be ordered by username or created_at:
    - GET /comments/?ordering=created_at
  - Filtering:
    - You can filter comments by owner or product id:
    - GET /comments/?owner__username=name
    - GET /comments/?product=5
- **Notes**
  - Comments are automatically associated with the user.
  - The created_at field uses natural time formatting (ex:5 minutes ago).
  - Users cannot edit or delete comments they do not own(staff users can delete any comment.).

### Votes
The /votes/ endpoint allows users to rate products by assigning a vote (1-5 stars). Each user can vote only once per product, and can update an existing vote.
- **GET /votes/**
  - Fetches a list of all votes.
  - Accessible to all users, read only for non authenticated users.
  - Returns id, owner, product, vote, and created_at.
    |||
    |--|--|
    |![Vote GET](/images/readme_img/votget.png)|This is the votes returned from the GET endpoint, we can see the details of each comment with the addition of is_owner that specify the ownership of a vote.|
- **GET /votes/{id}/**
  - Fetches details of a specific vote by id.
  - Returns a single vote object (See the picture above). 
- **POST /votes/**
  - Creates or updates a vote for a product.
  - Only authenticated users can vote.
  - Users can vote only once per product. If a vote already exists, it will be updated.
    |||
    |--|--|
    |![Vote POST](/images/readme_img/votpost.png)|Simple form to post a vote requiring the Owner the Product and the value.(To note the value can be only 1-5.).|
- **PUT /votes/{id}/**
  - Updates an existing vote.
  - Only the vote owner can update.
    |||
    |--|--|
    |![Vote PUT](/images/readme_img/votput.png)|As the previous picture we have a form we the data is already prepopulated and giving the chance to update the value of the vote.|
- **DELETE /votes/{id}/**
  - Deletes a specific vote.
  - Only the vote owner can delete their vote.
    |||
    |--|--|
    |![Vote DELETE](/images/readme_img/votdel.png)|Returns a feedback of successfull deletion and the data are destroyed.|
- **Notes**
  - Users can only vote once per product (vote updates are allowed).
  - Votes are restricted to a 1-5 range and not negatives are allowed.
  - Unauthenticated users can view votes but cannot create or modify them.
  - The created_at field is formatted in natural time (ex: 5 minutes ago).
### Comparisons
The /comparisons/ endpoint allows users to compare exactly two products. Users can create, view, update, and delete comparisons, but only the owner of a comparison can modify or delete it.
- **GET /comparisons/** and **/comparisons/{id}/**
  - Fetches a list of all comparisons and fetches a comparison by id.
  - Only authenticated users can create comparisons, but all users can view them.
  - Includes comparison id, owner, products, and created_at.
    |||
    |--|--|
    |![Comparison GET](/images/readme_img/compget.png)|In here we have a single comparison object it returns an id with the owner and ownership. The products are inside and array of ids to end with the created_at.|
- **POST /comparisons/**
  - Allows authenticated users to create a comparison.
  - Must include exactly two different products.
    |||
    |--|--|
    |![Comparison POST](/images/readme_img/comppost.png)|Adding a comparison requires 2 products and this is a must. Plus the owner. The created at is added automatically to it.Selecting the same product is not allowed.|
- **PUT /comparisons/{id}/**
  - Allows the owner to update the comparison.
  - Must contain exactly two different products (same as the creation of a comparison.).
  - Refer to the above picture for the form, the only difference is that the data is already prepopulated.
- **DELETE /comparisons/{id}/**
  - Allows the owner to delete a comparison.
  - Requires authentication.
    |||
    |--|--|
    |![Comparison POST](/images/readme_img/compdel.png)|In this example we have the successfull deletion of 26 comparisons(26 were added due to the submit button still available after submission in the client side that has been fixed.)|

### Serializers and Views
- To achieve the overall I used a series of serializers and views. The views were developed with manual requests POST , PUT and DELETE to be reformatted as genereic Views to avoid clutters and better readability.
    |||
    |--|--|
    |![Generic Views](/images/readme_img/views.png)|In Here we can see an sample of the code used to achieve generic views where the requests are automatically handled. We can also see the use of the backend filters (Search,Order). [Check the Generic Views](https://docs.djangoproject.com/en/5.1/topics/class-based-views/generic-display/)|
    |![Serializers](/images/readme_img/serializers.png)|In here we have a sample code of the Serializers used. The serializers in this project handle most of the validation and errors handling.[Check out the Serializers](https://www.django-rest-framework.org/api-guide/serializers/)|

# Back To Main Page
[Click here](/README.md) to get back.

# Go to Testing
[Click here](/testing.md) to go to the Testing Section.