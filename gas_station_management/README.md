# Gas Station Management System

This project is a web application for managing a gas station. It provides functionalities for handling products, users, and tickets. The application is structured in a modular way, allowing for easy maintenance and scalability.

## Project Structure

```
gas_station_management
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── controllers
│   │   ├── __init__.py
│   │   ├── products_controller.py
│   │   ├── users_controller.py
│   │   └── tickets_controller.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── product.py
│   │   ├── user.py
│   │   └── ticket.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── products_routes.py
│   │   ├── users_routes.py
│   │   └── tickets_routes.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── product_service.py
│   │   ├── user_service.py
│   │   └── ticket_service.py
│   └── templates
│       ├── base.html
│       ├── products.html
│       ├── users.html
│       └── tickets.html
├── config
│   ├── __init__.py
│   ├── database.py
│   └── settings.py
├── migrations
│   └── README.md
├── tests
│   ├── __init__.py
│   ├── test_products.py
│   ├── test_users.py
│   └── test_tickets.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Features

- **Product Management**: Add, update, delete, and view products.
- **User Management**: Manage user accounts and permissions.
- **Ticket Management**: Create and manage tickets for transactions.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd gas_station_management
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python app/main.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.