from flask import Flask, render_template, url_for
from browser import driver, ready_button, start_button, save_button, print_button, receive_button
app = Flask(__name__)


@app.route('/')
def index():    
    return render_template('menu.html')

@app.route('/ready')
def ready():    
    ready_button.click()
    return render_template('menu.html')

@app.route('/start')
def start():    
    start_button.click()
    return render_template('menu.html')

@app.route('/save')
def save():    
    save_button.click()
    return render_template('menu.html')

@app.route('/print')
def print_scores():    
    print_button.click()
    return render_template('menu.html')

@app.route('/receive')
def receive():
    receive_button.click()
    return render_template('menu.html')

if __name__ == '__main__':
    # app.debug = True
    app.run(host="0.0.0.0")
