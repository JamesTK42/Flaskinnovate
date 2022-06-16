from flask import Flask
from views import views
# import views from views file

app = Flask(__name__)
# we instantiate the app object

app.register_blueprint(views)
# we register the views blueprint

if __name__ == "__main__":
    app.run(debug=True, host='192.168.86.45', port=8000)
    # running app
