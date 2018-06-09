# News Desk

A small program that lets you read news through the command line.

![news-desk](https://raw.githubusercontent.com/jbonatakis/news-desk/master/images/news-desk-6-9-2018-1.png)
![news-desk](https://raw.githubusercontent.com/jbonatakis/news-desk/master/images/news-desk-6-9-2018-2.png)
![news-desk](https://raw.githubusercontent.com/jbonatakis/news-desk/master/images/news-desk-6-9-2018-3.png)


### Requirements

* Python 3.3 or higher
* pyperclip 
* termcolor
* newspaper3k

These requirements can be installed together by running 

`pip install -r requirements.txt`

or 

`pip3 install -r requirements.txt` 

depending on your system. As stated above, this program requires Python 3.3 or greater.

### Getting Started

First, clone the repository:

`git clone https://github.com/jbonatakis/news-desk.git`

Then, register and get a (free) API key from: [https://newsapi.org/](https://newsapi.org/)

Run the program:

`python3 news_desk.py`

This will prompt you to enter your API key, which will be saved in a file named `key` located in the `~/.nd_config/` directory and read to validate your access to the API each time News Desk is run.

### Features

* News Desk grabs top headlines from all major U.S. news outlets
* To view an article, type the article number and press `Enter`. This will print out the article text on the command line.
* Type `r` or `refresh` to update the list of articles. This command is not case sensitive.
* To exit the program and return to your command line, type `e`, `exit`, `q`, or `quit`. Again, this is not case sensitive.

* If you run the program with the flag `-b`, then selecting an article will open it in the browser and copy the article URL to your clipboard.

### Contributing

If you would like to contribute to the project, feel free to open a pull request and I will review it as soon as possible.
