from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",   # 👈 put your password
    database="pharmacare"
)

# HOME
@app.route("/")
def index():
    return render_template("index.html")

# ADD MEDICINE
@app.route("/add", methods=["POST"])
def add_medicine():
    name = request.form["name"]
    price = float(request.form["price"])
    desc = request.form["desc"]

    cur = db.cursor()
    cur.execute(
        "INSERT INTO medicines (name, price, description) VALUES (%s,%s,%s)",
        (name, price, desc)
    )
    db.commit()
    return redirect("/view")

# VIEW MEDICINES
@app.route("/view")
def view_medicines():
    cur = db.cursor()
    cur.execute("SELECT * FROM medicines")
    data = cur.fetchall()
    return render_template("view.html", medicines=data)

# DELETE
@app.route("/delete/<int:id>")
def delete_medicine(id):
    cur = db.cursor()
    cur.execute("DELETE FROM medicines WHERE id=%s", (id,))
    db.commit()
    return redirect("/view")

# CHAT BOT
@app.route("/chat", methods=["GET","POST"])
def chat():
    reply = ""
    if request.method == "POST":
        q = request.form["question"].lower()
        if "fever" in q:
            reply = "Take paracetamol after food"
        elif "cold" in q:
            reply = "Drink warm water and rest"
        elif "headache" in q:
            reply = "Take a mild pain reliever"
        else:
            reply = "Please consult a doctor"

    return render_template("chat.html", reply=reply)

if __name__ == "__main__":
    app.run(debug=True)
