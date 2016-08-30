from flask import Flask, render_template, request
import os
import requests
app = Flask(__name__)


# Lab Exercise 3 Solution 1/2
def get_room_memberships(roomId):
    url = os.getenv("SPARK_URL") + '/memberships?roomId={}'.format(roomId)
    token = os.getenv("SPARK_TOKEN")
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {}'.format(token)}
    resp = requests.get(url, headers=headers)
    return resp.json()['items']


def get_rooms():
    """
    calling this function should return a list of rooms in json format.

    :return: list
        """

    # Lab Exercise 1 solution
    url = os.getenv("SPARK_URL") + '/rooms'
    token = os.getenv("SPARK_TOKEN")
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {}'.format(token)}
    return requests.get(url, headers=headers).json()['items']



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
        for room in rooms:
            room['members'] = len(get_room_memberships(room['id']))
        return render_template('rooms.html', rooms=rooms)


if __name__ == '__main__':
    app.run(debug=True)
