#DATABASE
from flask import Flask, render_template, request, url_for, redirect
import sqlite3
app = Flask(__name__)
conn = sqlite3.connect('database.db')
print ("Opened database successfully")
conn.execute("DROP TABLE IF EXISTS Board")  # Board 테이블이 기존에 있다면 삭제 (매번, 동일한 파일에서 실행하면, 내용이 겹쳐서 만듦)
conn.execute('CREATE TABLE IF NOT EXISTS Board (name TEXT, context TEXT)')  # Board 테이블이 기존에 없다면 생성
print ("Table created successfully")
name = [['Elice', 15], ['Dodo', 16], ['Checher', 17], ['Queen', 18]]
for i in range(4):
    conn.execute(f"INSERT INTO Board(name, context) VALUES('{name[i][0]}', '{name[i][1]}')")
conn.commit()
conn.close()
 
# root = home
@app.route('/')
def board():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("select * from Board")
    rows = cur.fetchall()
    print("DB:")
    for i in range(len(rows)):
            print(rows[i][0] + ':' + rows[i][1])
    return render_template('board1.html', rows = rows)
 
# 게시물 조회 (Read)
@app.route('/search', methods = ['GET', 'POST'])
def search():
    if request.method == 'POST':
        name = request.form['name']
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute(f"SELECT * FROM Board WHERE name='{name}' or context='{name}'")
        rows = cur.fetchall()
        print("DB:")
        for i in range(len(rows)):
            print(rows[i][0] + ':' + rows[i][1])
        return render_template('search.html', rows = rows)
    else:
        return render_template('search.html')
 
# 게시물 생성 (Create)
@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        try:
            name = request.form['name']
            context = request.form['context']
            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute(f"INSERT INTO Board (name, context) VALUES ('{name}', '{context}')")
                con.commit()
        except:
            con.rollback()
        finally : 
            con.close()
            return redirect(url_for('board'))
    else:
        return render_template('add.html')
# 위에 조회, 생성은 이전과 동일 
 
# 게시물 내용 갱신(Update)
@app.route("/update/<uid>", methods=["GET","POST"])
def update(uid):
    if request.method == "POST":
        name = request.form["name"]
        context = request.form["context"]
        
        # 내용 갱신하고
        with sqlite3.connect("database.db") as con:
            cur = con.cursor()  # connection한 db에 접근하기 위해, cursor 객체 만들기
            cur.execute(f"UPDATE Board SET name='{name}', context='{context}' WHERE name='{uid}'")
            con.commit()
 
        return redirect(url_for("board"))   # 갱신되었는지, board함수 리다이렉트해서, / 페이지 렌더링
    else:
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute(f"SELECT * FROM Board WHERE name='{uid}'")
        row = cur.fetchall()
        return render_template("update.html",row=row)
 
@app.route("/delete/<uid>")
def delete(uid):
    # 들어온 uid 값이랑 name이랑 delete 연산하고 반영
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        cur.execute(f"DELETE FROM Board WHERE name='{uid}'")
        con.commit()
 
    return redirect(url_for('board'))  # 삭제 반영하고, 반영됬는지, board함수 리다이렉트, / 페이지 렌더링
 
if __name__ == '__main__':
    app.run()