from newsapi import NewsApiClient
import json


def main():
    ''' Credential Acquisition. '''
    api_key = get_api_key()
    newsapi = get_authorization(api_key)
    ''' Prompts user for query to search for. '''
    query = get_query()
    ''' Uses the News API to search for the top headlines matching that query term. '''
    top_headlines = search_for_query(newsapi, query)
    ''' Writes the output to a JSON file. '''
    write_output(top_headlines)


def get_api_key():
    ''' Gets API key from a JSON file and returns it. API keys can be gotten for free at newsapi.org. '''
    with open("auth.json", "r") as a:
        data = json.load(a)
    return data["api_key"]


def get_authorization(api_key):
    ''' Authorizes script using API key acquired earlier and returns authorization. '''
    newsapi = NewsApiClient(api_key)
    return newsapi


def get_query():
    ''' Prompts user for query term and returns it. '''
    query = input("What would you like to search for? \n")
    return query


def search_for_query(newsapi, query):
    ''' Uses the News API to get the top headlines matching the query term, and returns those headlines. '''
    top_headlines = newsapi.get_top_headlines(
        q=query, language='en')
    return top_headlines


def write_output(headlines):
    ''' Writes the resulting headlines to a JSON file. '''
    with open('output.json', 'w') as output:
        json.dump(headlines, output)


if __name__ == main():
    main()
