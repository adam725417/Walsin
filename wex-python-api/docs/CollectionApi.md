# ibmwex.CollectionApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](CollectionApi.md#create) | **POST** /api/v1/collections | Create a collection
[**delete**](CollectionApi.md#delete) | **DELETE** /api/v1/collections/{collectionId} | Delete a collection
[**get**](CollectionApi.md#get) | **GET** /api/v1/collections/{collectionId} | List collection details
[**is_indexing_enabled**](CollectionApi.md#is_indexing_enabled) | **GET** /api/v1/collections/{collectionId}/indexing | Get indexing status
[**list**](CollectionApi.md#list) | **GET** /api/v1/collections | List collections
[**rebuild**](CollectionApi.md#rebuild) | **POST** /api/v1/collections/{collectionId}/rebuild | Request rebuild index
[**set_indexing_enabled**](CollectionApi.md#set_indexing_enabled) | **PUT** /api/v1/collections/{collectionId}/indexing | Change indexing status
[**status**](CollectionApi.md#status) | **GET** /api/v1/collections/{collectionId}/status | List collection status
[**status_all**](CollectionApi.md#status_all) | **GET** /api/v1/collections/status | List status for all collections
[**update**](CollectionApi.md#update) | **PUT** /api/v1/collections/{collectionId} | Update a collection


# **create**
> Collection create(body)

Create a collection

Creates a new collection.

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
api_instance = ibmwex.CollectionApi()
body = ibmwex.Collection() # Collection | 

try: 
    # Create a collection
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Collection**](Collection.md)|  | 

### Return type

[**Collection**](Collection.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> SimpleResponse delete(collection_id)

Delete a collection

Deletes an existing collection.

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
api_instance = ibmwex.CollectionApi()
collection_id = 'collection_id_example' # str | The ID of the collection.

try: 
    # Delete a collection
    api_response = api_instance.delete(collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The ID of the collection. | 

### Return type

[**SimpleResponse**](SimpleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Collection get(collection_id)

List collection details

Display detailed information about an existing collection.

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
api_instance = ibmwex.CollectionApi()
collection_id = 'collection_id_example' # str | The ID of the collection.

try: 
    # List collection details
    api_response = api_instance.get(collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The ID of the collection. | 

### Return type

[**Collection**](Collection.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_indexing_enabled**
> IndexingConfig is_indexing_enabled(collection_id)

Get indexing status

Check if indexing is enabled.

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
api_instance = ibmwex.CollectionApi()
collection_id = 'collection_id_example' # str | The ID of the collection.

try: 
    # Get indexing status
    api_response = api_instance.is_indexing_enabled(collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->is_indexing_enabled: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The ID of the collection. | 

### Return type

[**IndexingConfig**](IndexingConfig.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ListResponseCollection list()

List collections

Display a list of existing collections.

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
api_instance = ibmwex.CollectionApi()

try: 
    # List collections
    api_response = api_instance.list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListResponseCollection**](ListResponseCollection.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rebuild**
> SimpleResponse rebuild(collection_id)

Request rebuild index

Request an index rebuild on an existing collection.

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
api_instance = ibmwex.CollectionApi()
collection_id = 'collection_id_example' # str | The ID of the collection.

try: 
    # Request rebuild index
    api_response = api_instance.rebuild(collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->rebuild: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The ID of the collection. | 

### Return type

[**SimpleResponse**](SimpleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_indexing_enabled**
> IndexingConfig set_indexing_enabled(collection_id, body)

Change indexing status

Enable or disable indexing on an existing collection.

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
api_instance = ibmwex.CollectionApi()
collection_id = 'collection_id_example' # str | The ID of the collection.
body = ibmwex.IndexingConfig() # IndexingConfig | 

try: 
    # Change indexing status
    api_response = api_instance.set_indexing_enabled(collection_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->set_indexing_enabled: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The ID of the collection. | 
 **body** | [**IndexingConfig**](IndexingConfig.md)|  | 

### Return type

[**IndexingConfig**](IndexingConfig.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status**
> CollectionStatus status(collection_id)

List collection status

Display status information about an existing collection.

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
api_instance = ibmwex.CollectionApi()
collection_id = 'collection_id_example' # str | The ID of the collection.

try: 
    # List collection status
    api_response = api_instance.status(collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The ID of the collection. | 

### Return type

[**CollectionStatus**](CollectionStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_all**
> ListCollectionStatus status_all()

List status for all collections

Display status information about all existing collections.

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
api_instance = ibmwex.CollectionApi()

try: 
    # List status for all collections
    api_response = api_instance.status_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->status_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListCollectionStatus**](ListCollectionStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Collection update(collection_id, body)

Update a collection

Updates an existing collection.

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
api_instance = ibmwex.CollectionApi()
collection_id = 'collection_id_example' # str | The ID of the collection.
body = ibmwex.Collection() # Collection | 

try: 
    # Update a collection
    api_response = api_instance.update(collection_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The ID of the collection. | 
 **body** | [**Collection**](Collection.md)|  | 

### Return type

[**Collection**](Collection.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

