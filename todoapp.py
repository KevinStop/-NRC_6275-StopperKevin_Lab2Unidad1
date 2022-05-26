#import libreria Flask
import email
from turtle import title
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def helloworld():
    return render_template("index.html")

@app.route('/enviar', methods=['POST'])
def enviar():
    title = request.form['title']
    return "<td>"+ title +"</td>"



if __name__ == "__main__":
    app.run(debug=True)
