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
            f.write('Author: ' + article["author"] + '\n')
            f.write(article["title"] + '\n')
            f.write(article["description"] + '\n')
            f.write(article["urlToImage"] + '\n')
            f.write('\n')
    f.close()


if __name__ == main():
    main()
