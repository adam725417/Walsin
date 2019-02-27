# ibmwex.DocumentExportApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download**](DocumentExportApi.md#download) | **GET** /api/v1/collections/{collectionId}/export/{jobId}/content | Download exported document
[**get_job**](DocumentExportApi.md#get_job) | **GET** /api/v1/collections/{collectionId}/export/{jobId} | Get status of a job
[**list**](DocumentExportApi.md#list) | **GET** /api/v1/collections/{collectionId}/export | List doucment export jobs
[**submit**](DocumentExportApi.md#submit) | **POST** /api/v1/collections/{collectionId}/export | Request document export


# **download**
> download(collection_id, job_id)

Download exported document

Get status of job

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
api_instance = ibmwex.DocumentExportApi()
collection_id = 'collection_id_example' # str | The ID of the collection.
job_id = 'job_id_example' # str | The ID of the job.

try: 
    # Download exported document
    api_instance.download(collection_id, job_id)
except ApiException as e:
    print("Exception when calling DocumentExportApi->download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The ID of the collection. | 
 **job_id** | **str**| The ID of the job. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> ExportStatus get_job(collection_id, job_id)

Get status of a job

Get status of job

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
api_instance = ibmwex.DocumentExportApi()
collection_id = 'collection_id_example' # str | The ID of the collection.
job_id = 'job_id_example' # str | The ID of the job.

try: 
    # Get status of a job
    api_response = api_instance.get_job(collection_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentExportApi->get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The ID of the collection. | 
 **job_id** | **str**| The ID of the job. | 

### Return type

[**ExportStatus**](ExportStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> list[ExportStatus] list(collection_id)

List doucment export jobs

List all jobs

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
api_instance = ibmwex.DocumentExportApi()
collection_id = 'collection_id_example' # str | The ID of the collection.

try: 
    # List doucment export jobs
    api_response = api_instance.list(collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentExportApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The ID of the collection. | 

### Return type

[**list[ExportStatus]**](ExportStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit**
> str submit(collection_id, body)

Request document export

Request document export

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
api_instance = ibmwex.DocumentExportApi()
collection_id = 'collection_id_example' # str | The ID of the collection.
body = ibmwex.ExportRequest() # ExportRequest | 

try: 
    # Request document export
    api_response = api_instance.submit(collection_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentExportApi->submit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The ID of the collection. | 
 **body** | [**ExportRequest**](ExportRequest.md)|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

