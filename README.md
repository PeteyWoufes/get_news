# get_news

A Python program that fetches news about a topic from the internet using the News API (https://newsapi.org/), writes the news it finds to a JSON file, converts that JSON to a human-readable text file, and then emails a target user using the Gmail API with that text file as the body text.

## Installation

To use this program you will need to provide a few things:
* A News API key, obtainable for free at https://newsapi.org.
* A Gmail address to send emails from, which you can create for free at https://accounts.google.com/signup.
* Gmail API credentials, which you can get by using the wizard at https://developers.google.com/gmail/api/quickstart/python.

To work with the source code provided you will also need to install some modules. You can do this by entering the following command into your Python interpreter:
```Python
pip install -r requirements.txt
```
This will install all the required modules.
Once all of this is done you can use the script by running get_news.py: this is the only script you need to run.

## License

This program is licenced under the MIT License. In short, all I require is that you preserve the copyright and license notices in this code. You can do whatever you want with it and you are not obligated to publish your improvements upstream, however, it would be greatly appreciated!

## Acknowledgements

I want to thank the collective brainpower of the internet for helping me put this together. Any problems I had I was able to solve using years-old Stack Overflow threads and API documentation. I made this script to test and improve my programming skills, and I learnt a lot making it, but I couldn't have done it without the wisdom of those who have gone before. Okay, pretentious thing over now. Finally, I want to thank you for checking this out, it means a lot!