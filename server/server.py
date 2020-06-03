import sys
from os import getenv

from flask import Flask, make_response, request

import logging

# Setup logging to console
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log_format = logging.Formatter('%(asctime)s\t%(levelname)s: %(message)s')
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(log.level)
handler.setFormatter(log_format)
log.addHandler(handler)

app = Flask('scaffold-app')
app.config.update(DEBUG=True, ENV='development')

# Load bind-host and port from environment, or use defaults
HOST = getenv('HOST', '127.0.0.1')
PORT = int(getenv('PORT', 8080))

@app.before_first_request
def do_before():
  '''Just an example. Method doesn't do anything, but showcases lifecycle. Can be removed with no consequences.'''
  log.info('Called before first request')

@app.route('/', methods=['GET'])
def root():
  return 'Incorrect endpoint', 501

@app.route('/hello')
def hello_world():
  return make_response('Hello world')

@app.route('/post', methods=['POST'])
def post_method():
  log.info('Received raw request: %s', request.data)
  log.info('Request is JSON: %s', request.is_json)
  if request.is_json:
    log.info('Request as JSON: %s', request.json)
  return 'OK', 200


if __name__ == '__main__':
  '''Run app at configured host and port
  
  use ctrl + c to disable 
  '''
  log.info('Running server at %s %s', HOST, PORT)
  app.run(host=HOST, port=PORT)
