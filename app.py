#importing the modules
from flask import Flask, render_template
import qrcode

#initializing the flask app
app = Flask(__name__)

#default route
@app.route('/')
def index():
    return render_template('index.html')

# main driver function
if __name__ == '__main__':
    app.run()

