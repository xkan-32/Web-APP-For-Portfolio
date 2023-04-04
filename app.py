from flask import Flask, render_template, request
import mysql.connector
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    conn = mysql.connector.connect(
        host="localhost",
        user="user",
        password="password",
        database="water_bill_tracker"
    )
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM water_data")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template("index.html", data=data)

@app.route("/add_data", methods=["POST"])
def add_data():
    water_bill = request.form["water_bill"]
    water_usage = request.form["water_usage"]
    year_month = datetime.datetime.now().strftime("%Y-%m") # 追加するコード
    
    conn = mysql.connector.connect(
        host="localhost",
        user="user",
        password="password",
        database="water_bill_tracker"
    )
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO water_data (year_month, water_bill, water_usage) VALUES (%s, %s, %s)", (year_month, water_bill, water_usage)) # 修正するコード
    conn.commit()
    cursor.close()
    conn.close()
    
    return "Data added successfully."

if __name__ == "__main__":
    app.run(debug=True)
