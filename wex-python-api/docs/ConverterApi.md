# ibmwex.ConverterApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download**](ConverterApi.md#download) | **GET** /api/v1/datasets/{datasetId}/testit/download | Download TestIt result
[**execute**](ConverterApi.md#execute) | **POST** /api/v1/datasets/{datasetId}/testit/execute | Execute TestIt
[**get_configuration_template**](ConverterApi.md#get_configuration_template) | **GET** /api/v1/converter/types/{converterType} | List converter configuration
[**get_types**](ConverterApi.md#get_types) | **GET** /api/v1/converter/types | List converter types
[**upload_r**](ConverterApi.md#upload_r) | **POST** /api/v1/datasets/{datasetId}/testit/upload/remote | Upload TestIt file on remote
[**upload_s**](ConverterApi.md#upload_s) | **POST** /api/v1/datasets/{datasetId}/testit/upload/server | Upload TestIt file on server


# **download**
> download(dataset_id, path)

Download TestIt result

Download TestIt result

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
api_instance = ibmwex.ConverterApi()
dataset_id = 'dataset_id_example' # str | The ID of the dataset.
path = 'path_example' # str | 

try: 
    # Download TestIt result
    api_instance.download(dataset_id, path)
except ApiException as e:
    print("Exception when calling ConverterApi->download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset. | 
 **path** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute**
> execute(dataset_id)

Execute TestIt

Execute TestIt

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
api_instance = ibmwex.ConverterApi()
dataset_id = 'dataset_id_example' # str | The ID of the dataset.

try: 
    # Execute TestIt
    api_instance.execute(dataset_id)
except ApiException as e:
    print("Exception when calling ConverterApi->execute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration_template**
> ConfigurationTemplate get_configuration_template(converter_type)

List converter configuration

Displays a list of configuration parameter of converter.

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
api_instance = ibmwex.ConverterApi()
converter_type = 'converter_type_example' # str | The type of converter.

try: 
    # List converter configuration
    api_response = api_instance.get_configuration_template(converter_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConverterApi->get_configuration_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **converter_type** | **str**| The type of converter. | 

### Return type

[**ConfigurationTemplate**](ConfigurationTemplate.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_types**
> ListResponseConfigurationType get_types()

List converter types

Display a list of available converter types.

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
api_instance = ibmwex.ConverterApi()

try: 
    # List converter types
    api_response = api_instance.get_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConverterApi->get_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListResponseConfigurationType**](ListResponseConfigurationType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_r**
> ListResponseTestit upload_r(dataset_id, file)

Upload TestIt file on remote

Upload a TestIt file on a remote machine

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
api_instance = ibmwex.ConverterApi()
dataset_id = 'dataset_id_example' # str | The ID of the dataset.
file = '/path/to/file.txt' # file | 

try: 
    # Upload TestIt file on remote
    api_response = api_instance.upload_r(dataset_id, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConverterApi->upload_r: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset. | 
 **file** | **file**|  | 

### Return type

[**ListResponseTestit**](ListResponseTestit.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_s**
> ListResponseTestit upload_s(dataset_id, path)

Upload TestIt file on server

Upload a TestIt file on the server

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
api_instance = ibmwex.ConverterApi()
dataset_id = 'dataset_id_example' # str | The ID of the dataset.
path = 'path_example' # str | 

try: 
    # Upload TestIt file on server
    api_response = api_instance.upload_s(dataset_id, path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConverterApi->upload_s: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset. | 
 **path** | **str**|  | 

### Return type

[**ListResponseTestit**](ListResponseTestit.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

