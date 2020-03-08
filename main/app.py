import flask


app = flask.Flask(__name__)


@app.route("/")
def main():
    """
    For now, this is a flask 'hello world'
    
        example: 
        - open http://localhost:5000/ in a browser
    """
    return "Hello World!"


if __name__ == "__main__":
    app.run()
