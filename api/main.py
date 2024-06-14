from flask import Flask, render_template, url_for

dir_template_folder = 'templates/'
dir_static_folder = "static/"

app = Flask(__name__, template_folder=dir_template_folder, static_folder=dir_static_folder)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/projects")
def projects():
    allProjects = [
    {
        "title": "Youtube Music Clone",
        "image": url_for('static', filename='/images/card(4).png'),
        "link": "https://github.com/0thigs/Youtube_music"
    },
    {
        "title": "StarDust",
        "image": url_for('static', filename='/images/card(5).png'),
        "link": "https://github.com/0thigs/StarDust",
    },
    {
        "title": "Pokedéx",
        "image": url_for('static', filename='/images/card(6).png'),
        "link": "https://github.com/0thigs/Pokedex-App",
    },
    {
        "title": "ChatApp",
        "image": url_for('static', filename='/images/card(1).png'),
        "link": "https://github.com/0thigs/ChatApp",
    },
    {
        "title": "DevLinks",
        "image": url_for('static', filename='/images/card(2).png'),
        "link": "https://github.com/0thigs/DevLinks",
    },
    {
        "title": "Github Finder",
        "image": url_for('static', filename='/images/card(3).png'),
        "link": "https://github.com/0thigs/Github-Profile-Finder",
    }
    ]
    return render_template("projects.html", allProjects=allProjects)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)