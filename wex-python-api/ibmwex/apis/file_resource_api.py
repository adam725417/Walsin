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


class FileResourceApi(object):
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

    def create(self, body, **kwargs):
        """
        Create a file resource
        Creates a new file resource.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param FileResource body: (required)
        :return: FileResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_with_http_info(body, **kwargs)
        else:
            (data) = self.create_with_http_info(body, **kwargs)
            return data

    def create_with_http_info(self, body, **kwargs):
        """
        Create a file resource
        Creates a new file resource.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param FileResource body: (required)
        :return: FileResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basicAuth']

        return self.api_client.call_api('/api/v1/fileResources', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FileResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete(self, file_resource_id, **kwargs):
        """
        Delete a file resource
        Deletes an existing file resource.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete(file_resource_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str file_resource_id: The ID of the file resource. (required)
        :return: SimpleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_with_http_info(file_resource_id, **kwargs)
        else:
            (data) = self.delete_with_http_info(file_resource_id, **kwargs)
            return data

    def delete_with_http_info(self, file_resource_id, **kwargs):
        """
        Delete a file resource
        Deletes an existing file resource.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_with_http_info(file_resource_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str file_resource_id: The ID of the file resource. (required)
        :return: SimpleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_resource_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_resource_id' is set
        if ('file_resource_id' not in params) or (params['file_resource_id'] is None):
            raise ValueError("Missing the required parameter `file_resource_id` when calling `delete`")


        collection_formats = {}

        path_params = {}
        if 'file_resource_id' in params:
            path_params['fileResourceId'] = params['file_resource_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['basicAuth']

        return self.api_client.call_api('/api/v1/fileResources/{fileResourceId}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SimpleResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def download(self, file_resource_id, **kwargs):
        """
        Fetch a file resource content
        Fetches a content of an existing file resource.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.download(file_resource_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str file_resource_id: The ID of the file resource. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.download_with_http_info(file_resource_id, **kwargs)
        else:
            (data) = self.download_with_http_info(file_resource_id, **kwargs)
            return data

    def download_with_http_info(self, file_resource_id, **kwargs):
        """
        Fetch a file resource content
        Fetches a content of an existing file resource.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.download_with_http_info(file_resource_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str file_resource_id: The ID of the file resource. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_resource_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_resource_id' is set
        if ('file_resource_id' not in params) or (params['file_resource_id'] is None):
            raise ValueError("Missing the required parameter `file_resource_id` when calling `download`")


        collection_formats = {}

        path_params = {}
        if 'file_resource_id' in params:
            path_params['fileResourceId'] = params['file_resource_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/octet-stream'])

        # Authentication setting
        auth_settings = ['basicAuth']

        return self.api_client.call_api('/api/v1/fileResources/{fileResourceId}/download', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get(self, file_resource_id, **kwargs):
        """
        List file resource details
        Display detailed information about an existing file resource.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get(file_resource_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str file_resource_id: The ID of the file resource. (required)
        :return: FileResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_with_http_info(file_resource_id, **kwargs)
        else:
            (data) = self.get_with_http_info(file_resource_id, **kwargs)
            return data

    def get_with_http_info(self, file_resource_id, **kwargs):
        """
        List file resource details
        Display detailed information about an existing file resource.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_with_http_info(file_resource_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str file_resource_id: The ID of the file resource. (required)
        :return: FileResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_resource_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_resource_id' is set
        if ('file_resource_id' not in params) or (params['file_resource_id'] is None):
            raise ValueError("Missing the required parameter `file_resource_id` when calling `get`")


        collection_formats = {}

        path_params = {}
        if 'file_resource_id' in params:
            path_params['fileResourceId'] = params['file_resource_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['basicAuth']

        return self.api_client.call_api('/api/v1/fileResources/{fileResourceId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FileResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list(self, **kwargs):
        """
        List file resources
        Display a list of existing file resources.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: ListResponseFileResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_with_http_info(**kwargs)
        else:
            (data) = self.list_with_http_info(**kwargs)
            return data

    def list_with_http_info(self, **kwargs):
        """
        List file resources
        Display a list of existing file resources.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: ListResponseFileResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['basicAuth']

        return self.api_client.call_api('/api/v1/fileResources', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ListResponseFileResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update(self, file_resource_id, body, **kwargs):
        """
        Update a file resource
        Updates an existing file resource.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update(file_resource_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str file_resource_id: The ID of the file resource. (required)
        :param FileResource body: (required)
        :return: FileResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_with_http_info(file_resource_id, body, **kwargs)
        else:
            (data) = self.update_with_http_info(file_resource_id, body, **kwargs)
            return data

    def update_with_http_info(self, file_resource_id, body, **kwargs):
        """
        Update a file resource
        Updates an existing file resource.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_with_http_info(file_resource_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str file_resource_id: The ID of the file resource. (required)
        :param FileResource body: (required)
        :return: FileResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_resource_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_resource_id' is set
        if ('file_resource_id' not in params) or (params['file_resource_id'] is None):
            raise ValueError("Missing the required parameter `file_resource_id` when calling `update`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update`")


        collection_formats = {}

        path_params = {}
        if 'file_resource_id' in params:
            path_params['fileResourceId'] = params['file_resource_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basicAuth']

        return self.api_client.call_api('/api/v1/fileResources/{fileResourceId}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FileResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def upload(self, file_resource_id, file, **kwargs):
        """
        Update a file resource content
        Updates a content of an existing file resource.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.upload(file_resource_id, file, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str file_resource_id: The ID of the file resource. (required)
        :param file file: (required)
        :return: FileResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.upload_with_http_info(file_resource_id, file, **kwargs)
        else:
            (data) = self.upload_with_http_info(file_resource_id, file, **kwargs)
            return data

    def upload_with_http_info(self, file_resource_id, file, **kwargs):
        """
        Update a file resource content
        Updates a content of an existing file resource.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.upload_with_http_info(file_resource_id, file, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str file_resource_id: The ID of the file resource. (required)
        :param file file: (required)
        :return: FileResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_resource_id', 'file']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_resource_id' is set
        if ('file_resource_id' not in params) or (params['file_resource_id'] is None):
            raise ValueError("Missing the required parameter `file_resource_id` when calling `upload`")
        # verify the required parameter 'file' is set
        if ('file' not in params) or (params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `upload`")


        collection_formats = {}

        path_params = {}
        if 'file_resource_id' in params:
            path_params['fileResourceId'] = params['file_resource_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = ['basicAuth']

        return self.api_client.call_api('/api/v1/fileResources/{fileResourceId}/upload', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FileResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)