from newsapi import NewsApiClient
import json
import requests

newsapi = NewsApiClient(api_key='1b60d36b8c334b68b72754f9484fdf4b')
query = input("What would you like to search for? \n")
top_headlines = newsapi.get_top_headlines(q=query,
                                          sources='rte',
                                          language='en')
headlines = json.dumps(top_headlines, indent=4, separators=(",", ";"))
print(headlines)