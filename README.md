# News Desk

A small program that lets you read news through the command line.

To run the program, you'll need to get a (free) API key from: https://newsapi.org/

Then save the API key as an environment variable named `NEWSAPIKEY`

`echo 'export NEWSAPIKEY=<your key>' >> ~/.bashrc && source ~/.bashrc`

Alternately, replace this line in the script:

`key = str(os.environ['NEWSAPIKEY'])`

with this line:

`key = <your key>`

### Requirements:

* Python 3.5.2 or higher
* pyperclip 1.6.1


### Features

* News Desk grabs top headlines from all major U.S. news outlets
* To open an article, type the article number and press `Enter`
*Note: this will also copy the article URL to your cliboard. Some websites, such as the New York Time and Washington Post, have soft paywalls. If the article is opened in your browser's incognito or safe mode, you can effectively avoid the paywall and access the article.
* Type `r` or `refresh` to update the list of articles. This command is not case sensitive.
* To exit the program and return to your command line, type `e`, `exit`, `q`, or `quit`. Again, this is not case sensitive.


### Contributing

If you would like to contribute to the program, feel free to open a pull request and I will review it as soon as possible.
