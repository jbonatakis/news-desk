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
from newspaper import Article
import set_key
#import pull_text

class color:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'

# # Check for api key, saved in `~/.nd_config/key` file. If doesn't exist, prompt for key and save in `~/.nd_config/key` file
# home = os.path.expanduser('~')
# try:
# 	key_file = open(home + '/.nd_config/key', 'r')
# 	key = key_file.readline()
# except FileNotFoundError:
# 	set_key.set_key()
# 	key_file = open(home + '/.nd_config/key', 'r')
# 	key = key_file.readline()

# url = ('https://newsapi.org/v2/top-headlines?country=us&apiKey=' + key)


url_list = []

class News_desk():

	def check_key(self):
		# Check for api key, saved in `~/.nd_config/key` file. If doesn't exist, prompt for key and save in `~/.nd_config/key` file
		home = os.path.expanduser('~')
		try:
			key_file = open(home + '/.nd_config/key', 'r')
			key = key_file.readline()
		except FileNotFoundError:
			set_key.set_key()
			key_file = open(home + '/.nd_config/key', 'r')
			key = key_file.readline()

		url = ('https://newsapi.org/v2/top-headlines?country=us&apiKey=' + key)
		news.get_articles(url)

	# Parse JSON and print Title, Description, and source, then get next steps from user
	def get_articles(self, url):
		data = requests.get(url).json()
		try:
			for i, article in enumerate(data['articles']):
				cprint('\n' + str(i+1) +  '. ' +  article['title'],'blue', attrs=['bold'])
				if len(str(article['description'])) < 5:# == '' or article['description'] in ['None', 'none']:
					pass
				else:
					print(article['description'])
				print('Source: ' + article['source']['name'])
				url_list.append(article['url'])
		except KeyError:
			home = os.path.expanduser('~')
			set_key.set_key()
			key_file = open(home + '/.nd_config/key', 'r')
			key = key_file.readline()
			url = ('https://newsapi.org/v2/top-headlines?country=us&apiKey=' + key)
			news.get_articles(url)

		# Prompt user for selection to determine next steps
		print(color.GREEN + color.BOLD +"\nEnter 'r' to refresh the articles, or 'q' to quit the program. \nSelect an article to read.\n" + color.END)

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
			if "-b" in sys.argv:
				try:
					if isinstance(int(selection), int):
						if int(selection) <= len(url_list) and int(selection) > 0:
							print("\n")
							news.open_link(int(selection))
							news.try_again()
						else:
							news.try_again()
				except ValueError:
					if selection in refresh:
						url_list.clear()
						news.get_articles()
					elif selection in exit:
						sys.exit(0)
					else:
						news.try_again()
			else:
				try:
					if isinstance(int(selection), int):
						if int(selection) <= len(url_list) and int(selection) > 0:
							print("\n")
							news.get_text(int(selection))
							news.try_again()
						else:
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
		selection = str(input(color.GREEN + color.BOLD +"\nPlease enter 'r' to refresh the articles, or 'q' to quit the program.\nSelect an article to read." + color.END + "\n\n>> "))
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

	def get_text(self, choice):
		if choice <= len(url_list)+1:
			counter = 0
			while counter < 1:
				#pull_text.pull_text(url_list[choice-1])
				article = Article(url_list[choice-1])
				article.download()
				article.parse()
				print(color.BLUE + color.BOLD + article.title + color.END)
				print(article.text)
				counter += 1



news = News_desk()

if __name__ == "__main__":
	news.check_key()
