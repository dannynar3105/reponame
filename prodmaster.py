import pymysql
import mysql.connector
import requests
from flask import Flask,request,render_template,jsonify
import requests, json
from db_config import mysql
from flask_cors import CORS
app = Flask(__name__,template_folder='.')
url = "http://0.0.0.0:5000"
CORS(app)
cors=CORS(app,resources={r"/api/*": {"origins": "*"}})
@app.route('/get_product/',methods=['GET','POST'])
def get_product():
    mydb = mysql.connector.connect(
      host = "172.25.10.8",
      user = "root",
      passwd = "admin",
      database = "company"
      )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM product_master")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    return ('Sample Product'+myresult)
if __name__ == '__main__':
  app.run(host="0.0.0.0", port = 5000,debug=True) 
