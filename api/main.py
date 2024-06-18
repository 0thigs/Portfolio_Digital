from flask import Flask, render_template, url_for

dir_template_folder = 'templates/'
dir_static_folder = "static/"

app = Flask(__name__, template_folder=dir_template_folder, static_folder=dir_static_folder)


@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/projects")
def projects():
        
        academicProjects = [
    {
        "title": "StarDust",
        "image": url_for('static', filename='/images/card(5).png'),
        "link": "https://github.com/0thigs/StarDust",
        "description": "A mobile application for learning programming logic.",
    },
    {
        "title": "Smart Farm",
        "image": url_for('static', filename='/images/card(8).png'),
        "link": "https://github.com/ctrI-Alt-Del/smart-farming/",
        "description": "A web application that helps monitoring a smart greenhouse.",
    },
    {
        "title": "Youtube Music Clone",
        "image": url_for('static', filename='/images/card(4).png'),
        "link": "https://github.com/0thigs/Youtube_music",
        "description": "A Youtube music UI Clone to listen your favorite musics.",
    },
]   
    
        personalProjects = [
    {
        "title": "Opportunity",
        "image": url_for('static', filename='/images/card(7).png'),
        "link": "https://github.com/0thigs/Opportunity",
        "description": "A website that aims to provides information about general oportunities."
    },
    {
        "title": "Pokedéx",
        "image": url_for('static', filename='/images/card(6).png'),
        "link": "https://github.com/0thigs/Pokedex-App",
        "description": "A Pokedex application to see your favorite pokemon stats."
    },
    {
        "title": "ChatApp",
        "image": url_for('static', filename='/images/card(1).png'),
        "link": "https://github.com/0thigs/ChatApp",
        "description": "A web chat app used to meet new people."
    },
    {
        "title": "DevLinks",
        "image": url_for('static', filename='/images/card(2).png'),
        "link": "https://github.com/0thigs/DevLinks",
        "description": "A social media links agragator."
    },
    {
        "title": "Github Finder",
        "image": url_for('static', filename='/images/card(3).png'),
        "link": "https://github.com/0thigs/Github-Profile-Finder",
        "description": "A web app to search profiles on Github."
    },
      {
        "title": "Rock Papper Scissor",
        "image": url_for('static', filename='/images/card(9).png'),
        "link": "https://github.com/0thigs/Rock-Papper-Scissor",
        "description": "A rock papper scissor web game to have a little fun."
    },
]
    
        return render_template("projects.html", academicProjects=academicProjects ,personalProjects=personalProjects)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)