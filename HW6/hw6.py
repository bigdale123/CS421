from flask import Flask, render_template, request
from markupsafe import Markup
app = Flask(__name__)

def contains_upper(password):
    result = False
    for char in password:
        if char.isupper():
            result = True
            break
    return result

def contains_lower(password):
    result = False
    for char in password:
        if char.islower():
            result = True
            break
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    password = request.args.get('pass')
    islong = len(password) >= 8
    has_lower = contains_lower(password)
    has_upper = contains_upper(password)
    endswith = password[-1].isnumeric()
    if(islong == False or has_lower == False or has_upper == False or endswith == False):
        issues = ""
        if(islong == False):
            issues += "<li><i>Be at least 8 characters long.</i></li>"
        if(has_lower == False):
            issues += "<li><i>Contain a lowercase character.</i></li>"
        if(has_upper == False):
            issues += "<li><i>Contain a uppercase character.</i></li>"
        if(endswith == False):
            issues += "<li><i>Must end in a number.</i></li>"
        return render_template('report.html',status="does not",punctuation=".",end_message=Markup("<p>Please go <a href=\"{{url_for('index.html')}}\">here</a> to try again.</p><p>The following criteria were not met:</p><ul>"+issues+"</ul>"))
    else:
        return render_template('report.html',status="does",punctuation="!",end_message=Markup("<p>Welcome to TriOpNET, you will be billed $99 monthly.</p>"))

if __name__ == '__main__':
    app.run(debug=True)
