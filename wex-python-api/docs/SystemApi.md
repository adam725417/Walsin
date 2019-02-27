# ibmwex.SystemApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_logs**](SystemApi.md#download_logs) | **GET** /api/v1/system/logs/download | Get logs in CSV format.
[**download_service_logs**](SystemApi.md#download_service_logs) | **GET** /api/v1/system/logs/service | Download service logs for IBM support.
[**export_config**](SystemApi.md#export_config) | **GET** /api/v1/system/config/{type}/{id} | Export configuration and resources
[**get_logs**](SystemApi.md#get_logs) | **GET** /api/v1/system/logs | Get logs in JSON format.
[**get_usage**](SystemApi.md#get_usage) | **GET** /api/v1/system/usage | Get system usage
[**import_config**](SystemApi.md#import_config) | **POST** /api/v1/system/config | Import configuration and resources


# **download_logs**
> download_logs(type=type, filter=filter, _from=_from, to=to)

Get logs in CSV format.

Get formatted system and audit logs in CSV format.

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
api_instance = ibmwex.SystemApi()
type = 'log' # str | Type of logs (optional) (default to log)
filter = 'all' # str | Filter logs by user (optional) (default to all)
_from = 789 # int | Oldest logs in epoch time [ms] (optional)
to = 789 # int | Latest logs in epoch time [ms] (optional)

try: 
    # Get logs in CSV format.
    api_instance.download_logs(type=type, filter=filter, _from=_from, to=to)
except ApiException as e:
    print("Exception when calling SystemApi->download_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type of logs | [optional] [default to log]
 **filter** | **str**| Filter logs by user | [optional] [default to all]
 **_from** | **int**| Oldest logs in epoch time [ms] | [optional] 
 **to** | **int**| Latest logs in epoch time [ms] | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_service_logs**
> download_service_logs(core=core, heapdump=heapdump)

Download service logs for IBM support.

Download logs and system info in zip format.

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
api_instance = ibmwex.SystemApi()
core = true # bool | Set <code>true</code> to include \"core.*\" (optional)
heapdump = true # bool | Set <code>true</code> to include \"heapdump.*\" (optional)

try: 
    # Download service logs for IBM support.
    api_instance.download_service_logs(core=core, heapdump=heapdump)
except ApiException as e:
    print("Exception when calling SystemApi->download_service_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **core** | **bool**| Set &lt;code&gt;true&lt;/code&gt; to include \&quot;core.*\&quot; | [optional] 
 **heapdump** | **bool**| Set &lt;code&gt;true&lt;/code&gt; to include \&quot;heapdump.*\&quot; | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_config**
> str export_config(type, id)

Export configuration and resources

Download a package which contains configuration and related resources. Related resouces except built-in resources and data sets will be included. Example: Exporting simple collection includes collection, enrichment, ranker and file resources. 

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
api_instance = ibmwex.SystemApi()
type = 'type_example' # str | Type of resource
id = 'id_example' # str | ID of resource

try: 
    # Export configuration and resources
    api_response = api_instance.export_config(type, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->export_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type of resource | 
 **id** | **str**| ID of resource | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logs**
> LogRecords get_logs(type=type, filter=filter, _from=_from, to=to, offset=offset, size=size, level=level, order=order)

Get logs in JSON format.

Get formatted system and audit logs.

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
api_instance = ibmwex.SystemApi()
type = 'log' # str | Type of logs (optional) (default to log)
filter = 'all' # str | Filter logs by user (optional) (default to all)
_from = 789 # int | Oldest logs in epoch time [ms] (optional)
to = 789 # int | Latest logs in epoch time [ms] (optional)
offset = 56 # int | Offset of first log records in the result (optional)
size = 56 # int | Maximum size of the records (optional)
level = 'INFO' # str | Returned log with level equal or above this level (optional) (default to INFO)
order = 'asc' # str | Sort order of the returned log record (optional) (default to asc)

try: 
    # Get logs in JSON format.
    api_response = api_instance.get_logs(type=type, filter=filter, _from=_from, to=to, offset=offset, size=size, level=level, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->get_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type of logs | [optional] [default to log]
 **filter** | **str**| Filter logs by user | [optional] [default to all]
 **_from** | **int**| Oldest logs in epoch time [ms] | [optional] 
 **to** | **int**| Latest logs in epoch time [ms] | [optional] 
 **offset** | **int**| Offset of first log records in the result | [optional] 
 **size** | **int**| Maximum size of the records | [optional] 
 **level** | **str**| Returned log with level equal or above this level | [optional] [default to INFO]
 **order** | **str**| Sort order of the returned log record | [optional] [default to asc]

### Return type

[**LogRecords**](LogRecords.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage**
> SystemUsage get_usage()

Get system usage

Display system usage information.

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
api_instance = ibmwex.SystemApi()

try: 
    # Get system usage
    api_response = api_instance.get_usage()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->get_usage: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemUsage**](SystemUsage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_config**
> import_config(file)

Import configuration and resources

Upload exported file and load into the system. Imported resource ID will be remain same and can be updated by latest resource. 

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
api_instance = ibmwex.SystemApi()
file = '/path/to/file.txt' # file | Exported file

try: 
    # Import configuration and resources
    api_instance.import_config(file)
except ApiException as e:
    print("Exception when calling SystemApi->import_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| Exported file | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

