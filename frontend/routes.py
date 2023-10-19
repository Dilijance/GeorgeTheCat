from frontend import app
from flask import render_template, request

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/chat', methods=['GET','POST'])
def chat_page():
    return render_template('chat.html')