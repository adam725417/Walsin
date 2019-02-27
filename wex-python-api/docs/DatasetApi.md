# ibmwex.DatasetApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_document**](DatasetApi.md#add_document) | **POST** /api/v1/datasets/{datasetId}/documents | Add a document
[**create**](DatasetApi.md#create) | **POST** /api/v1/datasets | Create a dataset
[**delete**](DatasetApi.md#delete) | **DELETE** /api/v1/datasets/{datasetId} | Delete a dataset
[**delete_document**](DatasetApi.md#delete_document) | **DELETE** /api/v1/datasets/{datasetId}/documents/{documentId} | Delete a document
[**get**](DatasetApi.md#get) | **GET** /api/v1/datasets/{datasetId} | List dataset details
[**get_converter_pipeline**](DatasetApi.md#get_converter_pipeline) | **GET** /api/v1/datasets/{datasetId}/converters | List converter pileline details
[**import_csv**](DatasetApi.md#import_csv) | **POST** /api/v1/datasets/{datasetId}/import | Import a CSV file
[**list**](DatasetApi.md#list) | **GET** /api/v1/datasets | List datasets
[**status**](DatasetApi.md#status) | **GET** /api/v1/datasets/{datasetId}/status | List dataset status
[**status_all**](DatasetApi.md#status_all) | **GET** /api/v1/datasets/status | List status for all datasets
[**update**](DatasetApi.md#update) | **PUT** /api/v1/datasets/{datasetId} | Update a dataset
[**update_converter_pipeline**](DatasetApi.md#update_converter_pipeline) | **PUT** /api/v1/datasets/{datasetId}/converters | Update converter pipeline


# **add_document**
> Dataset add_document(dataset_id, body)

Add a document

Add a document to a dataset.

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
api_instance = ibmwex.DatasetApi()
dataset_id = 'dataset_id_example' # str | The ID of the dataset.
body = [ibmwex.Document()] # list[Document] | 

try: 
    # Add a document
    api_response = api_instance.add_document(dataset_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->add_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset. | 
 **body** | [**list[Document]**](Document.md)|  | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> Dataset create(body)

Create a dataset

Creates a new dataset.

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
api_instance = ibmwex.DatasetApi()
body = ibmwex.Dataset() # Dataset | 

try: 
    # Create a dataset
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dataset**](Dataset.md)|  | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> SimpleResponse delete(dataset_id)

Delete a dataset

Deletes an existing dataset.

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
api_instance = ibmwex.DatasetApi()
dataset_id = 'dataset_id_example' # str | The ID of the dataset.

try: 
    # Delete a dataset
    api_response = api_instance.delete(dataset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset. | 

### Return type

[**SimpleResponse**](SimpleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document**
> SimpleResponse delete_document(dataset_id, document_id)

Delete a document

Delete a document from a dataset.

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
api_instance = ibmwex.DatasetApi()
dataset_id = 'dataset_id_example' # str | The ID of the dataset.
document_id = 'document_id_example' # str | The ID of the document.

try: 
    # Delete a document
    api_response = api_instance.delete_document(dataset_id, document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->delete_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset. | 
 **document_id** | **str**| The ID of the document. | 

### Return type

[**SimpleResponse**](SimpleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Dataset get(dataset_id)

List dataset details

Display detailed information about an existing dataset.

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
api_instance = ibmwex.DatasetApi()
dataset_id = 'dataset_id_example' # str | The ID of the dataset.

try: 
    # List dataset details
    api_response = api_instance.get(dataset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset. | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_converter_pipeline**
> ConverterPipelineConfiguration get_converter_pipeline(dataset_id)

List converter pileline details

Display detailed information about converters.

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
api_instance = ibmwex.DatasetApi()
dataset_id = 'dataset_id_example' # str | The ID of the dataset.

try: 
    # List converter pileline details
    api_response = api_instance.get_converter_pipeline(dataset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->get_converter_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset. | 

### Return type

[**ConverterPipelineConfiguration**](ConverterPipelineConfiguration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_csv**
> import_csv(dataset_id, tag, file, config, samples=samples)

Import a CSV file

(Deprecated) Imports a CSV file into an existing dataset.

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
api_instance = ibmwex.DatasetApi()
dataset_id = 'dataset_id_example' # str | The ID of the dataset.
tag = 'tag_example' # str | 
file = '/path/to/file.txt' # file | 
config = '/path/to/file.txt' # file | 
samples = 'samples_example' # str |  (optional)

try: 
    # Import a CSV file
    api_instance.import_csv(dataset_id, tag, file, config, samples=samples)
except ApiException as e:
    print("Exception when calling DatasetApi->import_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset. | 
 **tag** | **str**|  | 
 **file** | **file**|  | 
 **config** | **file**|  | 
 **samples** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ListResponseDataset list()

List datasets

Display a list of existing datasets.

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
api_instance = ibmwex.DatasetApi()

try: 
    # List datasets
    api_response = api_instance.list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListResponseDataset**](ListResponseDataset.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status**
> IngestionStatusSummary status(dataset_id)

List dataset status

Display status information about an existing dataset.

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
api_instance = ibmwex.DatasetApi()
dataset_id = 'dataset_id_example' # str | The ID of the dataset.

try: 
    # List dataset status
    api_response = api_instance.status(dataset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset. | 

### Return type

[**IngestionStatusSummary**](IngestionStatusSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_all**
> ListResponseIngestionStatusSummary status_all()

List status for all datasets

Display status information about all existing datasets.

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
api_instance = ibmwex.DatasetApi()

try: 
    # List status for all datasets
    api_response = api_instance.status_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->status_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListResponseIngestionStatusSummary**](ListResponseIngestionStatusSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Dataset update(dataset_id, body)

Update a dataset

Updates an existing dataset.

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
api_instance = ibmwex.DatasetApi()
dataset_id = 'dataset_id_example' # str | The ID of the dataset.
body = ibmwex.Dataset() # Dataset | 

try: 
    # Update a dataset
    api_response = api_instance.update(dataset_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset. | 
 **body** | [**Dataset**](Dataset.md)|  | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_converter_pipeline**
> update_converter_pipeline(dataset_id, body)

Update converter pipeline

Updates an converter pipeline.

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
api_instance = ibmwex.DatasetApi()
dataset_id = 'dataset_id_example' # str | The ID of the dataset.
body = ibmwex.ConverterPipelineConfiguration() # ConverterPipelineConfiguration | 

try: 
    # Update converter pipeline
    api_instance.update_converter_pipeline(dataset_id, body)
except ApiException as e:
    print("Exception when calling DatasetApi->update_converter_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset. | 
 **body** | [**ConverterPipelineConfiguration**](ConverterPipelineConfiguration.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

