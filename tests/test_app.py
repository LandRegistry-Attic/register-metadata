import unittest
import json
import os

from application import app

submission_ref = "ZYX9873"
case_data = '{ "dateReceived": "1993-11-01T12:00:00Z", "submissionRef": "' + submission_ref + '", "keyNumber": "KEY3243", "amountPaid": "12000", "lender": "GE Money Home Finance Limited", "mortgageDate": "1993-08-13T12:00:00Z", "titleNumber": "DN503122", "borrower": "", "propertyDetails": "", "emdref": ""}'

class TestCaseAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_service(self):
        response = self.app.get('/')
        assert response.status_code == 200

    def test_cre_info(self):
        response = self.app.get('/mdref/goodref')
        response_json = json.loads(response.data.decode())
        cre_codes = response_json['CRE_code']
        assert cre_codes[0] == 'AB123'
        assert cre_codes[1] == 'CD678'
        assert response_json["draft_entry_text"][0] == "This is some kind of entry to go on the register"
