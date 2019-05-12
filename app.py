# movies.py

from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2019-05-12&'
       'sortBy=popularity&'
       'apiKey=afb72b362d91446999442c04aa5424d6')

@app.route('/')
def homepage():
  r = requests.get(url)
  return render_template('home.html', articles = json.loads(r.text)['articles'])

if __name__ == '__main__':
  app.run(port=8080,debug=True)