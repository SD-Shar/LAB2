from flask import Flask, render_template, request, redirect, session
import mysql.connector
app = Flask(__name__)



def get_connection():
    return mysql.connector.connect(
        host="10.200.14.11",
        user="absolute_solver",
        password="silly",
        use_pure=True,
        database="new_test",
    )

@app.route("/")
def home():
    return "Flask aaaaa"

    
    
@app.route("/navn/<navn>", methods=["GET", "POST"])
def vis_navn(navn):
    return navn



@app.route("/bottle", methods=["GET", "POST"])
def name():
    if request.method == "POST":
        name = request.form["name"]
        return name
    return render_template("index.html")



@app.route("/jinja")
def jinja():
    elever = ['Mila', 'Helen', 'Jehona']
    return render_template('jinja.html', elever=elever, eleverLen= len(elever))
    
    
@app.route("/database")
def data():
    mydb = get_connection()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM folk")
    folk=mycursor.fetchall()
    
    mydb.close()
    mycursor.close()
    
    return render_template("database.html", folk=folk)
    

@app.route("/database/add", methods=["GET", "POST"])    
def new_guy():
    
    navn = session["name"]
    tlf = session["tlf"]
    
    mydb = get_connection()
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO folk (navn, tlf) VALUES (%s, %s)",(navn, tlf),)
    mydb.close()
    mycursor.close()
    
    return render_template("database.html")

    
    
if __name__ == "__main__":
    app.run(debug=True)