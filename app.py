from flask import Flask, render_template, request, redirect
import pymongo
from datetime import datetime
from DBUtil import GetDB

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'




class todoDaoImpl:
    def __init__(self):
        self.db = GetDB.getDatabase("todolist")
        self.collection_todo = self.db['todo']

    def add(self, task):
        self.collection_todo.insert_one(task)

    def rem(self, id):
        self.collection_todo.delete_one({ "id": id })

    def view(self):
        return self.collection_todo.find()





@app.route('/', methods=['POST', 'GET'])

def index():
    return render_template('index.html')

@app.route('/delete/<int:id>')
def delete(id):
    return '/'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    return '/'


app.run(debug=True)