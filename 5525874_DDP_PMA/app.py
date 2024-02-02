from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# 配置SQLite3数据库
DATABASE = 'your_database.db'

# 创建表格（如果不存在）
def create_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            accountNumber TEXT,
            firstName TEXT,
            lastName TEXT,
            email TEXT,
            contactNumber TEXT
        )
    ''')
    conn.commit()
    conn.close()

# 创建用户
def create_user(accountNumber, firstName, lastName, email, contactNumber):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (accountNumber, firstName, lastName, email, contactNumber) VALUES (?, ?, ?, ?, ?)',
                   (accountNumber, firstName, lastName, email, contactNumber))
    conn.commit()
    conn.close()

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

@app.route('/signup', methods=['POST'])
def signup_post():
    accountNumber = request.form['accountNumber']
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    email = request.form['email']
    contactNumber = request.form['contactNumber']

    # 将用户信息插入数据库
    create_user(accountNumber, firstName, lastName, email, contactNumber)

    return redirect(url_for('success'))

@app.route('/success')
def success():
    return 'Registration successful!'

if __name__ == '__main__':
#     create_table()
    app.run(debug=True)

