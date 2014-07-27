from flask import Flask, render_template, url_for, redirect
from browser import driver, Keys, ready_button, start_button, save_button, print_button, receive_button, abort_button, wait, EC, By
app = Flask(__name__)

buttons = {
    'ready':ready_button.is_displayed,
    'start':start_button.is_displayed,
    'printb':print_button.is_displayed,
    'receive':ready_button.is_displayed,
    'save':save_button.is_displayed,
    'abort':abort_button.is_displayed
}

local_buttons = {    
    'ready':ready_button.is_displayed,
    'start':start_button.is_displayed,
    'printb':print_button.is_displayed,
    'receive':ready_button.is_displayed,
    'save':save_button.is_displayed,
    'abort':abort_button.is_displayed
}

def visible_buttons(buttons):
    visible = {}
    for key in buttons.keys():
        visible[key] = buttons[key]()
    return visible
    
@app.route('/')
def index():    
    return render_template('index.html', **visible_buttons(buttons))

@app.route('/ready')
def ready():    
    ready_button.click()
    wait.until(EC.visibility_of(start_button))
    return redirect(url_for('index'))

@app.route('/start')
def start():    
    start_button.click()
    wait.until(EC.invisibility_of_element_located((By.ID, 'startbutton')))
    return redirect(url_for('index'))

@app.route('/save')
def save():    
    print('saving')
    save_button.click()
    wait.until(EC.visibility_of(ready_button))
    return redirect(url_for('index'))

@app.route('/print')
def print_scores():    
    print_button.click()
    wait.until(EC.alert_is_present())
    alert = driver.switch_to_alert()
    alert.accept()    
    return redirect(url_for('index'))

@app.route('/receive')
def receive():
    receive_button.click()
    wait.until(EC.visibility_of(ready_button))
    return redirect(url_for('index'))

@app.route('/abort')
def abort():
    abort_button.click()
    wait.until(EC.visibility_of(save_button))
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    # app.debug = True
    # app.run()
    app.run(host="0.0.0.0")
