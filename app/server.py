from flask import Flask, request

app = Flask(__name__)


def wordcount(file):
    # create a file for writing
    with open('output/result.txt', 'a') as f:
        word_disc = {}
        for line in file:
            # clean word if they include a special character
            word_list = [x.strip("()\":,\n.") for x in line.split(" ")]
            for word in word_list:
                if word in word_disc:
                    word_disc[word] += 1
                else:
                    word_disc[word] = 1
        for word, count in word_disc.items():
            if len(word) > 0:
                f.write(f"{word}\t{count}\n")


@app.route('/file', methods=['POST'])
def upload_file():
    # check if path params exists
    if 'path' in request.json:
        path = request.json['path']
        with open(path, 'r') as f:
            wordcount(f)
    return {"response": "ok"}


if __name__ == "__main__":
    # Start the app
    app.run(host='localhost', debug = True) 
