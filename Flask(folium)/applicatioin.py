from flask import url_for, session, Flask, render_template, request, redirect
from flaskext.mysql import MySQL

mysql = MySQL()
application = Flask(__name__)


application.config['MYSQL_DATABASE_USER'] = 'mstpjt'
application.config['MYSQL_DATABASE_PASSWORD'] = '1111'
application.config['MYSQL_DATABASE_DB'] = 'mstDB'
application.config['MYSQL_DATABASE_PORT'] = 51933
application.config['MYSQL_DATABASE_HOST'] = '13.209.17.209'
application.secret_key = "ABCDEFG"
mysql.init_app(application)
 
@application.route('/', methods=['GET', 'POST'])
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
            return redirect(url_for('login'))
        else:
            error = 'invalid input data detected !'
    return render_template('login.html', error = error)
 
 
@application.route('/register.html', methods=['GET', 'POST'])
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
            return redirect(url_for('login'))
        else:
            conn.rollback()
            return "Register Failed"
 
        cursor.close()
        conn.close()
    return render_template('register.html', error=error)
 
# @application.route('/home-1.html', methods=['GET', 'POST'])
# def home_1():
#     error = None
#     id = session['login_user']
#     return render_template('home-1.html', error=error, name=id)
 

@application.route("/HOME")
def home():
    return render_template("home.html")
    
@application.route("/login", methods = ["get"])
def login():
    global ID, PW
    _id_ = request.args.get("loginId")
    _password_ = request.args.get("loginPw")
        
    if id == _id_ and _password_ == pw:
        session["userID"] = _id_
        return redirect(url_for("login_page"))
    else:
        return redirect(url_for("login_page"))
            


# @application.route("/logout")
# def logout():
#     session.pop("userID")
#     return redirect(url_for("login_page"))



@application.route("/camera1", methods=["GET","POST"])
def camera1():
    return render_template("camera1.html")

@application.route("/camera2", methods=["GET","POST"])
def camera2():
    return render_template("camera1.html")
@application.route("/camera3", methods=["GET","POST"])
def camera3():
    return render_template("camera1.html")


@application.route("/map1", methods=["GET"])
def map1():
    return render_template("save.html")


if __name__ == "__main__": 
    application.run(host="0.0.0.0" ,debug=True)
    # application.run(host="192.168.123.21",port = 5555, debug=True)
    



