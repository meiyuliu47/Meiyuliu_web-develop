from flask import Flask, request, render_template, redirect, url_for, flash, g
import sqlite3

# 应用配置
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_very_secret_key'
DATABASE = 'app.db'

# 获取数据库连接
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

# 关闭数据库连接
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# 注册路由和视图函数
@app.route('/register', methods=['GET', 'POST'])
def register():
    print("注册视图函数被调用")
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # 这里应该添加密码加密步骤，例如使用 Werkzeug 的 generate_password_hash
        db = get_db()
        cur = db.cursor()
        try:
            cur.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, password))
            db.commit()
            flash('注册成功！')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('用户名已存在，请选择其他用户名。')
            return redirect(url_for('register'))
    return render_template('register.html')

# 登录路由
@app.route('/login', methods=['GET', 'POST'])
def login():
    print('啦啦啦')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # 这里应该添加查找用户和验证密码的逻辑
        db = get_db()
        user = db.execute("SELECT * FROM Users WHERE username = ?", (username,)).fetchone()

        if user and user["password"] == password:  # 假设密码是明文存储（实际开发中应使用密码哈希）
            flash('登录成功！')
            return redirect(url_for('index'))  # 登录成功后重定向到首页或其他页面
        else:
            flash('用户名或密码错误')

    return render_template('login.html')

@app.route('/reservation', methods=['GET', 'POST'])
def reservation():
    print("预定视图函数被调用")
    if request.method == 'POST':
        user_id = request.form['user_id']
        reservation_date = request.form['reservation_date']
        time = request.form['time']
        email = request.form['email']
        number_of_people = request.form['number_of_people']
        special_request = request.form['special_request']
        # 这里应该添加密码加密步骤，例如使用 Werkzeug 的 generate_password_hash
        db = get_db()
        cur = db.cursor()
        try:
            cur.execute("INSERT INTO reservation (user_id, reservation_date, time, email, number_of_people, special_request) VALUES (?, ?, ?, ?, ?, ?)", (user_id, reservation_date, time, email, number_of_people, special_request))
            db.commit()
            flash('注册成功！')
            return redirect(url_for('reservation'))
        except sqlite3.IntegrityError:
            flash('用户名已存在，请选择其他用户名。')
            return redirect(url_for('reservation'))
    return render_template('reservation.html')

@app.route('/membership_update', methods=['GET', 'POST'])
def update_membership():
    if request.method == 'POST':
        member_id = request.form.get('id')
        amount = int(request.form.get('amount'))
        db = get_db()
        cur = db.cursor()

        cur.execute('SELECT * FROM members WHERE id = ?', (member_id,))
        member = cur.fetchone()

        if member:
            # Update existing member
            new_points = member['points'] + amount
            new_level = new_points //100 + 1 
            cur.execute('UPDATE members SET points = ?, level = ? WHERE id = ?', (new_points, new_level,member_id))
        else:
            # Create new member
            cur.execute('INSERT INTO members (id, points,level) VALUES (?, ?, ?)', (member_id, amount, 1))
        
        db.commit()
        return redirect(url_for('index'))
    else:
        return render_template('membership_update.html')


@app.route('/member-info', methods=['GET', 'POST'])
def member_info():
    member = None
    if request.method == 'POST':
        member_id = request.form.get('query_id')
        conn = get_db()
        member = conn.execute('SELECT * FROM members WHERE id = ?', (member_id,)).fetchone()
        if not member:
            flash('Member not found.')
            return render_template('member_info.html')
    return render_template('member_info.html', member=member)


# 首页路由，重定向到注册页面
@app.route('/')
def index():
    return "这是首页，用户登录成功后看到的页面。"

if __name__ == '__main__':
    app.run(debug=True)
