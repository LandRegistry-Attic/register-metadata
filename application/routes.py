from application import app, db
from application.models import mdref

from .utils import get_cre_info

import json

@app.route('/', methods=["GET"])
def index():
    return 'Register Metadata'

@app.route('/mdref/<md_ref>', methods=["GET"])
def getEntry(md_ref):
    cre_entry_info = json.dumps(get_cre_info(md_ref))
    return cre_entry_info
