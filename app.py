from flask import Flask, render_template, request
import os
import requests
app = Flask(__name__)
import socket




def get_members(roomid):
    token = os.environ['SPARK_TOKEN']
    auth = "Bearer %s" % token
    url = os.environ['SPARK_URL'] + '/memberships'
    headers = {
        'content-type': "application/json",
        'authorization': auth,
    }
    params = {'roomId': roomid
    }

    response = requests.get(url, headers=headers, params=params).json()
    memberCount = len(response['items'])

    return memberCount

def get_rooms():
    """
    calling this function should return a list of rooms in json format.

    :return: list
        """

    # your code goes here

    token = os.environ['SPARK_TOKEN']
    auth = "Bearer %s" % token
    url = os.environ['SPARK_URL'] + '/rooms'
    headers = {
        'content-type': "application/json",
        'authorization': auth
    }

    response = requests.get(url, headers=headers).json()

    rooms = response['items']



    #for room in rooms:
    #    room['memberCount'] = str(get_members(str(room['id'])))

    return rooms


#@app.route('/')
def hello():
    #return "Hello, World!"
    return render_template('index.html', text="Hello World!")

@app.route('/', methods=['GET','POST'])
def rooms():
    hostname = socket.gethostname()
    if request.method == 'GET':
        rooms = get_rooms() or []
        return render_template('rooms.html', rooms=rooms, hostname=hostname)
    elif request.method == 'POST':
        rooms = get_rooms() or []
        return render_template('rooms.html', rooms=rooms, hostname=hostname)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
