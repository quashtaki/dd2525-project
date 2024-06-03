#!/usr/bin/python3
import pickle
import flask
import hmac
import hashlib
app = flask.Flask(__name__)


@app.route('/')
def main():
    return flask.render_template('index.html')

@app.route('/verify', methods = ['POST'])
def verify():
    if flask.request.method == 'POST':
        digest, f = flask.request.files['pickled'].stream.read().split(b' ', 1) # borrowed from https://pycharm-security.readthedocs.io/en/latest/checks/PIC100.html
        expected_digest = hmac.new(b'mykey', f, hashlib.sha256).digest()
        if (hmac.compare_digest(digest, expected_digest)):
            pickle.loads(f)
            return "hello"
        else:
            return "the pickle needs to be signed with a trusted key"
         # dont do this !!!
        

if __name__ == "__main__":
    app.run(debug=True)