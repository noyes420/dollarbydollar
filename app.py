from flask import Flask, render_template

app = Flask(__name__)

app.secret_key = "0123456789876543210"

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/about')
def about_page():
    return render_template('about.html', page_title='Dollar By Dollar - About Us')

@app.route('/resources')
def resources_page():
    return render_template('resources.html')

@app.route('/team')
def team_page():
    return render_template('team.html', page_title='Dollar By Dollar - Our Team')


