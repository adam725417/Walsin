# coding: utf-8

"""
    WEX REST APIs

    Authentication methods - Basic Auth - JSON Web Token   - [POST /api/v1/usermgmt/login](#!/User/signinUser)   - [POST /api/v1/usermgmt/logout](#!/User/doLogout) - Python client sample [Download](/docs/wex-python-api.zip) 

    OpenAPI spec version: 12.0.2.417
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class NLPApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def analyze(self, collection_id, **kwargs):
        """
        Analyze documents with enrichments of a specified collection
        Real-time NLP allows users to analyze their documents with enrichments of a specified collection. Results describe enriched document that will be stored when indexed (not during the call of this API).
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.analyze(collection_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str collection_id: The ID of the collection. (required)
        :param NLPDocument document: Set a document to analyze. Document has two fields, **fields** and metadata. You only need to deal with **fields** for analysis. Fields holds key-value pairs that a text or string value is associated with a field name of dataset used by a collection. Note that annotators will be processed basically against **analyzable** **text** **content** **fields**, which can be checked in enrichFieldGroups of collection configuration or in collection edition UI. The other types of fields can be used for another purpose. For example, a classifier can use those fields when it uses such fields as features. 
        :return: RichDocument
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.analyze_with_http_info(collection_id, **kwargs)
        else:
            (data) = self.analyze_with_http_info(collection_id, **kwargs)
            return data

    def analyze_with_http_info(self, collection_id, **kwargs):
        """
        Analyze documents with enrichments of a specified collection
        Real-time NLP allows users to analyze their documents with enrichments of a specified collection. Results describe enriched document that will be stored when indexed (not during the call of this API).
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.analyze_with_http_info(collection_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str collection_id: The ID of the collection. (required)
        :param NLPDocument document: Set a document to analyze. Document has two fields, **fields** and metadata. You only need to deal with **fields** for analysis. Fields holds key-value pairs that a text or string value is associated with a field name of dataset used by a collection. Note that annotators will be processed basically against **analyzable** **text** **content** **fields**, which can be checked in enrichFieldGroups of collection configuration or in collection edition UI. The other types of fields can be used for another purpose. For example, a classifier can use those fields when it uses such fields as features. 
        :return: RichDocument
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collection_id', 'document']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method analyze" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collection_id' is set
        if ('collection_id' not in params) or (params['collection_id'] is None):
            raise ValueError("Missing the required parameter `collection_id` when calling `analyze`")


        collection_formats = {}

        path_params = {}
        if 'collection_id' in params:
            path_params['collectionId'] = params['collection_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'document' in params:
            body_params = params['document']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['basicAuth']

        return self.api_client.call_api('/api/v1/collections/{collectionId}/analyze', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='RichDocument',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
