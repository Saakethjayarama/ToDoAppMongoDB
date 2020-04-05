from flask import Flask, render_template, request, redirect
import pymongo
from datetime import datetime
from DBUtil import GetDBUtil

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'


id = 0

class ToDoDaoImpl:
    def __init__(self):
        getDb = GetDBUtil("todolist")
        self.db = getDb.getDB()
        self.collection_todo = self.db['todo']
        self.id = 0

    def add(self, task):
        self.collection_todo.insert_one(task)

    def rem(self, id):
        self.collection_todo.delete_one({ "id": id })

    def view(self):
        return self.collection_todo.find()
    def get(self, task):
        return self.collection_todo.find_one({"task": task})
    def getId(self):
        self.id = self.id + 1
        return self.id
    


todoDaoImpl = ToDoDaoImpl()


@app.route('/', methods=['POST', 'GET'])

def index():
    if request.method == "POST":
        content = request.form['task']
        todoDaoImpl.add({"task": content, "dateCreated": datetime.utcnow(), "id": todoDaoImpl.getId()})
        return render_template("index.html", tasks=todoDaoImpl.view())
    else:
        
        tasks = todoDaoImpl.view()
        return render_template('index.html',content=tasks)

@app.route('/delete/<string:id>')
def delete(id):
    x = todoDaoImpl.rem({"id": id})
    tasks = todoDaoImpl.view()
    return render_template("index.html", content=tasks)


@app.route('/update/<string:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        content = request.form['task']
        query = {"id": id}
        update = {"$set": {"task": content}}
        tasks = todoDaoImpl.view()
        return render_template("index.html", content=tasks)

    else:
        x = todoDaoImpl.get(id)
        render_template('update.html', tasks = x)
        


app.run(debug=True)
todoDaoImpl