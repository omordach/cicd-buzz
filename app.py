import os
#import signal
from flask import Flask, render_template
from buzz import generator

app = Flask(__name__)

@app.route("/")
def generate_buzz():
    buzz = generator.generate_buzz()
    return render_template('index.html', buzz=buzz)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
