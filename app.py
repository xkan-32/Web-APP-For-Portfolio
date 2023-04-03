from flask import Flask, request, redirect, render_template
import mysql.connector

app = Flask(__name__)

# MySQL database connection information
host = "hostname"
user = "username"
password = "password"
database = "water_bill_tracker"

# Connect to the database
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
cursor = conn.cursor()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_data", methods=["POST"])
def add_data():
    water_bill = request.form["water_bill"]
    water_usage = request.form["water_usage"]
    cursor.execute("INSERT INTO water_data (water_bill, water_usage) VALUES (%s, %s)", (water_bill, water_usage))
    conn.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
