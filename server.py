from flask import Flask,render_template,request
import mysql.connector

serveur = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="MVC"
)
mycursor = mydb.cursor()

# mycursor.execute('''create table games(id int primary key auto_increment, nom varchar(50), prix int, description varchar(200))
#                  ''')
# mydb.commit()

@serveur.route('/')
def accueil():
    return render_template('accueil.html')


    