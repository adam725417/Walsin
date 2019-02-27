# ibmwex.RankerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](RankerApi.md#create) | **POST** /api/v1/rankers | Create a ranker instance
[**delete**](RankerApi.md#delete) | **DELETE** /api/v1/rankers/{rankerInstanceId} | Delete a ranker instance
[**get**](RankerApi.md#get) | **GET** /api/v1/rankers/{rankerInstanceId} | Show ranker instance details
[**list**](RankerApi.md#list) | **GET** /api/v1/rankers | List ranker instances
[**update**](RankerApi.md#update) | **PUT** /api/v1/rankers/{rankerInstanceId} | Update a ranker instance


# **create**
> Ranker create(body)

Create a ranker instance

Creates a new ranker instance

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
api_instance = ibmwex.RankerApi()
body = ibmwex.Ranker() # Ranker | 

try: 
    # Create a ranker instance
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankerApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Ranker**](Ranker.md)|  | 

### Return type

[**Ranker**](Ranker.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> SimpleResponse delete(ranker_instance_id)

Delete a ranker instance

Delete an existing ranker instance

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
api_instance = ibmwex.RankerApi()
ranker_instance_id = 'ranker_instance_id_example' # str | The ID of the ranker instance.

try: 
    # Delete a ranker instance
    api_response = api_instance.delete(ranker_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankerApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ranker_instance_id** | **str**| The ID of the ranker instance. | 

### Return type

[**SimpleResponse**](SimpleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Ranker get(ranker_instance_id)

Show ranker instance details

Show detailed information of an existing ranker instance

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
api_instance = ibmwex.RankerApi()
ranker_instance_id = 'ranker_instance_id_example' # str | The ID of the ranker instance.

try: 
    # Show ranker instance details
    api_response = api_instance.get(ranker_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankerApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ranker_instance_id** | **str**| The ID of the ranker instance. | 

### Return type

[**Ranker**](Ranker.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ListResponseRanker list()

List ranker instances

Display a list of existing ranker instances.

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
api_instance = ibmwex.RankerApi()

try: 
    # List ranker instances
    api_response = api_instance.list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankerApi->list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListResponseRanker**](ListResponseRanker.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Ranker update(ranker_instance_id, body)

Update a ranker instance

Update an existing ranker instance

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
api_instance = ibmwex.RankerApi()
ranker_instance_id = 'ranker_instance_id_example' # str | The ID of the ranker instance.
body = ibmwex.Ranker() # Ranker | 

try: 
    # Update a ranker instance
    api_response = api_instance.update(ranker_instance_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankerApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ranker_instance_id** | **str**| The ID of the ranker instance. | 
 **body** | [**Ranker**](Ranker.md)|  | 

### Return type

[**Ranker**](Ranker.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

