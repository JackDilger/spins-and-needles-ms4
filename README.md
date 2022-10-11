<h1 align="center">Spins & Needles</h1>

![Spins & Needles Home Page](documentation/readme_images/am-i-responsive-readme.JPG)

## About

***

[Spins & Needles](https://spins-and-needles.herokuapp.com/) is an online e-commerce store selling a range of vinyl records across various music genres. The site offers full CRUD functionality for customers, they can easily add, edit and delete products from their shopping basket and quickly locate what they are looking for using the search bar. New customers benefit from signing up as a user to make use of the profiles page. Here they can pre-save delivery information for seamless checkouts and easily keep track of all their orders in one place. The site also doubles down as an advertisement for the company’s music events which are hosted at their store located in Manchester, this fits perfectly with the theme of the of site and helps attract likeminded people to their events.

## Strategy and planning

***

Why Spins & Needles?

This project was born out of my passion for music and when creating an e-commerce store, I wanted to be able to sell products I was personally invested in but would also be a viable revenue stream in a very crowded online market. 

As streaming platforms gradually took offer the market, physical music copies seem to be dying out, but Vinyl has seen a strong resurgence in recent years. Today, about 85% of mainstream music’s sales are vinyl and Last year saw U.S. revenues exceed $1 billion for the first time since the mid-80s. Ever growing interest from younger people has helped drive this, compared to the average buyer of music, buyers of vinyl records are 57% more likely to be aged under 25. Buyers clearly still appreciate the bonus of physical ownership in a world of streaming music. 

Taking all this information in to account I believe targeting the Vinyl market will help us succeed in our main aim of creating a viable revenue stream. Also, with such a large portion of sales coming from the younger age bracket I think that would offer good longevity, as we can maintain a loyal customer base who can grow with the company. 

Sales are important but we also aim to build a community of likeminded music lovers who can interact with each other. The events page was a big part of this, offering customers a chance to meet each other and enjoy local and international talent. Adding the comments section will encourage customers to interact and help build that community feel. 

One of our main aims throughout was to ensure all customer information was kept secure, and users can have peace of mind when handling payments safely with us. We understand the importance of safely managing data online, which is why we used several defensive programming features in the app to ensure this was done correctly. 

## User Experience (UX)

***

-   ### User stories

    1. As a user, I want to understand the purpose of the website immediately upon opening the site.
    2. As a user, I want to be able to easily navigate the website. 
    3. As a user, I want to be able to view a list of all products and add them to my basket.
    4. As a user, I want to easily view individual product information.
    5. As a user, I want to be able to search for an item.
    6. As a user, I want to be able to select the quantity of an item.
    7. As a user, I want to be able to edit or remove items from my basket.
    8. As a user, I want to see an overview of items in basket and see the total cost of the order.
    9. As a user, I want to be able to enter my payment details and securely checkout.
    10. As a user, I want to get email confirmation when completing an order.
    11. As a user, I want to be able to register as a user.
    12. As a user, I want to be able pre save my delivery information to my profile.
    13. As a user, I want to view my historic orders on my user profile.
    14. As a user, I want to be able to log out. 
    15. As a user, I want to be able to log in.
    16. As a user, I want to be able to view upcoming event details.
    17. As a user, I want to be able engage in the events comments section.

-   ### Site Developer/Owner

    1. As the site developer/owner, I want to be able to add a product with its information to the website
    2. As the site developer/owner, I want to be able to edit a product with its information to the website
    3. As the site developer/owner, I want to be able to delete a product with its information to the website
    4. As the site developer/owner, I want to be able moderate any event comments.

## Layout

***

- I used Balsamiq to structure the layout of my website during the initial design phase.
- I used Bootstraps built in grid system and CSS media queries to make my site responsive across all devices.

### Home page wireframe

![Home](documentation/readme_images/home-wireframe.JPG)

### Products(Shop) wireframe

![Products](documentation/readme_images/products-wireframe.JPG)

### Product Detail wireframe

![Product Detail](documentation/readme_images/product-detail-wireframe.JPG)

### Events wireframe

![Events](documentation/readme_images/events-wireframe.JPG)

### Event Detail wireframe

![Event Detail](documentation/readme_images/event-details-wireframe.JPG)

### Bag wireframe

![Bag](documentation/readme_images/bag-wireframe.JPG)

### Checkout wireframe

![Checkout](documentation/readme_images/checkout-wireframe.JPG)

### Login wireframe

![Login](documentation/readme_images/log-in-wireframe.JPG)

### Register wireframe

![Register](documentation/readme_images/register-wireframe.JPG)

### Profile wireframe

![Profile](documentation/readme_images/profile-wireframe.JPG)


## Existing Features and how they align to user stories

***

- __Logo- Links to user story 1 & 2__

  - The head of the page contains the 'Spins & Needles' logo. The logo was designed to represent the websites target audience and purpose.
  - The text content of the logo 'Spins & Needles Records' gives a clear indication immediately that the site is for a record shop. The image of a spinning record included in the logo helps reinforce this and confirms the sites purpose.
  - The logo also serves as a clickable link, allowing users a straightforward way to navigate back to the home page at any time.

![Logo](documentation/readme_images/logo-live-site.JPG)

- __Home page image gallery-  Links to user story 1 & 2__
  - The image gallery is the main focus on the home page, the images collectively offer an insight into the sites themes and purpose. 
  - The larger images display headings with additional context, they give concise information on what the site offers and invites
  the user to navigate to these sections of the website through clickable links. 

![Gallery](documentation/readme_images/home-gallery-live-site.JPG)

  
- __Search Bar- Links to user story 5__
  - The search bar is always available throughout each page of the site and allows users to easily locate what they are looking for. The placeholder text informs the user of the search criteria.

![Search](documentation/readme_images/search-bar-live-site.JPG)

- __Main Navigation- Links to user story 2__
  - The main nav bar is always available throughout each page of the site, users can easily move from page to page using the clickable links. 

![Main Navigation](documentation/readme_images/navigation-bar-live-site.JPG)

- __Products- Links to user story 3- Links to site owner goal 2 & 3__
  - When users navigate to the shopping page they get a full list of all available products.
  - Each product shows the record image, name, artist and price.
  - The images serve as a clickable link to view the full product detail of each item.
  - The edit and delete options are only shown to the admin when logged in to allow them product management.

![Products](documentation/readme_images/products-live-site.JPG)


- __Product Detail- Links to user story 3, 4 & 6__
  - Each item has its own product detail page where users can display the individual product information for each.
  - On the product details page users can add items to their shopping bag and select the quantity needed.

![Product Detail](documentation/readme_images/product-detail-live-site.JPG)

- __Events- Links to user story 16__
  - When users navigate to the events page they get a full list of all upcoming events.
  - Each event has its own dedicated page which users can navigate to using the event details button.

![Events](documentation/readme_images/events-live-site.JPG)

- __Event Details- Links to user story 16 & 17__
  - Each event has its own page showing the event information and description.
  - The event details page allows users to interact via the comments section, the form allows new comments to be submitted.
  - Existing comments are displayed once approved by the admin, they show the time, date and name of the user who left the comment.

![Event Details](documentation/readme_images/event-details-2-live-site.JPG)
![Event Details](documentation/readme_images/event-details-live-site.JPG)

- __About- Links to user story 1__
  - The about section of the website is easily accessible from the navigation bar link and offers clear insight into what the site has to offer
  - The page shows an image of the store itself and gives some information on the background of the company and what the purpose is.

![About](documentation/readme_images/about-live-site.JPG)

- __Bag- Links to user story 6, 7 & 8__
  - The shopping bag is easily accessible from the navigation bar link. 
  - Users can see an overview of items in basket and see the total cost of the order.
  - Users are able to update the quantity of an item in the bag or remove items altogether.

![Bag](documentation/readme_images/bag-live-site.JPG)

- __Checkout- Links to user story 9 & 12__
  - Users can navigate to the checkout using the secure checkout button in the bag.
  - A form is available to enter the delivery and contact information.
  - Logged in users have the benefit of saving delivery information to their profiles to be pre filled the next time they shop.
  - Users can easily enter their payment details through the secure payment system in the checkout.

![Checkout](documentation/readme_images/checkout-live-site.JPG)

- __Order Confirmation- Links to user story 10__
  - When an order is successfully placed users are taken to the confirmation order page, this gives an overview of the order.
  - Email confirmation is sent to the provided contact email address.

![Complete order & Confirmation](documentation/readme_images/order-confirmation-live-site.JPG)
![Complete order & Confirmation](documentation/readme_images/email-confirmation.JPG)


- __Profile- Links to user story 12 & 13__
  - Logged in users can access their profile through the my account drop down section of the main navigation bar.
  - They can maintain their up-to-date delivery information and view their historic orders.
  - Clicking into the order number will show a copy of the confirmation order page.

  ![Profile](documentation/readme_images/profile-live-site.JPG)


- __Register- Links to user story 11__
  - Users can register for the site to give them access to the profiles page.
  - The registration form is easily accessed through my account drop down section of the main navigation bar.

  ![Register](documentation/readme_images/register-live-site.JPG)


- __Log in- Links to user story 15__
  - Users can access their existing profile information by logging in to the site.
  - The login form is easily accessed through the my account drop down section of the main navigation bar.

  ![Login](documentation/readme_images/login-live-site.JPG)


- __Log Out- Links to user story 14__
  - Logged in users can easily log out at any time.
  - The logout option is easily accessed through the my account drop down section of the main navigation bar.

  ![Logout](documentation/readme_images/logout-live-site.JPG)


- __Product Management- Links to site owner goal 1__
  - The product management page is only accessible by approved super users, it can be accessed through the my account section of the main navigation bar.
  - This page allows the site admin to add new products directly into the site.


  ![Product Managment](documentation/readme_images/product-managment-live-site.JPG)


- __Edit Product- Links to site owner goal 2__
  - Approved super users can edit any product, the edit option is displayed on each product when the admin is logged in.
  - The edit product form prefills the existing product information and allows the admin to make any changes required.

  ![Edit Product](documentation/readme_images/edit-product-live-site.JPG)


- __Delete Product- Links to site owner goal 3__
  - Approved super users can delete any product, the delete option is displayed on each product when the admin is logged in.
  - The delete button will trigger a modal to open to allow the option to confirm deletion

  ![Delete Product](documentation/readme_images/product-delete-edit.JPG)
  ![Delete Modal](documentation/readme_images/delete-modal-live-site.JPG)

- __Moderate Comments- Links to site owner goal 4__
  - Any comment added to the site must first be approved by a super user.
  - The admin can moderate all comments by logging in to the [Django Admin](https://spins-and-needles.herokuapp.com/admin/login/?next=/admin/). This will soon be available in product management as part of the sites future development
  - In the comments section of Django admin there is the option to approve/delete any comment.

  ![Moderate Comment](documentation/readme_images/moderate-comments-admin.jpg)


## Data Schema

***

![Schema](documentation/readme_images/schema-design.JPG)

The above shows the database design followed when building this site, a relational database was used with the PostgreSQL option in Heroku.

[Django Allauth](https://pypi.org/project/django-allauth/) was integrated in to the site to make use of their built in authentication system.

The above design shows the key relationships between the date stored; I will outline some examples shown. The user and the user profile is a 1 to 1 relationship, only 1 user profile is permitted per user. The design also shows how the user primary key is used as a foreign key in the user profile.

The relationship between an event blog post and a blog comment is a one-to-many relationship meaning many comments can go into 1 post. The design again shows how the blog post primary key is used as a foreign key in the blog comments. Another example of this is shown with products and genres, as many products can go into one genre.

## Testing

***


Please refer to seperate [Testing](testing.md) file for full the full breakdown on testing.