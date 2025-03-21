from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    render_template=[]
