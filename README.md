# News Desk

A small program that lets you browse news through the command line.

![news-desk](https://raw.githubusercontent.com/jbonatakis/news-desk/master/images/news-desk-screenshot.png)


### Requirements

* Python 3.3 or higher
* pyperclip 
* termcolor

These requirements can be installed together by running 

`pip install -r requirements.txt`

or 

`pip3 install -r requirements.txt` 

depending on your system. As stated above, this program requires Python 3.3 or greater.

### Getting Started

First, clone the repository:

`git clone https://github.com/jbonatakis/news-desk.git`

Then, register and get a (free) API key from: [https://newsapi.org/](https://newsapi.org/)

Save the API key as an environment variable named `NEWSAPIKEY`

`echo 'export NEWSAPIKEY=<your key>' >> ~/.bashrc && source ~/.bashrc`

Alternately, replace this line in the script:

`key = str(os.environ['NEWSAPIKEY'])`

with this line:

`key = "<your key>"`

Finally, run:

`python3 news_desk.py`

### Features

* News Desk grabs top headlines from all major U.S. news outlets
* To open an article, type the article number and press `Enter`
  * Note: this will also copy the article URL to your cliboard. Some websites, such as the New York Times and Washington Post, have soft paywalls. If the article is opened in your browser's incognito or safe mode, you can effectively avoid the paywall and access the article.
* Type `r` or `refresh` to update the list of articles. This command is not case sensitive.
* To exit the program and return to your command line, type `e`, `exit`, `q`, or `quit`. Again, this is not case sensitive.


### Contributing

If you would like to contribute to the project, feel free to open a pull request and I will review it as soon as possible.
