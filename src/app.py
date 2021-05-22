import time

import redis
from flask import (Flask, render_template)

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    message = 'Hello {}! I have been seen {} times.\n'.format(app.config['SECRET_KEY'], count)
    return render_template('index.html', message = message)

