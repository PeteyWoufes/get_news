import json


def main():
    read_from_output()

def read_from_output():
    with open ("output.json", "r") as f:
        data = json.load(f)
    with open('output.txt', 'w') as f:
        for article in data["articles"]:
            f.write('Author: ' + article["author"] + '\n')
            f.write(article["title"] + '\n')
            f.write(article["description"] + '\n')
            f.write(article["urlToImage"] + '\n')
            f.write('\n')
    f.close()

if __name__ == main():
    main()



