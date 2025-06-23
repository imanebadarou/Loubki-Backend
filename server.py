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