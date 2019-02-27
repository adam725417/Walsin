# ibmwex.MigrationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_cas_to_index**](MigrationApi.md#convert_cas_to_index) | **POST** /api/v1/migration/cas2index | Migrate CAS to index mapping file
[**convert_category_tree**](MigrationApi.md#convert_category_tree) | **POST** /api/v1/migration/category | Migrate category tree file
[**convert_csv_to_fdic**](MigrationApi.md#convert_csv_to_fdic) | **POST** /api/v1/migration/csv2fdic | Migrate dictionary CSV file
[**convert_fdic**](MigrationApi.md#convert_fdic) | **POST** /api/v1/migration/fdic | Migrate dictionary file


# **convert_cas_to_index**
> AnnotationIndexingSpecs convert_cas_to_index(body)

Migrate CAS to index mapping file

Convert common analysis structure to index mapping file.

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
api_instance = ibmwex.MigrationApi()
body = ibmwex.InputStream() # InputStream | 

try: 
    # Migrate CAS to index mapping file
    api_response = api_instance.convert_cas_to_index(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MigrationApi->convert_cas_to_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InputStream**](InputStream.md)|  | 

### Return type

[**AnnotationIndexingSpecs**](AnnotationIndexingSpecs.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_category_tree**
> Category convert_category_tree(body)

Migrate category tree file

Convert category_tree.xml file to Json format.

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
api_instance = ibmwex.MigrationApi()
body = ibmwex.InputStream() # InputStream | 

try: 
    # Migrate category tree file
    api_response = api_instance.convert_category_tree(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MigrationApi->convert_category_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InputStream**](InputStream.md)|  | 

### Return type

[**Category**](Category.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_csv_to_fdic**
> FacetDictionary convert_csv_to_fdic(body, facet, language=language, encoding=encoding, pos=pos, delimiters=delimiters, escape=escape)

Migrate dictionary CSV file

Convert the list of words in CSV file to Json format.

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
api_instance = ibmwex.MigrationApi()
body = ibmwex.InputStream() # InputStream | 
facet = 'facet_example' # str | 
language = 'language_example' # str |  (optional)
encoding = 'encoding_example' # str |  (optional)
pos = 'pos_example' # str |  (optional)
delimiters = 'delimiters_example' # str |  (optional)
escape = 'escape_example' # str |  (optional)

try: 
    # Migrate dictionary CSV file
    api_response = api_instance.convert_csv_to_fdic(body, facet, language=language, encoding=encoding, pos=pos, delimiters=delimiters, escape=escape)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MigrationApi->convert_csv_to_fdic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InputStream**](InputStream.md)|  | 
 **facet** | **str**|  | 
 **language** | **str**|  | [optional] 
 **encoding** | **str**|  | [optional] 
 **pos** | **str**|  | [optional] 
 **delimiters** | **str**|  | [optional] 
 **escape** | **str**|  | [optional] 

### Return type

[**FacetDictionary**](FacetDictionary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/csv
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_fdic**
> FacetDictionary convert_fdic(body)

Migrate dictionary file

Convert fdic xml file to Json format.

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
api_instance = ibmwex.MigrationApi()
body = ibmwex.InputStream() # InputStream | 

try: 
    # Migrate dictionary file
    api_response = api_instance.convert_fdic(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MigrationApi->convert_fdic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InputStream**](InputStream.md)|  | 

### Return type

[**FacetDictionary**](FacetDictionary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

