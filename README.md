💊 Pharma Care – Healthcare Web Application

Pharma Care is a web-based healthcare application developed using Python Flask and MySQL.
The application helps users manage medicine information and provides basic healthcare guidance through a simple chat query bot.

🚀 Features

Add, view, and delete medicine details (CRUD operations)

Store medicine data securely in MySQL

Rule-based healthcare chat bot for basic queries

Clean and responsive UI using Bootstrap

Simple and user-friendly interface

🛠️ Technologies Used

Backend: Python, Flask

Frontend: HTML, CSS, Bootstrap

Database: MySQL

Tools: VS Code, MySQL Workbench

📁 Project Structure
pharma_care/
│
├── app.py
├── templates/
│   ├── index.html
│   ├── view.html
│   └── chat.html
│
├── static/
│   └── style.css
│
└── database.sql

🗄️ Database Schema

Database Name: pharmacare

Table: medicines

Column	Type
id	INT (Primary Key)
name	VARCHAR(100)
price	DOUBLE
description	VARCHAR(255)
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/pharma-care-flask.git
cd pharma-care-flask

2️⃣ Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install flask mysql-connector-python

4️⃣ Setup MySQL Database

Open MySQL Workbench and run:

CREATE DATABASE pharmacare;
USE pharmacare;

CREATE TABLE medicines (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price DOUBLE,
    description VARCHAR(255)
);

5️⃣ Update database credentials in app.py
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD",
    database="pharmacare"
)

6️⃣ Run the application
python app.py


Open browser:

http://127.0.0.1:5000

🤖 Chat Bot

The chatbot is rule-based and responds to basic healthcare-related queries such as:

Fever

Cold

Headache

⚠️ This chatbot is for educational purposes only and does not replace medical advice.

📸 Output

Add Medicine Page

View Medicines Table

Chat Query Bot Interface

🎯 Learning Outcomes

Hands-on experience with Flask framework

Database integration using MySQL

Implementation of CRUD operations

Basic chatbot logic

Frontend design using Bootstrap

🔮 Future Enhancements

User login and authentication

Medicine search and update functionality

AI-based chatbot integration

Online medicine ordering

Deployment on cloud platforms

⚠️ Disclaimer

This project is developed for educational purposes only.
It does not provide professional medical advice.

👤 Author

Simran Qureshi
Python & Web Development Enthusiast
