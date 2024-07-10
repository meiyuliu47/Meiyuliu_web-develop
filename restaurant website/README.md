# The Cafe Warwick Web Application

## Description

The Cafe Warwick Web Application is a Flask-based web platform designed to offer users a comprehensive experience including features like Home, Menu, Reservation, and Register/Login functionalities. The application utilizes Flask for backend logic and SQLite for database management, providing an intuitive interface for managing user registrations, logins, and reservations.

## Features

- User login and registration with hashed passwords.
- Ability to make reservations with user-specific details.
- Simple and intuitive UI for interaction.

## Installation

To run this project, you need Python, Flask and SQLite installed on your machine.

## Initial Setup

1. **Clone this repository:

Clone the project to your local machine using the following command:
```bash
git clone https://your-repository-link.git
cd your-repository-folder
```

2. **Install required packages

Install the necessary Python packages including Flask:
```bash
pip install -r requirements.txt
```

3. **Database Setup
To set up the SQLite database for the first time, run the following Python code:
import sqlite3

connection = sqlite3.connect('app.db')
with connection:
    connection.execute("""
    CREATE TABLE IF NOT EXISTS register (
        user_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );
    """)
    connection.execute("""
    CREATE TABLE IF NOT EXISTS reservation (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        number_of_people INTEGER,
        time TEXT NOT NULL,
        message TEXT,
        FOREIGN KEY (user_id) REFERENCES register (user_id)
    );
    """)

4. Navigate to the project directory and run the application:
```bash
python app.py
```

5. **Running the Application
```bash
falsk run
```

## Testing

### Running Tests

This application includes a suite of unittests to verify the functionality of registration, login, and reservation features. To run these tests, follow the steps below:

1. **Ensure Testing Environment**: Make sure your application is set up for testing by configuring the `TESTING` flag and a test database in the application configuration.

2. **Initialize the Test Database**: Before running the tests, ensure your test database schema is set up correctly. You can use the `schema.sql` script provided in the project to initialize your test database.

3. **Run the Tests**:
    - Navigate to the project directory in your terminal or command prompt.
    - Run the test:
```bash
python app_test.py
```
This command will execute all the test cases defined in `app_test.py`. Successful execution without any errors indicates that your application's core functionalities are working as expected.

4. **Test Cases Included**:
    - Test Register:** Verifies that a new user can successfully register.
    - Test Login:** Ensures that a registered user can log in.
    - Test Reservation:** Checks if a registered user can make a reservation.

Each test case posts data to the respective route and checks the response to ensure it contains the expected success message. This process verifies that the application's core functionalities are working correctly.

5. **Debugging Tests**:
- If any test fails, the output will indicate which test failed and why. This information can be used to debug issues within the application.
- It's recommended to check the configuration and ensure that the `test_app.db` is correctly set up as per the `schema.sql`.

By following these instructions, you can run tests to ensure the application's robustness and reliability before deployment or after making changes to the codebase.

## Contributing

Contributions to the project are welcome. Please ensure to follow the existing coding style and submit pull requests for any new features or bug fixes.