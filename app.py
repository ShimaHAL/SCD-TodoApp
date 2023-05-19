from typing import Tuple, List, Dict, Optional
from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder="templates", static_folder='static', static_url_path='')

todos: List[Dict] = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo: str = request.form.get('todo')
    todos.append({'content': todo, 'completed': False})
    print(todos)
    return redirect('/')

@app.route('/complete', methods=['POST'])
def complete():
    todo_index = int(request.form.get('index'))
    try:
        todos[todo_index]['completed'] = True
        print(todos)
    except:
        print("No TODO matched")
    return redirect('/')

if __name__ == '__main__':
    app.run(port=8080, debug=True)