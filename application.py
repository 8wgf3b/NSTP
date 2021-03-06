from flask import Flask, request, Response
from utils import clean
from reddit import reddit_user_media, useranalysis, subredditanalysis
import os
import requests
import json


application = app = Flask(__name__)

@app.route('/small', methods=['POST', 'GET'])
def api():
    try:
        if request.method == 'POST':
            js = request.get_json()
            if js['func'] == '/clam':
                mess = {'result':clean(log=True)}
                return json.dumps(mess)
            elif js['func'] == '/rumz':
                mess = {'result':reddit_user_media(js['param'])}
                return json.dumps(mess)
            elif js['func'] == '/ruseran':
                mess = {'result':useranalysis(*js['param'])}
                return json.dumps(mess)
            elif js['func'] == '/rsuban':
                mess = {'result':subredditanalysis(*js['param'])}
                return json.dumps(mess)
    except Exception as e:
        print(e)
        return Response('ok', status=200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
