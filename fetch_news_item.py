from newsapi import NewsApiClient
import json
import requests


def main():
    ''' newsapi = NewsApiClient(api_key='1b60d36b8c334b68b72754f9484fdf4b') '''
    api_key= '1b60d36b8c334b68b72754f9484fdf4b'
    newsapi = get_authorization(api_key)
    query = get_query()
    source = get_source()
    top_headlines = search_for_query(newsapi, query, source)
    headlines = json.dumps(top_headlines, indent=4, separators=(",", ";"))
    print(headlines)

def get_authorization(api_key):
    newsapi = NewsApiClient(api_key)
    return newsapi

def get_query():
    query = input("What would you like to search for? \n")
    return query

def get_source():
    source = input("What source would you like to search? \n")
    return source

def search_for_query(newsapi, query, source):
    top_headlines = newsapi.get_top_headlines(q=query, sources=source, language='en')
    return top_headlines



if __name__ == main():
    main()