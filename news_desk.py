# Author: Jack Bonatakis
# Date: 24 May 2018
# Title: news-desk: a command line news client

import requests
import os
import json
import sys

# Authenticate API. Key saved as environment variable
key = str(os.environ['NEWSAPIKEY'])

url = ('https://newsapi.org/v2/top-headlines?'
        'country=us&'
        'apiKey=' + key)

data = requests.get(url).json()

class News_desk():

    # Parse JSON and print Title, Description, and URL, then get next steps from user
    def get_articles(self):
        for i, article in enumerate(data['articles']):
            print('\n' + str(i+1) +  '. Title: ' +  article['title'])
            print(article['description'])
            print('Link: ' + article['url'])

        # Prompt user for selection to determine next steps
        print("\nEnter 'r' to refresh the articles, or 'q' to quit the program \n")

        selection = str(input('>> ')).lower()

        # Valid input commands
        refresh = ["r", "ref", "refresh"]
        exit = ["e", "exit", "q", "quit"]

        # Call 'options' function
        news.options(selection)


    def options(self, selection):

        refresh = ["r", "ref", "refresh"]
        exit = ["e", "exit", "q", "quit"]

        while True:
            if selection in refresh:
                news.get_articles()
            elif selection in exit:
                sys.exit(0)
            else:
                news.try_again()


    # Bounces back and forth between news.options() and news.try_again() until user selects valid command. Probably a better way to do this somehow.
    # Idea: limit number of incorrect commands. After 5? 10? quit program
    def try_again(self):
        selection = str(input("\nThat is not a valid command. Please enter 'r' to refresh the articles, or 'q' to quit the program\n\n>> "))
        news.options(selection)

news = News_desk()

if __name__ == "__main__":
    news.get_articles()





