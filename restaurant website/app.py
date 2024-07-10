
# Code generated using ChatGPT

from flask import Flask, request, render_template, redirect, url_for, flash, g
import sqlite3
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


# Application configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_very_secret_key'
DATABASE = '/Users/apple/Desktop/DDP/restaurant website/app.db' 

# Get database connection
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

# Close database connection
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

"""Login function
    - Implementing user login
    - Validate user id and password
    - Return login result"""
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']
        
        # Add logic to find user and validate password
        db = get_db()
        # use user_id to search the user
        user = db.execute("SELECT * FROM register WHERE user_id = ?", (user_id,)).fetchone()

        # Check if provided password matches hashed password in database
        if user and check_password_hash(user['password'], password):
            flash('Successfully signed in！')
            return redirect(url_for('index'))  # Redirect to homepage after successful login
        else:
            flash('The user id or password is incorrect')

    return render_template('login.html')

#Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_id = request.form['user_id']
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        # password encryption
        hashed_password = generate_password_hash(password)

        db = get_db()
        cur = db.cursor()
        try:
            cur.execute("INSERT INTO register (user_id, name, email, password) VALUES (?, ?, ?, ?)", (user_id, name, email, hashed_password))
            db.commit()
            
            flash('Successfully registed！')          
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('User id already exists。')
            return redirect(url_for('register'))
    return render_template('register.html')

#Reservation route
@app.route('/reservation', methods=['GET', 'POST'])
def reservation():
    if request.method == 'POST':
        # Get data from the table
        user_id = request.form['user_id']
        number_of_people = request.form['number_of_people']
        reservation_time = request.form['time']
        message = request.form['message']

        # Insert the database
        db = get_db()
        cur = db.cursor()
        cur.execute("INSERT INTO reservation (user_id, number_of_people, time, message) VALUES (?, ?, ?, ?)",
                    (user_id, number_of_people, reservation_time, message))
        db.commit()
        flash('Reservation made successfully!')
        return redirect(url_for('index'))
    else:
        return render_template('reservation.html')  


# Homepage route
@app.route('/')
def index():
    return render_template('website.complete.html')

@app.route('/the_cafe')
def the_cafe():
    return render_template('website.complete.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)