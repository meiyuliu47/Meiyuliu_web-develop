
import unittest
from flask import Flask, session
from app import app, get_db  
import sqlite3
import os

class FlaskAppTestCase(unittest.TestCase):    
    """
    This class represents the test suite for the Flask application.
    It includes setup and teardown methods for test environment preparation
    and cleanup, along with individual test cases for registration, login,
    and reservation functionalities.
    """
    def setUp(self):
        """
        Prepare the test environment before each test.
        
        - Enable TESTING mode to isolate the test environment from production settings.
        - Disable CSRF for testing purposes.
        - Initialize the test client for sending requests to the Flask application.
        - Set up a temporary database for testing to prevent interference with the production database.
        """
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()
    
        # Configure the path for the testing database
        app.config['DATABASE'] = 'test_app.db'

        #Initialize the database schema for the test database
        with app.app_context():
            db = get_db()
            with open('schema.sql', 'r') as f:
                db.cursor().executescript(f.read())
            db.commit()

# Clean up after each test.
    def tearDown(self):
        if os.path.exists('test_app.db'):
            os.unlink('test_app.db')

# Test the registration functionality.
    def test_register(self):
        response = self.client.post('/register', data=dict(
            user_id='testuser',
            name='Test User',
            email='test@example.com',
            password='password'
        ), follow_redirects=True)
        self.assertIn('Successfully registed！', response.get_data(as_text=True))

# Test the login functionality.
    def test_login(self):
        self.test_register()
        response = self.client.post('/login', data=dict(
            user_id='testuser',
            password='password'
        ), follow_redirects=True)
        self.assertIn('Successfully signed in！', response.get_data(as_text=True))

# Test the reservation functionality.
    def test_reservation(self):
        self.test_register()
        response = self.client.post('/reservation', data=dict(
            user_id='testuser',
            number_of_people=2,
            time='2021-01-01T19:00',
            message='A table for two, please.'
        ), follow_redirects=True)
        self.assertIn('Reservation made successfully!', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
