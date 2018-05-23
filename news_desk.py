import requests
import os
import json

# Authenticate API. Key saved as environment variable

url = ('https://newsapi.org/v2/top-headlines?'
        'country=us&'
        'apiKey=' + str(os.environ['NEWSAPIKEY']))

data = requests.get(url).json()


for i, article in enumerate(data['articles']):
    print('\n' + str(i+1) +  '. Title: ' +  article['title'])
    print(article['description'])
    print('Link: ' + article['url'])

