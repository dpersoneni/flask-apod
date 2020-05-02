from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__, template_folder="templates")

@app.route('/', methods=['POST', 'GET'])
def home():
    r = requests.get('https://api.nasa.gov/planetary/apod?api_key=WiRrKZ0Dih8M9Wzh6q7Qms80x9cotsPfzSu71RM6&hd=True')
    obj = r.json()
    title = obj["title"]
    url = obj["url"]
    description = obj["explanation"]
    return render_template('template.html', title = title, url = url, description = description)

@app.route('/day', methods=['POST', 'GET'])
def day():
    if request.method=='POST':
        day = request.form['day']
        date_changed = day.split('-')
        date_changed = date_changed[::-1]
        date_changed  = '/'.join(date_changed)
        r = requests.get('https://api.nasa.gov/planetary/apod?api_key=WiRrKZ0Dih8M9Wzh6q7Qms80x9cotsPfzSu71RM6&hd=True&date='+ day)
        obj = r.json()
        title = obj["title"]
        url = obj["url"]
        description = obj["explanation"]
        return render_template('day.html', title = title, url = url, description = description, date_changed=date_changed)
    
   



if __name__=="__main__":
    app.run(debug=True)
