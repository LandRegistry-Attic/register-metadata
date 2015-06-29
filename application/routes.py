from application import app

from .utils import get_cre_info

@app.route('/', methods=["GET"])
def index():
    return 'Register Metadata'

@app.route('/mdref/<mdref>', methods=["GET"])
def getEntry(mdref):
    cre_entry_info = get_cre_info(mdref)
    return cre_entry_info
