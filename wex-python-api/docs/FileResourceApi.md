# ibmwex.FileResourceApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](FileResourceApi.md#create) | **POST** /api/v1/fileResources | Create a file resource
[**delete**](FileResourceApi.md#delete) | **DELETE** /api/v1/fileResources/{fileResourceId} | Delete a file resource
[**download**](FileResourceApi.md#download) | **GET** /api/v1/fileResources/{fileResourceId}/download | Fetch a file resource content
[**get**](FileResourceApi.md#get) | **GET** /api/v1/fileResources/{fileResourceId} | List file resource details
[**list**](FileResourceApi.md#list) | **GET** /api/v1/fileResources | List file resources
[**update**](FileResourceApi.md#update) | **PUT** /api/v1/fileResources/{fileResourceId} | Update a file resource
[**upload**](FileResourceApi.md#upload) | **POST** /api/v1/fileResources/{fileResourceId}/upload | Update a file resource content


# **create**
> FileResource create(body)

Create a file resource

Creates a new file resource.

### Example 
```python
from __future__ import print_function
import time
import ibmwex
from ibmwex.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
ibmwex.configuration.username = 'YOUR_USERNAME'
ibmwex.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = ibmwex.FileResourceApi()
body = ibmwex.FileResource() # FileResource | 

try: 
    # Create a file resource
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileResourceApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileResource**](FileResource.md)|  | 

### Return type

[**FileResource**](FileResource.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> SimpleResponse delete(file_resource_id)

Delete a file resource

Deletes an existing file resource.

### Example 
```python
from __future__ import print_function
import time
import ibmwex
from ibmwex.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
ibmwex.configuration.username = 'YOUR_USERNAME'
ibmwex.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = ibmwex.FileResourceApi()
file_resource_id = 'file_resource_id_example' # str | The ID of the file resource.

try: 
    # Delete a file resource
    api_response = api_instance.delete(file_resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileResourceApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_resource_id** | **str**| The ID of the file resource. | 

### Return type

[**SimpleResponse**](SimpleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download**
> download(file_resource_id)

Fetch a file resource content

Fetches a content of an existing file resource.

### Example 
```python
from __future__ import print_function
import time
import ibmwex
from ibmwex.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
ibmwex.configuration.username = 'YOUR_USERNAME'
ibmwex.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = ibmwex.FileResourceApi()
file_resource_id = 'file_resource_id_example' # str | The ID of the file resource.

try: 
    # Fetch a file resource content
    api_instance.download(file_resource_id)
except ApiException as e:
    print("Exception when calling FileResourceApi->download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_resource_id** | **str**| The ID of the file resource. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> FileResource get(file_resource_id)

List file resource details

Display detailed information about an existing file resource.

### Example 
```python
from __future__ import print_function
import time
import ibmwex
from ibmwex.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
ibmwex.configuration.username = 'YOUR_USERNAME'
ibmwex.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = ibmwex.FileResourceApi()
file_resource_id = 'file_resource_id_example' # str | The ID of the file resource.

try: 
    # List file resource details
    api_response = api_instance.get(file_resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileResourceApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_resource_id** | **str**| The ID of the file resource. | 

### Return type

[**FileResource**](FileResource.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ListResponseFileResource list()

List file resources

Display a list of existing file resources.

### Example 
```python
from __future__ import print_function
import time
import ibmwex
from ibmwex.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
ibmwex.configuration.username = 'YOUR_USERNAME'
ibmwex.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = ibmwex.FileResourceApi()

try: 
    # List file resources
    api_response = api_instance.list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileResourceApi->list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListResponseFileResource**](ListResponseFileResource.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> FileResource update(file_resource_id, body)

Update a file resource

Updates an existing file resource.

### Example 
```python
from __future__ import print_function
import time
import ibmwex
from ibmwex.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
ibmwex.configuration.username = 'YOUR_USERNAME'
ibmwex.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = ibmwex.FileResourceApi()
file_resource_id = 'file_resource_id_example' # str | The ID of the file resource.
body = ibmwex.FileResource() # FileResource | 

try: 
    # Update a file resource
    api_response = api_instance.update(file_resource_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileResourceApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_resource_id** | **str**| The ID of the file resource. | 
 **body** | [**FileResource**](FileResource.md)|  | 

### Return type

[**FileResource**](FileResource.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload**
> FileResource upload(file_resource_id, file)

Update a file resource content

Updates a content of an existing file resource.

### Example 
```python
from __future__ import print_function
import time
import ibmwex
from ibmwex.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
ibmwex.configuration.username = 'YOUR_USERNAME'
ibmwex.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = ibmwex.FileResourceApi()
file_resource_id = 'file_resource_id_example' # str | The ID of the file resource.
file = '/path/to/file.txt' # file | 

try: 
    # Update a file resource content
    api_response = api_instance.upload(file_resource_id, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileResourceApi->upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_resource_id** | **str**| The ID of the file resource. | 
 **file** | **file**|  | 

### Return type

[**FileResource**](FileResource.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

