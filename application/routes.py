from application import app

@app.route('/', methods=["GET"])
def index():
    return 'Register Metadata'

@app.route('/mdref/<mdref>', methods=["GET"])
def getEntry(mdref):
    return 'MDRef'
