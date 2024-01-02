from flask import Flask, render_template, request, redirect


todolist = ["sleep", "scoot", "griddy"]

######

app = Flask(__name__)

######

@app.route("/", methods = ["GET", "POST"])
def index():

    if request.method == "POST":

        newTodo = request.form["new2do"]

        todolist.append(newTodo)


    return render_template ("todo.html.jinja", my2dolist = todolist)
    
    return ("This my 2dos...!")

    # return ("<p style=\"color:red;\">Hello!</p>")


@app.route("/delete/<int:todoIndex>", methods = ["POST"])
def todoDel(todoIndex):

    del todolist[todoIndex]

    return redirect("/")