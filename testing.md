# Testing
## Testing Map
- [Testing](#testing)
  - [Testing Map](#testing-map)
  - [Manual Testing](#manual-testing)
    - [Example of what I tried](#example-of-what-i-tried)
  - [Automated Tesing](#automated-tesing)
    - [Auto test on Comparisons](#auto-test-on-comparisons)
    - [Auto test showcase](#auto-test-showcase)
  - [More testing](#more-testing)

[Back to main page](/README.md)  
## Manual Testing

||||
|--|--|--|
|Create / Update/ Delete a category|Create: ok/ Update: ok / Delete: ok|When deleting a category make sure that the category doesn't contain Products or an error is thrown.|
|Create/ Update/ Delete a product|Create: ok/ Update: ok/ Delete: ok| When creating a product a feedback is sent if the product already exists, Deleting a product gives a confirm message that shows all the object that the product contains like votes or comments.|
|Create/ Update/ Delete a Comment|Create: ok / Update: ok/ Delete: ok| No issues encountered.|
|Create/ Update/ Delete a Vote|Create: ok/ Update: ok/ Delete: ok|When a vote is created it make sure that the vote is in range of 1-5.|
|Create/ Update/ Delete a profile|For the profile the creation is handled by the signal on the User model. |No issues encoutered deleting or updating.|
|Create/ Update/ Delte a Comparison|Create: ok/ Update: ok/ Delete: ok|When creating or updating the Comparison it makes sure that you can select only 2 products and not the same product twice. No issues on deleting.|

### Example of what I tried
- Create a new Comparison selecting two or more or less products.
- Create a new category with a already used name.
- Add a comment on a product without owner.
- Don't details for the product: name, category, description, price, location, and features.
- Add wrong details for the product: same name, negative price.
- Deleting a Product deleted also votes and comments.
- Average rating returns right value and null when no vote has been made.
- For the profile I tried to add different users and the name is always matching and default picture.
- Tried to create a user with an already existing username.
- Tried adding favourites and check matching of ids.
- Tried adding a vote on a product and check the average rating if matches.
- Vote can only be selected in the range of 1-5.
- Tried deleting objects and see if other objects are deleted on cascade.
- No issues were found.


## Automated Tesing

### Auto test on Comparisons

- Two test cases for the Comparison:
  - 1. A user can successfully retrieve a valid Comparison
      - For this test I set up a Test User with Test and Pass credentials.
      - I also set Up a test category with two test products.
        - self.test_category = Category.objects.create(name="test")
        - self.product1 = Product.objects.create(  
          owner=self.test_user,  
          name="Product1",   
          price="10.00",   
          category=self.test_category  
          )  
          self.product2 = Product.objects.create(  
          owner=self.test_user,  
          name="Product2",  
          price="15.00",  
          category=self.test_category  
          )  
      - A comparison was set up using these details.
      - Using the self.assertEqual I checked the status of the response and the mathing owner.
      - Test pass. 
      - Tried to use different status, different owner and test fails.
 
  - 2. Tried to retrieve a non existent Comparison 
      - Using the same set up as the previous test.
      - I tried using a different id than the one specified.
        - Using self.assertEqual to check the response on a 404 status
        - Test pass
          - Tried to put the same id and test fails. 
    - Overview of this test:
    - A valid Comparison object can be retrieved successfully 200 response.
    - Trying to retrieve a worng id Comparison returns a 404 response.
    - The fetched data includes the correct owner information.
 - Two test cases for the Product:
   -  This test case verifies that a list of products can be fetched successfully.
   -  As the previous test I set up a test User with test crendentials and a category 
      -  def setUp(self):  
          self.test_user = User.objects.create_user(  
        username='test', password='pass'  
    )  
    self.test_category = Category.objects.create(name='test')  
    - In the test I created a test product.
    - The test creates a product connected to the user and the category and returns a 200 status on a GET request for a get('/products/').
      - Test pass.
      - Tried a 201 status and test fails.
 
    - In the second test I set up a test user, a test category and 2 test products.
      - The two products contains owner, name ,price and the connected test category.
      - The test consist in retrieving the id of the products and check if matches.
        - using a GET request on the ('/products/1/') we set the assertEqual on the name:
          - Product with id 1 has name: name1.
          - The response on the get request returns a 200 status
          - Test pass
          - Trying to pass a 201 status
          - Test fails.
 
      - Another test made on product was to retrieve the product with a non existent id.
        - Using the same set up as before:
          - I tried to send a GET request on a test id ('/products/123/')
            - Using a assertEqual on the status code 404
            - Test pass
            - If the status passed is a 200
            - Test fails

  ### Auto test showcase

  - When we want to try to check the tests run this command on the terminal:
    - python3 manage.py test
      |||
      |--|--|
      |![Running Tests](/images/readme_img/test1.png)|In here we have a representation of all the tests passing.|
      |![Failed Test](/images/readme_img/failtest.png)|In this case we see how the 201 response let the test fail.|
      |The tests are built using the TestCase that is a **unittest** based test.|[Learn more about unittest here](https://realpython.com/python-unittest/)|

## More testing
-  The code has been passed in through the Code Institute Python Linter

    |||
    |--|--|
    |Categories Folder files.|Passed without issues.|
    |Comments Folder files.|Passed without issues.|
    |Comparisons Folder files.|Passed without issues.|
    |Products Folder files.|Passed without issues.|
    |Profiles Folder files.|Passed without issues.|
    |Votes Folder files.|Passed without issues.|
    |drf_api_head2head Folder files|Passed without issues.|
    |![Python Linter](/images/readme_img/linter.png)|In here an example of how to use the linter. Paste the full code over and the Linter will display any issue on the right side of the page. Follow this link to check it out. ([Link to Linter](https://pep8ci.herokuapp.com/)) |
