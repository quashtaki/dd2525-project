#!/usr/bin/python3
#import pickle
import flask
import json
app = flask.Flask(__name__)


@app.route('/')
def main():
    return flask.render_template('index.html')

@app.route('/verify', methods = ['POST'])
def verify():
    if flask.request.method == 'POST':
        f = flask.request.files['pickled'].stream.read()
        myobject = json.loads(f)
        #pickle.loads(f) # dont do this !!!
        return myobject

if __name__ == "__main__":
    app.run(debug=True)