#!/usr/bin/env python3
# Author: Jack Bonatakis
# Date: 24 May 2018
# Title: news-desk: a command line news client

import requests
import os
import json
import sys
import webbrowser
import pyperclip
from termcolor import colored, cprint

# Authenticate API. Key saved as environment variable
key = str(os.environ['NEWSAPIKEY'])

url = ('https://newsapi.org/v2/top-headlines?'
        'country=us&'
        'apiKey=' + key)

data = requests.get(url).json()

url_list = []

class News_desk():

    # Parse JSON and print Title, Description, and source, then get next steps from user
    def get_articles(self):
        for i, article in enumerate(data['articles']):
            cprint('\n' + str(i+1) +  '. Title: ' +  article['title'], attrs=['bold'])
            if len(str(article['description'])) < 5:# == '' or article['description'] in ['None', 'none']:
                pass
            else:
                print(article['description'])
            print('Source: ' + article['source']['name'])
            url_list.append(article['url'])

        # Prompt user for selection to determine next steps
        print("\nEnter 'r' to refresh the articles, or 'q' to quit the program. \nEnter an article number to open it in your browser.\n")

        choice = input('>> ')
        selection = str(choice).lower()

        # Valid input commands
        refresh = ["r", "ref", "refresh"]
        exit = ["e", "exit", "q", "quit"]

        # Call 'options' function
        news.options(selection)


    def options(self, selection):

        refresh = ["r", "ref", "refresh"]
        exit = ["e", "exit", "q", "quit"]

        while True:
            try:
                isinstance(int(selection), int)
                news.open_link(int(selection))
                news.try_again()
            except ValueError:
                if selection in refresh:
                    url_list.clear()
                    news.get_articles()
                elif selection in exit:
                    sys.exit(0)
                else:
                    news.try_again()


    # Bounces back and forth between news.options() and news.try_again() until user selects valid command. Probably a better way to do this somehow.
    # Idea: limit number of incorrect commands. After 5? 10? quit program
    def try_again(self):
        selection = str(input("\nPlease enter 'r' to refresh the articles, or 'q' to quit the program.\nEnter an article number to open it in your browser.\n\n>> "))
        news.options(selection)


    def open_link(self, choice):
        if choice <= len(url_list)+1:
            counter = 0
            while counter < 1:
                pyperclip.copy(url_list[choice-1])
                webbrowser.open_new_tab(url_list[choice-1])
                counter += 1
        else:
            news.try_again()

news = News_desk()

if __name__ == "__main__":
    news.get_articles()
