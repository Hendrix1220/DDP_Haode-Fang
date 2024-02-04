import os
import uuid
from flask import Flask, flash, render_template, request, redirect, session, url_for
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# 配置SQLite3数据库
DATABASE = 'users.db'

def init_db():
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
             accountNumber INTEGER PRIMARY KEY AUTOINCREMENT,
             firstName TEXT NOT NULL,
             lastName TEXT NOT NULL,
             email TEXT NOT NULL UNIQUE,
             contactNumber TEXT NOT NULL,
             password TEXT NOT NULL
            )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
        id TEXT PRIMARY KEY,
        account_number INTEGER NOT NULL,
        booking_name TEXT NOT NULL,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        restaurant_name TEXT NOT NULL,
        contact_number TEXT NOT NULL
    )
    ''')
        conn.commit()


def create_user(firstName, lastName, email, contactNumber, password):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password)
    cursor.execute('''
        INSERT INTO users (firstName, lastName, email, contactNumber, password) 
        VALUES (?, ?, ?, ?, ?)''',  # Updated to match the revised column list
        (firstName, lastName, email, contactNumber, hashed_password))
    conn.commit()
    conn.close()

# def save_booking(account_number, booking_name, date, time, restaurant_name, contact_number):
#     conn = sqlite3.connect(DATABASE)
#     cursor = conn.cursor()
#     id = str(uuid.uuid4())
#     query = '''INSERT INTO bookings (id, account_number, booking_name, date, time, restaurant_name, contact_number)
#                VALUES (?, ?, ?, ?, ?, ?, ?)'''
#     cursor.execute(query, (id, account_number, booking_name, date, time, restaurant_name, contact_number))
#     conn.commit()
#     conn.close()

def save_booking(account_number, booking_name, date, time, restaurant_name, contact_number):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        id = str(uuid.uuid4())
        query = '''INSERT INTO bookings (id, account_number, booking_name, date, time, restaurant_name, contact_number)
                   VALUES (?, ?, ?, ?, ?, ?, ?)'''
        cursor.execute(query, (id, account_number, booking_name, date, time, restaurant_name, contact_number))
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"An integrity error occurred: {e}")
        # 在这里可以添加更多的错误处理逻辑，比如回滚事务、记录到日志文件等
    except Exception as e:
        print(f"An error occurred: {e}")
        # 处理其他类型的异常
    finally:
        conn.close()  # 确保数据库连接总是被关闭



# 路由和视图函数
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template("login.html")

@app.route('/all_restaurants')
def all_restaurants():
    return render_template('all_restaurants.html')

@app.route('/all_cafes')
def all_cafes():
    return render_template('all_cafes.html')

@app.route('/all_foodstations')
def all_foodstations():
    return render_template('all_foodstations.html')

@app.route('/DirtyDuck')
def DirtyDuck():
    return render_template('DirtyDuck.html')

@app.route('/WBSCafe')
def WBSCafe():
    return render_template('WBSCafe.html')

@app.route('/Varsity')
def Varsity():
    return render_template('Varsity.html')

@app.route('/Cosco')
def Cosco():
    return render_template('Cosco.html')

@app.route('/Starbucks')
def Starbucks():
    return render_template('Starbucks.html')

@app.route('/Pret')
def Pret():
    return render_template('Pret.html')

@app.route('/Thaifood')
def Thaifood():
    return render_template('Thaifood.html')

@app.route('/ChineseRamen')
def ChineseRamen():
    return render_template('ChineseRamen.html')

@app.route('/ItalyTaco')
def ItalyTaco():
    return render_template('ItalyTaco.html')

@app.route('/Contact')
def ContactUs():
    return render_template('ContactUs.html')
@app.route('/booking')
def booking():
    return render_template('booking.html')
@app.route('/signup')
def signup():
    return render_template('signup.html')

# @app.route('/signup', methods=['POST'])
# def signup_post():
#     accountNumber = request.form['accountNumber']
#     firstName = request.form['firstName']
#     lastName = request.form['lastName']
#     email = request.form['email']
#     contactNumber = request.form['contactNumber']

@app.route('/signup', methods=['POST'])
def signup_post():
    # Fetching form data
    firstName = request.form.get('firstName')
    lastName = request.form.get('lastName')
    email = request.form.get('email')
    contactNumber = request.form.get('contactNumber')
    password = request.form.get('password')  # Correctly fetching the password from form

    # Perform your validation and user creation logic
    if not (firstName and lastName and email and contactNumber and password):
        flash('Please fill out all fields.')
        return redirect(url_for('signup'))

    try:
        create_user(firstName, lastName, email, contactNumber, password)
        flash('Signup successful!')
        return redirect(url_for('index'))
    except sqlite3.IntegrityError:
        flash('Signup failed. User might already exist.')
        return redirect(url_for('signup'))

@app.route("/login", methods=["GET", "POST"])
def login_post():
    if request.method == "POST":
        accountNumber= request.form.get('accountNumber')
        password = request.form.get('password')

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE accountNumber = ?", (accountNumber,))
        user = cursor.fetchone()

        if user and check_password_hash(user[5], password):  # 假设密码是第六个字段
            flash("Login successful!")
            return redirect(url_for('index'))  # 登录成功后重定向到首页或其他页面
        else:
            flash("Invalid email or password. Please try again.")

    # 对于 GET 请求或登录失败，显示登录表单
    return render_template("login.html")




@app.route('/submit-booking', methods=['POST'])
def submit_booking():
    
    account_number = request.form['accountNumber']
    booking_name = request.form['bookingName']
    date = request.form['date']
    time = request.form['time']
    restaurant_name = request.form['restaurantName']
    contact_number = request.form['contactNumber']
    
    # 保存预订信息到数据库
    save_booking(account_number, booking_name, date, time, restaurant_name, contact_number)
    
    flash('Your reservation has been successfully submitted!')
    return redirect(url_for('index'))  # 假设您有一个名为 'index' 的路由作为首页



# @app.route('/success')
# def success():
#     return 'Registration successful!'

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

