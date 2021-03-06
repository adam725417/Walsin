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
from ibmwex.apis.collection_api import CollectionApi


class TestCollectionApi(unittest.TestCase):
    """ CollectionApi unit test stubs """

    def setUp(self):
        self.api = ibmwex.apis.collection_api.CollectionApi()

    def tearDown(self):
        pass

    def test_create(self):
        """
        Test case for create

        Create a collection
        """
        pass

    def test_delete(self):
        """
        Test case for delete

        Delete a collection
        """
        pass

    def test_get(self):
        """
        Test case for get

        List collection details
        """
        pass

    def test_is_indexing_enabled(self):
        """
        Test case for is_indexing_enabled

        Get indexing status
        """
        pass

    def test_list(self):
        """
        Test case for list

        List collections
        """
        pass

    def test_rebuild(self):
        """
        Test case for rebuild

        Request rebuild index
        """
        pass

    def test_set_indexing_enabled(self):
        """
        Test case for set_indexing_enabled

        Change indexing status
        """
        pass

    def test_status(self):
        """
        Test case for status

        List collection status
        """
        pass

    def test_status_all(self):
        """
        Test case for status_all

        List status for all collections
        """
        pass

    def test_update(self):
        """
        Test case for update

        Update a collection
        """
        pass


if __name__ == '__main__':
    unittest.main()
