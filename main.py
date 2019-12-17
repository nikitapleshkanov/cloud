from collections import namedtuple
import time
import subprocess
import threading 
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
    print('help')
    solve_tasks1()
    time.sleep(10)
    print(1.1)
    solve_tasks2()
    time.sleep(5)
    print(1)
    solve_tasks3()
    time.sleep(5)
    return redirect(url_for('main'))



def solve_tasks1():
	print('start2222')
	subprocess.Popen("bash vmup.sh", shell=True)
	time.sleep(10)

def solve_tasks2():
    subprocess.Popen("bash vmpy.sh", shell=True)
    time.sleep(10)

def solve_tasks3():
	subprocess.Popen("bash vmdown.sh", shell=True)
	time.sleep(10)


def vm1(str1, str2):
    collection = get_mongo_db()
    collection.insert_one({'str1': str1, 'str2': str2})