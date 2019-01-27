import json


def main():
    data = read_from_output()
    try:
        write_to_output(data)
    except TypeError:
        with open("output.txt", "w") as f:
            f.write("No results found.")


def read_from_output():
    with open("output.json", "r") as f:
        data = json.load(f)
    return data


def write_to_output(data):
    with open('output.txt', 'w') as f:
        for article in data["articles"]:
            try:
                f.write('Author: ' + article["author"] + '\n')
            except:
                f.write('Unable to find author of this article. \n')
            try:
                f.write('Source: ' + article["source"]["name"] + '\n')
            except:
                f.write('Unable to find source of this article. \n')
            f.write(article["title"] + '\n')
            f.write(article["description"] + '\n')
            try:
                f.write(article["urlToImage"] + '\n')
            except:
                print('')
            f.write('\n')
    f.close()


if __name__ == main():
    main()
