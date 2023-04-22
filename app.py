from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import datetime
import re

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_data", methods=["POST"])
def add_data():
    year_month_input = request.form["year_month"]

    if not re.match(r"\d{4}-\d{2}-\d{2}", year_month_input):
        return render_template("error.html", message="Invalid Year-Month-Date format. Please use YYYY-MM-DD format.")

    year_month = datetime.datetime.strptime(year_month_input, "%Y-%m-%d").date()
    water_bill = float(request.form["water_bill"])
    water_usage = int(request.form["water_usage"])
    
    conn = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="password",
        database="water_bill_tracker"
    )
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO water_data (`year_month`, water_bill, water_usage) VALUES (%s, %s, %s)", (year_month, water_bill, water_usage))
    conn.commit()
    cursor.close()
    conn.close()
    
    return render_template("data_added_success.html")

@app.route("/delete_data/<int:id>", methods=["GET"])
def delete_data(id):
    conn = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="password",
        database="water_bill_tracker"
    )
    
    cursor = conn.cursor()
    cursor.execute("DELETE FROM water_data WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    return render_template("data_deleted_success.html")

@app.route("/data")
def data():
    conn = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="password",
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

