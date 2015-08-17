import unittest
import json
import os
import mock

from application import app, db
from test_data import get_cre_response


submission_ref = "ZYX9873"
case_data = '{ "dateReceived": "1993-11-01T12:00:00Z", "submissionRef": "' + submission_ref + '", "keyNumber": "KEY3243", "amountPaid": "12000", "lender": "GE Money Home Finance Limited", "mortgageDate": "1993-08-13T12:00:00Z", "titleNumber": "DN503122", "borrower": "", "propertyDetails": "", "emdref": ""}'

class TestCaseAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_service(self):
        response = self.app.get('/')
        assert response.status_code == 200

    #@mock.patch('db.engine.execute')
    @mock.patch('application.routes.get_cre_info')
    def test_cre_info(self, mock_cre_info):
        mock_cre_info.return_value = get_cre_response()
        response = self.app.get('/mdref/goodref')
        response_json = json.loads(response.data.decode())
        cre_codes = response_json['cres']
        assert cre_codes[0]["code"] == 'CD100'
        assert cre_codes[1]["sub_role_code"] == 'BRES'
