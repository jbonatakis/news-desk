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
