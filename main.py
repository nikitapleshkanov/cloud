from collections import namedtuple
import time
import subprocess
from flask import Flask, render_template, redirect, url_for, request
from pymongo import MongoClient

app = Flask(__name__)

Message = namedtuple('Message', 'text tag')
messages = []

def get_mongo_db():
	client = MongoClient(f'mongodb+srv://pleshkanov:pleshkanov@cluster0-bmzr3.azure.mongodb.net/database', 27017)
	return client.database.strings

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/main', methods=['GET'])
def main():
    return render_template('main.html', messages=messages)


@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']
    vm1(text, tag)
    solve_tasks()
    time.sleep(10)
    return redirect(url_for('main')) 

def solve_tasks():
    subprocess.Popen("bash vmpy.sh", shell=True)



def vm1(str1, str2):
	collection = get_mongo_db()
	collection.insert_one({'str1': str1, 'str2': str2})