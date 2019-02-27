# ibmwex.ImporterApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_csv**](ImporterApi.md#add_csv) | **PUT** /api/v1/importer/csv/upload/{uploadId} | Add a CSV file
[**create**](ImporterApi.md#create) | **POST** /api/v1/datasets/{datasetId}/importers | Create an importer
[**delete**](ImporterApi.md#delete) | **DELETE** /api/v1/datasets/{datasetId}/importers/{importerId} | Delete an importer
[**delete_csv**](ImporterApi.md#delete_csv) | **DELETE** /api/v1/importer/csv/upload/{uploadId}/{fileName} | Delete a CSV file
[**get**](ImporterApi.md#get) | **GET** /api/v1/datasets/{datasetId}/importers/{importerId} | List importer details
[**get_configuration_template**](ImporterApi.md#get_configuration_template) | **GET** /api/v1/importer/types/{importerType} | List importer configuration
[**get_types**](ImporterApi.md#get_types) | **GET** /api/v1/importer/types | List importer types
[**list**](ImporterApi.md#list) | **GET** /api/v1/datasets/{datasetId}/importers | List importers
[**list_csv**](ImporterApi.md#list_csv) | **GET** /api/v1/importer/csv/upload/{uploadId} | List CSV files
[**preview_csv**](ImporterApi.md#preview_csv) | **POST** /api/v1/importer/csv/preview/{uploadId}/{fileName} | Preview CSV file
[**start**](ImporterApi.md#start) | **POST** /api/v1/datasets/{datasetId}/importers/{importerId}/start | Start an importer
[**status**](ImporterApi.md#status) | **GET** /api/v1/datasets/{datasetId}/importers/{importerId}/status | List importer status
[**stop**](ImporterApi.md#stop) | **POST** /api/v1/datasets/{datasetId}/importers/{importerId}/stop | Stop an importer
[**update**](ImporterApi.md#update) | **PUT** /api/v1/datasets/{datasetId}/importers/{importerId} | Update an importer
[**upload_csv**](ImporterApi.md#upload_csv) | **POST** /api/v1/importer/csv/upload | Upload CSV file


# **add_csv**
> UploadResult add_csv(upload_id, file)

Add a CSV file

Uploads a new CSV file.

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
api_instance = ibmwex.ImporterApi()
upload_id = 'upload_id_example' # str | The ID of the upload request.
file = '/path/to/file.txt' # file | 

try: 
    # Add a CSV file
    api_response = api_instance.add_csv(upload_id, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterApi->add_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**| The ID of the upload request. | 
 **file** | **file**|  | 

### Return type

[**UploadResult**](UploadResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> Importer create(dataset_id, body)

Create an importer

Creates a new importer.

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
api_instance = ibmwex.ImporterApi()
dataset_id = 'dataset_id_example' # str | The ID of the dataset.
body = ibmwex.CrawlerConfiguration() # CrawlerConfiguration | 

try: 
    # Create an importer
    api_response = api_instance.create(dataset_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset. | 
 **body** | [**CrawlerConfiguration**](CrawlerConfiguration.md)|  | 

### Return type

[**Importer**](Importer.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> SimpleResponse delete(dataset_id, importer_id)

Delete an importer

Deletes an existing importer.

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
api_instance = ibmwex.ImporterApi()
dataset_id = 'dataset_id_example' # str | The ID of the dataset.
importer_id = 'importer_id_example' # str | The ID of the importer.

try: 
    # Delete an importer
    api_response = api_instance.delete(dataset_id, importer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset. | 
 **importer_id** | **str**| The ID of the importer. | 

### Return type

[**SimpleResponse**](SimpleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_csv**
> delete_csv(upload_id, file_name)

Delete a CSV file

Deletes an uploaded CSV file.

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
api_instance = ibmwex.ImporterApi()
upload_id = 'upload_id_example' # str | The ID of the upload request.
file_name = 'file_name_example' # str | The name of file.

try: 
    # Delete a CSV file
    api_instance.delete_csv(upload_id, file_name)
except ApiException as e:
    print("Exception when calling ImporterApi->delete_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**| The ID of the upload request. | 
 **file_name** | **str**| The name of file. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> CrawlerConfiguration get(dataset_id, importer_id)

List importer details

Display detailed information about an existing importer.

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
api_instance = ibmwex.ImporterApi()
dataset_id = 'dataset_id_example' # str | The ID of the dataset.
importer_id = 'importer_id_example' # str | The ID of the importer.

try: 
    # List importer details
    api_response = api_instance.get(dataset_id, importer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset. | 
 **importer_id** | **str**| The ID of the importer. | 

### Return type

[**CrawlerConfiguration**](CrawlerConfiguration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration_template**
> ConfigurationTemplate get_configuration_template(importer_type)

List importer configuration

Displays a list of configuration parameter of importer.

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
api_instance = ibmwex.ImporterApi()
importer_type = 'importer_type_example' # str | The type of importer.

try: 
    # List importer configuration
    api_response = api_instance.get_configuration_template(importer_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterApi->get_configuration_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **importer_type** | **str**| The type of importer. | 

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

List importer types

Display a list of available importer types.

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
api_instance = ibmwex.ImporterApi()

try: 
    # List importer types
    api_response = api_instance.get_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterApi->get_types: %s\n" % e)
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
> ListResponseImporter list(dataset_id)

List importers

Display a list of existing importers.

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
api_instance = ibmwex.ImporterApi()
dataset_id = 'dataset_id_example' # str | The ID of the dataset.

try: 
    # List importers
    api_response = api_instance.list(dataset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset. | 

### Return type

[**ListResponseImporter**](ListResponseImporter.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_csv**
> UploadResult list_csv(upload_id)

List CSV files

Display a list of uploaded CSV files.

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
api_instance = ibmwex.ImporterApi()
upload_id = 'upload_id_example' # str | The ID of the upload request.

try: 
    # List CSV files
    api_response = api_instance.list_csv(upload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterApi->list_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**| The ID of the upload request. | 

### Return type

[**UploadResult**](UploadResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_csv**
> PreviewResult preview_csv(upload_id, file_name, body)

Preview CSV file

Display a preview of a CSV file.

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
api_instance = ibmwex.ImporterApi()
upload_id = 'upload_id_example' # str | The ID of the upload request.
file_name = 'file_name_example' # str | The name of file.
body = ibmwex.CrawlerConfiguration() # CrawlerConfiguration | 

try: 
    # Preview CSV file
    api_response = api_instance.preview_csv(upload_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterApi->preview_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**| The ID of the upload request. | 
 **file_name** | **str**| The name of file. | 
 **body** | [**CrawlerConfiguration**](CrawlerConfiguration.md)|  | 

### Return type

[**PreviewResult**](PreviewResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start**
> start(dataset_id, importer_id)

Start an importer

Starts ingesting documents with an importer.

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
api_instance = ibmwex.ImporterApi()
dataset_id = 'dataset_id_example' # str | The ID of the dataset.
importer_id = 'importer_id_example' # str | The ID of the importer.

try: 
    # Start an importer
    api_instance.start(dataset_id, importer_id)
except ApiException as e:
    print("Exception when calling ImporterApi->start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset. | 
 **importer_id** | **str**| The ID of the importer. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status**
> ZkIngestionStatus status(dataset_id, importer_id)

List importer status

Displays status information about an existing importer.

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
api_instance = ibmwex.ImporterApi()
dataset_id = 'dataset_id_example' # str | The ID of the dataset.
importer_id = 'importer_id_example' # str | The ID of the importer.

try: 
    # List importer status
    api_response = api_instance.status(dataset_id, importer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterApi->status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset. | 
 **importer_id** | **str**| The ID of the importer. | 

### Return type

[**ZkIngestionStatus**](ZkIngestionStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop**
> stop(dataset_id, importer_id)

Stop an importer

Stops ingesting documents with an importer.

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
api_instance = ibmwex.ImporterApi()
dataset_id = 'dataset_id_example' # str | The ID of the dataset.
importer_id = 'importer_id_example' # str | The ID of the importer.

try: 
    # Stop an importer
    api_instance.stop(dataset_id, importer_id)
except ApiException as e:
    print("Exception when calling ImporterApi->stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset. | 
 **importer_id** | **str**| The ID of the importer. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Importer update(dataset_id, importer_id, body)

Update an importer

Updates an existing importer.

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
api_instance = ibmwex.ImporterApi()
dataset_id = 'dataset_id_example' # str | The ID of the dataset.
importer_id = 'importer_id_example' # str | The ID of the importer.
body = ibmwex.CrawlerConfiguration() # CrawlerConfiguration | 

try: 
    # Update an importer
    api_response = api_instance.update(dataset_id, importer_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | **str**| The ID of the dataset. | 
 **importer_id** | **str**| The ID of the importer. | 
 **body** | [**CrawlerConfiguration**](CrawlerConfiguration.md)|  | 

### Return type

[**Importer**](Importer.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_csv**
> UploadResult upload_csv(file)

Upload CSV file

Upload a CSV file.

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
api_instance = ibmwex.ImporterApi()
file = '/path/to/file.txt' # file | 

try: 
    # Upload CSV file
    api_response = api_instance.upload_csv(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImporterApi->upload_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**|  | 

### Return type

[**UploadResult**](UploadResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

