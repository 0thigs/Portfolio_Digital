from flask import Flask, render_template, url_for

dir_template_folder = 'templates/'
dir_static_folder = "static/"

app = Flask(__name__, template_folder=dir_template_folder, static_folder=dir_static_folder)

@app.route("/")
def homepage():
    return render_template("homepage.html")

if __name__ == "__main__":
    app.run(debug=True)