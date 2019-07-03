from flask import Flask, render_template, request
import  pymysql.cursors

app = Flask(__name__)
db = pymysql.connect("localhost", "root", "anand@123", "TESTDB")
cursor=db.cursor()
@app.route('/',methods=['GET','POST'])

def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        cursor = db.cursor()

        cursor.execute("insert into STUDENT values (%s,%s)", (first_name, last_name,))
        db.commit()

    return render_template("cgi_post.html")
if __name__ ==  "__main__":
    app.run(debug=True)
