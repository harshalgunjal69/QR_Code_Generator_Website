#importing the modules
from flask import Flask, render_template, request
import qrcode
from io import BytesIO
import base64

#initializing the flask app
app = Flask(__name__)

#default route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def generateQR():
    memory=BytesIO()
    data = request.form.get('dataQR')
    img = qrcode.make(data)
    img.save(memory)
    memory.seek(0)
    base64_img = "data:image/png;base64," + base64.b64encode(memory.getvalue()).decode('ascii')
    return render_template('index.html', data=base64_img)
    

# main driver function
if __name__ == '__main__':
    app.run(debug=True)

