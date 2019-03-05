# coding: utf-8

"""
    WEX REST APIs

    Authentication methods - Basic Auth - JSON Web Token   - [POST /api/v1/usermgmt/login](#!/User/signinUser)   - [POST /api/v1/usermgmt/logout](#!/User/doLogout) - Python client sample [Download](/docs/wex-python-api.zip) 

    OpenAPI spec version: 12.0.2.417
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import ibmwex
from ibmwex.rest import ApiException
from ibmwex.apis.document_export_api import DocumentExportApi


class TestDocumentExportApi(unittest.TestCase):
    """ DocumentExportApi unit test stubs """

    def setUp(self):
        self.api = ibmwex.apis.document_export_api.DocumentExportApi()

    def tearDown(self):
        pass

    def test_download(self):
        """
        Test case for download

        Download exported document
        """
        pass

    def test_get_job(self):
        """
        Test case for get_job

        Get status of a job
        """
        pass

    def test_list(self):
        """
        Test case for list

        List doucment export jobs
        """
        pass

    def test_submit(self):
        """
        Test case for submit

        Request document export
        """
        pass


if __name__ == '__main__':
    unittest.main()