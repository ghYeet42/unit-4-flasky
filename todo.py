from flask import Flask, render_template, request, redirect, jsonify
import pymysql
import pymysql.cursors
from pprint import pprint as print


con = pymysql.connect (
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

    if request.method == "POST":

        newTodo = request.form["new2do"]

        todolist.append(newTodo)

        cursor = con.cursor()

        cursor.execute(f"INSERT INTO `todosah` (`description`) VALUES ('{newTodo}')")

        cursor.close()

        con.commit()


    cursor = con.cursor()

    cursor.execute("SELECT * FROM `todosah` ORDER BY `complete`")

    results = cursor.fetchall()

    cursor.close()

    return render_template ("todo.html.jinja", my2dolist = results)
    
    return ("This my 2dos...!")

    # return ("<p style=\"color:red;\">Hello!</p>")

@app.route("/completedTodo/<int:todoIndex>", methods = ["POST"])
def todoCompleted(todoIndex):
     
    cursor = con.cursor()

    cursor.execute(f"UPDATE `todosah` SET `complete` = 1 WHERE `id` = {todoIndex}")

    cursor.close()

    con.commit()


    return redirect("/")


@app.route("/delete/<int:todoIndex>", methods = ["POST"])
def todoDel(todoIndex):
    cursor = con.cursor()

    cursor.execute(f"DELETE FROM `todosah` WHERE `id` = {todoIndex}")

    cursor.close()

    con.commit()

    # del todolist[todoIndex]

    return redirect("/")