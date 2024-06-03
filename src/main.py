#!/usr/bin/python3
import pickle
import flask
app = flask.Flask(__name__)

@app.route('/')
def main():
    return flask.render_template('index.html')

@app.route('/verify', methods = ['POST'])
def verify():
    if flask.request.method == 'POST':
        f = flask.request.files['pickled'].stream.read()
        pickle.loads(f) # dont do this !!!
        return "hello"

if __name__ == "__main__":
    app.run(debug=True)