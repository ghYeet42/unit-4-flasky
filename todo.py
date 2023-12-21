from flask import Flask, render_template, request


todolist = ["sleep", "scoot", "griddy"]

######

app = Flask(__name__)

######

@app.route("/", methods = ["GET", "POST"])
def index():

    newTodo = request.form["newTodo"]

    todolist.append(newTodo)

    return render_template ("todo.html.jinja", my2dolist = todolist )
    

    return ("This my 2dos...!")

    # return ("<p style=\"color:red;\">Hello!</p>")