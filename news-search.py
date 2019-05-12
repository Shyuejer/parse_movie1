import requests
import json

url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2019-05-12&'
       'sortBy=popularity&'
       'apiKey=afb72b362d91446999442c04aa5424d6')

r = requests.get(url)

articles=json.loads(r.text)['articles']



for article in articles:
    print(article['author'])
#