from flask import render_template, Blueprint, request

views = Blueprint("views", __name__)

# view  in this instance is a blueprint
task_list = []


@views.route("/")
def home():
    return render_template("index.html")


@views.route("/about")
def about():
    return render_template("about.html")


@views.route("/contact")
def contact():
    return render_template("contact.html")


@views.route("/shop")
def shop():
    return render_template("shop.html")


@views.route("/doodles")
def doodles():
    return render_template("doodles.html")


@views.route("/todo", methods=["POST", "GET"])
def todo():
    if request.method == "POST":
        task = request.form.get("task-input")
        task_list.append(task)
        print(task_list)
        return render_template("todo.html", task_list=task_list)
    return render_template("todo.html")


@views.route("/admin")
def admin():
    return render_template("admin.html")
