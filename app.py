import os
import signal
from flask import Flask
from buzz import generator

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
    page = '<html><body><h1>'
    page += generator.generate_buzz()
    page += "<hr>"
    page += "Fuck yeah!! it works!!"
    page += "<hr>"
    page += "<a href 'https://www.upwork.com/freelancers/~01a6738208d8e81707'>Hire me<hr>"

    page += '</h1></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT')) # port 5000 is the default


