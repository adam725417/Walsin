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
from ibmwex.models.facet_type import FacetType


class TestFacetType(unittest.TestCase):
    """ FacetType unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFacetType(self):
        """
        Test FacetType
        """
        # FIXME: construct object with mandatory attributes with example values
        #model = ibmwex.models.facet_type.FacetType()
        pass


if __name__ == '__main__':
    unittest.main()
