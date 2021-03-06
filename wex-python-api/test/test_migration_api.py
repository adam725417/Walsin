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
from ibmwex.apis.migration_api import MigrationApi


class TestMigrationApi(unittest.TestCase):
    """ MigrationApi unit test stubs """

    def setUp(self):
        self.api = ibmwex.apis.migration_api.MigrationApi()

    def tearDown(self):
        pass

    def test_convert_cas_to_index(self):
        """
        Test case for convert_cas_to_index

        Migrate CAS to index mapping file
        """
        pass

    def test_convert_category_tree(self):
        """
        Test case for convert_category_tree

        Migrate category tree file
        """
        pass

    def test_convert_csv_to_fdic(self):
        """
        Test case for convert_csv_to_fdic

        Migrate dictionary CSV file
        """
        pass

    def test_convert_fdic(self):
        """
        Test case for convert_fdic

        Migrate dictionary file
        """
        pass


if __name__ == '__main__':
    unittest.main()
