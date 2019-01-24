from newsapi import NewsApiClient
import json
import requests


def main():
    api_key = get_api_key()
    newsapi = get_authorization(api_key)
    query = get_query()
    source = get_source()
    top_headlines = search_for_query(newsapi, query, source)
    write_output(top_headlines)


def get_api_key():
    with open("auth.json", "r") as a:
        data = json.load(a)
    return data["api_key"]


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
    top_headlines = newsapi.get_top_headlines(
        q=query, sources=source, language='en')
    return top_headlines


def write_output(headlines):
    with open('output.json', 'w') as output:
        json.dump(headlines, output)


if __name__ == main():
    main()
