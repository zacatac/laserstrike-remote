from flask import Flask, render_template, url_for, redirect
from browser import driver, Keys, ready_button, start_button, save_button, print_button, receive_button, abort_button, wait, EC, By
from browser import StaleElementReferenceException, ElementNotVisibleException, UnexpectedAlertPresentException
app = Flask(__name__)

buttons = {
    'ready':ready_button,
    'start':start_button,
    'print':print_button,
    'receive':receive_button,
    'save':save_button,
    'abort':abort_button
}

name = "none"

def visible_buttons(buttons):
    visible = {}
    for key in buttons.keys():
        try:
            visible[key] = buttons[key].is_displayed()
        except StaleElementReferenceException:
            visible[key] = False
            try:
                buttons[key] = driver.find_element_by_id("%sbutton" % key)
            except ElementNotVisibleException:
                pass
    return visible
    
@app.route('/')
def index():   
    global name 
    time = driver.find_element_by_id("gametime").text
    num = driver.find_element_by_id("gamenumber").text
    return render_template('index.html', time=time, num=num, name=name, **visible_buttons(buttons))

@app.route('/ready')
def ready():    
    buttons["ready"].click()
    wait.until(EC.visibility_of(buttons["start"]))
    return redirect(url_for('index'))

@app.route('/start')
def start():    
    buttons["start"].click()
    wait.until(EC.invisibility_of_element_located((By.ID, 'startbutton')))
    return redirect(url_for('index'))

@app.route('/save')
def save():    
    buttons["save"].click()
    wait.until(EC.visibility_of(buttons["ready"]))
    return redirect(url_for('index'))

@app.route('/print')
def print_scores():    
    buttons["print"].click()
    wait.until(EC.alert_is_present())
    alert = driver.switch_to_alert()
    alert.accept()    
    return redirect(url_for('index'))

@app.route('/receive')
def receive():
    buttons["receive"].click()
    try:
        wait.until(EC.visibility_of(buttons["ready"]))
    except UnexpectedAlertPresentException:
        alert = driver.switch_to_alert()
        alert.accept()
        try:
            wait.until(EC.visibility_of(buttons["ready"]))
        except  StaleElementReferenceException:
            buttons["ready"] = driver.find_element_by_id("readybutton")
            wait.until(EC.visibility_of(buttons["ready"]))
    driver.find_element_by_id("editbutton").click()
    wait.until(EC.presence_of_element_located((By.ID,"VEST1")))
    global name
    name = driver.find_element_by_id("VEST1").get_attribute("value")
    driver.back()
    try:
        wait.until(EC.visibility_of(buttons["ready"]))
    except  StaleElementReferenceException:
        buttons["ready"] = driver.find_element_by_id("readybutton")
        wait.until(EC.visibility_of(buttons["ready"]))
    return redirect(url_for('index'))

@app.route('/abort')
def abort():
    buttons["abort"].click()
    wait.until(EC.visibility_of(buttons["save"]))
    wait.until(EC.invisibility_of_element_located((By.ID, 'savebutton')))
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    # app.debug = True
    # app.run()
    app.run(host="0.0.0.0")
