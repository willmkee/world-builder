from flask import Flask, render_template
import csv
import random

app = Flask(__name__)

def roll_dice():
    return [random.randint(1, 6) for _ in range(3)]

def find_sentence(rolls, data):
    rolls_str = ''.join(map(str, rolls))
    for row in data:
        if row[0] == rolls_str:
            return row[1]
    return "Sentence not found for rolls: {}".format(rolls_str)

@app.route('/')
def index():
    # Replace 'your_file.csv' with the actual path to your CSV file
    file_path = 'world-events.csv'

    # Read CSV file
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)

    # Roll three six-sided dice
    rolls = roll_dice()

    # Find the corresponding sentence
    sentence = find_sentence(rolls, data)

    return render_template('index.html', rolls=rolls, sentence=sentence)

if __name__ == '__main__':
    app.run(debug=True)
