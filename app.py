from flask import Flask, render_template, request
import mysql.connector
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_data", methods=["POST"])
def add_data():
    year_month = datetime.datetime.strptime(request.form["year_month"], "%Y-%m").date()
    water_bill = float(request.form["water_bill"])
    water_usage = int(request.form["water_usage"])
    
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kanseiA@12345",
        database="water_bill_tracker"
    )
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO water_data (`year_month`, water_bill, water_usage) VALUES (%s, %s, %s)", (year_month, water_bill, water_usage))
    conn.commit()
    cursor.close()
    conn.close()
    
    return "Data added successfully."

@app.route("/data")
def data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kanseiA@12345",
        database="water_bill_tracker"
    )
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM water_data")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template("data.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
