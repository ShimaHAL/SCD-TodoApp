from typing import List, Optional

from flask import Flask, redirect, render_template, request

app = Flask(
    __name__, template_folder="templates", static_folder="static", static_url_path=""
)


class Todo:
    content: str
    completed: bool

    def __init__(self, content: str):
        self.content = content
        self.completed = False

    def complete(self):
        self.completed = True

    def to_dict(self):
        return {"content": self.content, "completed": self.completed}


todos: List[Todo] = []


@app.route("/")
def index():
    return render_template(
        "index.html", todos=list(map(lambda todo: todo.to_dict(), todos))
    )


@app.route("/add", methods=["POST"])
def add():
    content: Optional[str] = request.form.get("todo")

    if content is not None:
        todo = Todo(content=content)
        todos.append(todo)
    else:
        print("No content provided")
    print(todos)
    return redirect("/")


@app.route("/complete", methods=["POST"])
def complete():
    index: Optional[str] = request.form.get("index")
    if index is not None:
        todo_index = int(index)
        try:
            todos[todo_index].complete()
            print(todos)
        except Exception:
            print("No TODO matched")
    else:
        print("No index provided")

    return redirect("/")


if __name__ == "__main__":
    app.run(port=8080, debug=True)
