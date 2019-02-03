import fetch_news_item
import parse_output
import deliver_news


def main():
    ''' Fetches and returns top headlines for a search query and then writes the results to a JSON file. '''
    fetch_news_item.main()
    ''' Converts the output from JSON to human-readable text. '''
    parse_output.main()
    ''' Sends the resulting text file to an email address. '''
    deliver_news.main()
    return 0
