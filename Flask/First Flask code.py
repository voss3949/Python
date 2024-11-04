import os
from flask import Flask, render_template

template_dir = os.path.abspath('C:/Users/12245/OneDrive/Documents/Python_Projects/MyDashboard/')

app = Flask(__name__, template_folder=template_dir)
Name = 'Joshua'

@app.route("/")
def homepage():
    return render_template("index.html", name=Name)


if __name__ == "__main__":
	app.run(port=5000)
