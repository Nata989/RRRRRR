# Тянем из инета

import requests
import json
from flask import Flask

#text = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text

#valutes=json.loads(text)
#print(c)

#for val in valutes ['Valute']:
 #print(val)

# Выводим Flask
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!<h1>"

if __name__ == "__main__":
    app.run()