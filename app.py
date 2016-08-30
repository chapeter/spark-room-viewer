from flask import Flask, render_template, request
import os
import requests
app = Flask(__name__)

def get_rooms():
    """
    calling this function should return a list of rooms in json format.

    :return: list
        """

    # your code goes here

    pass


@app.route('/')
def hello():
    # Intro Exercise Solution

    #return "Hello, World!"
    return render_template('index.html', text='Hello, World')


@app.route('/rooms', methods=['GET','POST'])
def rooms():
    if request.method == 'GET':
        return render_template('rooms.html')
    elif request.method == 'POST':
        rooms = get_rooms() or []
        return render_template('rooms.html', rooms=rooms)


if __name__ == '__main__':
    app.run(debug=True)
