<h1>Online Store</h1>
<p align="left">
   <img src="https://img.shields.io/badge/Python-3.11-yellow" alt="Python Version">
   <img src="https://img.shields.io/badge/Django-5.0-blue" alt="Beautiful Soup Version">
   
</p>

## About

An online store project in which I implemented a shopping cart using Django sessions, customer order registration, 
asynchronous tasks, social authentication, a comment system and wish list, a personal account page, a payment gateway, 
exporting orders to CSV and generating invoices to PDF, and a recommendation system.


## Running with Docker ![Docker](https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

1. Clone the repository:

   `git clone https://github.com/Amato789/iShop`

2. Create an `.env` file. and add your own data following the structure and path of the `.env_example` file.
3. Use `make app` to run application and database infrastructure.
4. Use `make migrate` to apply migration, create all needed db and add some default data (Category, Brand, Product).
5. Use `make createsuperuser` to create admin user.
6. Use `make app-logs` to follow the logs in app container.
7. In payment Stripe service form you can use:
   
   - Card number: 4242 4242 4242 4242
   - Use a valid future date, such as 12/34
   - Use any three-digit CVC (four digits for American Express cards).
   - Use any value you like for other form fields.


## Available commands:

`make app` - Up application and database infrastructure

`make app-logs` - Follow the logs in app container

`make app-down` - Down application and all infrastructure

`make container-shell` - Go to container shell

`make storages-shell` - Go to storages shell

`make migrate` - Apply all made migrations

`make makemigrations` - Make migrations to models

`make createsuperuser` - Create admin user

`make collectstatic` - Collect static
