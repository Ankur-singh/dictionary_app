from flask import Flask, render_template, request
from dictionary import get_meaning
import sqlite3 as sql

app = Flask(__name__)
db = sql.connect('words.db', check_same_thread=False)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        word = request.form['word']

        try:
            pos, meaning = db.execute('select pos, meaning from words where word= ?;', (word,)).fetchall()[0]
        except:
            pos, meaning = get_meaning(word)
            db.execute('insert into words values (?, ?, ?);', (word, pos, meaning))
            db.commit()

        data = {'word': word, 'pos': pos, 'meaning': meaning}
        return render_template('index.html', data=data)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)