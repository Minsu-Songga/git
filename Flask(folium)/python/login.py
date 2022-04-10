from flask import Flask, session, render_template, redirect, request, url_for
from flaskext.mysql import MySQL
 
mysql = MySQL()
login = Flask(__name__)
 
login.config['MYSQL_DATABASE_USER'] = 'mstpjt'
login.config['MYSQL_DATABASE_PASSWORD'] = '1111'
login.config['MYSQL_DATABASE_DB'] = 'mstDB'
login.config['MYSQL_DATABASE_PORT'] = 55756
login.config['MYSQL_DATABASE_HOST'] = '52.78.123.53'
login.secret_key = "ABCDEFG"
mysql.init_app(login)
 
@login.route('/Main', methods=['GET', 'POST'])
def Main():
    error = None
 
    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']
 
        conn = mysql.connect()
        cursor = conn.cursor()
        sql = "SELECT id FROM user WHERE id = %s AND pw = %s"
        value = (id, pw)
        cursor.execute("set names utf8")
        cursor.execute(sql, value)
 
        data = cursor.fetchall()
        cursor.close()
        conn.close()
 
        for row in data:
            data = row[0]
 
        if data:
            session['login_user'] = id
            return redirect(url_for('home-1'))
        else:
            error = 'invalid input data detected !'
    return render_template('Main.html', error = error)
 
 
@login.route('/register.html', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        id = request.form['regi_id']
        pw = request.form['regi_pw']
 
        conn = mysql.connect()
        cursor = conn.cursor()
 
        sql = "INSERT INTO user VALUES ('%s', '%s')" % (id, pw)
        cursor.execute(sql)
 
        data = cursor.fetchall()
 
        if not data:
            conn.commit()
            return redirect(url_for('Main'))
        else:
            conn.rollback()
            return "Register Failed"
 
        cursor.close()
        conn.close()
    return render_template('register.html', error=error)
 
@login.route('/home-1.html', methods=['GET', 'POST'])
def home():
    error = None
    id = session['login_user']
    return render_template('home-1.html', error=error, name=id)
 
if __name__ == "__main__": 
    login.run(host="192.168.123.21",port = 5555, debug=True)
