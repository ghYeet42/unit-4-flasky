from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors
from pprint import pprint as print


con = pymysql.connect(
    database = "cscarlett_todosah",
    user = "cscarlett",
    password = "228941274",
    host = "10.100.33.60",
    cursorclass = pymysql.cursors.DictCursor
)

todolist = ["sleep", "scoot", "griddy"]

######

app = Flask(__name__)

######

@app.route("/", methods = ["GET", "POST"])
def index():

    cursor = con.cursor()

    cursor.execute("SELECT `description` FROM `todosah`")

    results = cursor.fetchall()

    print(results)

    if request.method == "POST":

        newTodo = request.form["new2do"]

        todolist.append(newTodo)


    #for todosDescripton in results:
    #    print(todosDescripton...)

    return render_template ("todo.html.jinja", my2dolist = results)
    
    return ("This my 2dos...!")

    # return ("<p style=\"color:red;\">Hello!</p>")


@app.route("/delete/<int:todoIndex>", methods = ["POST"])
def todoDel(todoIndex):

    del todolist[todoIndex]

    return redirect("/")
