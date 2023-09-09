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
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=7,
        border=2
        )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(memory)
    memory.seek(0)
    base64_img = "data:image/png;base64," + base64.b64encode(memory.getvalue()).decode('ascii')
    return render_template('index.html', data=base64_img)
    

# main driver function
if __name__ == '__main__':
    app.run(debug=True)

