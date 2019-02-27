# ibmwex.CrawlerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](CrawlerApi.md#create) | **POST** /api/v1/datasets/{datasetId}/crawlers | Create a crawler
[**delete**](CrawlerApi.md#delete) | **DELETE** /api/v1/datasets/{datasetId}/crawlers/{crawlerId} | Delete a crawler
[**discover_subspaces**](CrawlerApi.md#discover_subspaces) | **POST** /api/v1/crawler/subspaces | Discover subspaces
[**get**](CrawlerApi.md#get) | **GET** /api/v1/datasets/{datasetId}/crawlers/{crawlerId} | Get a crawler configuration
[**get_template**](CrawlerApi.md#get_template) | **GET** /api/v1/crawler/types/{crawlerTypeName} | Get a crawler template for a specified cralwer type
[**get_types**](CrawlerApi.md#get_types) | **GET** /api/v1/crawler/types | Get a list of crawler types
[**list**](CrawlerApi.md#list) | **GET** /api/v1/datasets/{datasetId}/crawlers | Get a list of crawlers
[**start**](CrawlerApi.md#start) | **POST** /api/v1/datasets/{datasetId}/crawlers/{crawlerId}/start | Start a crawler
[**status**](CrawlerApi.md#status) | **GET** /api/v1/datasets/{datasetId}/crawlers/{crawlerId}/status | List crawler status
[**stop**](CrawlerApi.md#stop) | **POST** /api/v1/datasets/{datasetId}/crawlers/{crawlerId}/stop | Stop a crawler
[**update**](CrawlerApi.md#update) | **PUT** /api/v1/datasets/{datasetId}/crawlers/{crawlerId} | Update a crawler configuration


# **create**
> Crawler create(dataset_id, body=body)

Create a crawler

Create a crawler

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
api_instance = ibmwex.CrawlerApi()
dataset_id = 'dataset_id_example' # str | 
body = ibmwex.CrawlerConfiguration() # CrawlerConfiguration |  (optional)

try: 
    # Create a crawler
    api_response = api_instance.create(dataset_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrawlerApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **body** | [**CrawlerConfiguration**](CrawlerConfiguration.md)|  | [optional] 

### Return type

[**Crawler**](Crawler.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> SimpleResponse delete(dataset_id, crawler_id)

Delete a crawler

Delete a configuration of a specified crawler

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
api_instance = ibmwex.CrawlerApi()
dataset_id = 'dataset_id_example' # str | 
crawler_id = 'crawler_id_example' # str | 

try: 
    # Delete a crawler
    api_response = api_instance.delete(dataset_id, crawler_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrawlerApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **crawler_id** | **str**|  | 

### Return type

[**SimpleResponse**](SimpleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_subspaces**
> ListDiscoveredSubspaces discover_subspaces(path=path, filters=filters, body=body)

Discover subspaces

Discover subspaces available for the crawler with the provided path / filter.

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
api_instance = ibmwex.CrawlerApi()
path = 'path_example' # str |  (optional)
filters = 'filters_example' # str |  (optional)
body = ibmwex.CrawlerConfiguration() # CrawlerConfiguration |  (optional)

try: 
    # Discover subspaces
    api_response = api_instance.discover_subspaces(path=path, filters=filters, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrawlerApi->discover_subspaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | [optional] 
 **filters** | **str**|  | [optional] 
 **body** | [**CrawlerConfiguration**](CrawlerConfiguration.md)|  | [optional] 

### Return type

[**ListDiscoveredSubspaces**](ListDiscoveredSubspaces.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> CrawlerConfiguration get(dataset_id, crawler_id)

Get a crawler configuration

Get a crawler configuration

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
api_instance = ibmwex.CrawlerApi()
dataset_id = 'dataset_id_example' # str | 
crawler_id = 'crawler_id_example' # str | 

try: 
    # Get a crawler configuration
    api_response = api_instance.get(dataset_id, crawler_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrawlerApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **crawler_id** | **str**|  | 

### Return type

[**CrawlerConfiguration**](CrawlerConfiguration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template**
> ConfigurationTemplate get_template(crawler_type_name)

Get a crawler template for a specified cralwer type

Get a crawler template

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
api_instance = ibmwex.CrawlerApi()
crawler_type_name = 'crawler_type_name_example' # str | 

try: 
    # Get a crawler template for a specified cralwer type
    api_response = api_instance.get_template(crawler_type_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrawlerApi->get_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crawler_type_name** | **str**|  | 

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

Get a list of crawler types

Get a list of available crawler types.

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
api_instance = ibmwex.CrawlerApi()

try: 
    # Get a list of crawler types
    api_response = api_instance.get_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrawlerApi->get_types: %s\n" % e)
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

# **list**
> ListResponseCrawler list(dataset_id)

Get a list of crawlers

Get a list of crawlers

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
api_instance = ibmwex.CrawlerApi()
dataset_id = 'dataset_id_example' # str | 

try: 
    # Get a list of crawlers
    api_response = api_instance.list(dataset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrawlerApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 

### Return type

[**ListResponseCrawler**](ListResponseCrawler.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start**
> start(dataset_id, crawler_id)

Start a crawler

Starts ingesting documents with a crawler.

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
api_instance = ibmwex.CrawlerApi()
dataset_id = 'dataset_id_example' # str | The ID of the dataset.
crawler_id = 'crawler_id_example' # str | The ID of the crawler.

try: 
    # Start a crawler
    api_instance.start(dataset_id, crawler_id)
except ApiException as e:
    print("Exception when calling CrawlerApi->start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset. | 
 **crawler_id** | **str**| The ID of the crawler. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status**
> ZkIngestionStatus status(dataset_id, crawler_id)

List crawler status

Displays status information about a crawler.

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
api_instance = ibmwex.CrawlerApi()
dataset_id = 'dataset_id_example' # str | The ID of the dataset.
crawler_id = 'crawler_id_example' # str | The ID of the crawler.

try: 
    # List crawler status
    api_response = api_instance.status(dataset_id, crawler_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrawlerApi->status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset. | 
 **crawler_id** | **str**| The ID of the crawler. | 

### Return type

[**ZkIngestionStatus**](ZkIngestionStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop**
> stop(dataset_id, crawler_id)

Stop a crawler

Stops ingesting documents with a crawler.

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
api_instance = ibmwex.CrawlerApi()
dataset_id = 'dataset_id_example' # str | The ID of the dataset.
crawler_id = 'crawler_id_example' # str | The ID of the crawler.

try: 
    # Stop a crawler
    api_instance.stop(dataset_id, crawler_id)
except ApiException as e:
    print("Exception when calling CrawlerApi->stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset. | 
 **crawler_id** | **str**| The ID of the crawler. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Crawler update(dataset_id, crawler_id, body=body)

Update a crawler configuration

Update a configuration of a specified crawler

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
api_instance = ibmwex.CrawlerApi()
dataset_id = 'dataset_id_example' # str | 
crawler_id = 'crawler_id_example' # str | 
body = ibmwex.CrawlerConfiguration() # CrawlerConfiguration |  (optional)

try: 
    # Update a crawler configuration
    api_response = api_instance.update(dataset_id, crawler_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrawlerApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**|  | 
 **crawler_id** | **str**|  | 
 **body** | [**CrawlerConfiguration**](CrawlerConfiguration.md)|  | [optional] 

### Return type

[**Crawler**](Crawler.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

