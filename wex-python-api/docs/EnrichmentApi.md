# ibmwex.EnrichmentApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](EnrichmentApi.md#create) | **POST** /api/v1/enrichments | Create an enrichment
[**create_facet_dictionary**](EnrichmentApi.md#create_facet_dictionary) | **POST** /api/v1/enrichments/{enrichmentId}/fdics | Create a dictionary
[**create_from_pear**](EnrichmentApi.md#create_from_pear) | **POST** /api/v1/enrichments#pear | Create an enrichment from pear file
[**delete**](EnrichmentApi.md#delete) | **DELETE** /api/v1/enrichments/{enrichmentId} | Delete an enrichment
[**get**](EnrichmentApi.md#get) | **GET** /api/v1/enrichments/{enrichmentId} | List enrichment details
[**get_facet_dictionary**](EnrichmentApi.md#get_facet_dictionary) | **GET** /api/v1/enrichments/{enrichmentId}/fdics/{dictionaryId} | List dictionary details
[**get_facet_dictionary_content**](EnrichmentApi.md#get_facet_dictionary_content) | **GET** /api/v1/enrichments/{enrichmentId}/fdics/{dictionaryId}/content | Fetch a dictionary content
[**get_reg_ex_config**](EnrichmentApi.md#get_reg_ex_config) | **GET** /api/v1/enrichments/{enrichmentId}/regexconfig | Get the regular expression annotator rules
[**list**](EnrichmentApi.md#list) | **GET** /api/v1/enrichments | List enrichments
[**list_facet_dictionaries**](EnrichmentApi.md#list_facet_dictionaries) | **GET** /api/v1/enrichments/{enrichmentId}/fdics | List dictionaries
[**remove_facet_dictionary**](EnrichmentApi.md#remove_facet_dictionary) | **DELETE** /api/v1/enrichments/{enrichmentId}/fdics/{dictionaryId} | Remove a dictionary
[**update**](EnrichmentApi.md#update) | **PUT** /api/v1/enrichments/{enrichmentId} | Update an enrichment
[**update_facet_dictionary**](EnrichmentApi.md#update_facet_dictionary) | **PUT** /api/v1/enrichments/{enrichmentId}/fdics/{dictionaryId} | Update a dictionary
[**update_facet_dictionary_content**](EnrichmentApi.md#update_facet_dictionary_content) | **PUT** /api/v1/enrichments/{enrichmentId}/fdics/{dictionaryId}/content | Update a dictionary content
[**update_reg_ex_config**](EnrichmentApi.md#update_reg_ex_config) | **PUT** /api/v1/enrichments/{enrichmentId}/regexconfig | Create or update regular expression annotator rules


# **create**
> Enrichment create(body)

Create an enrichment

Creates a new enrichment

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
api_instance = ibmwex.EnrichmentApi()
body = ibmwex.Enrichment() # Enrichment | 

try: 
    # Create an enrichment
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrichmentApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Enrichment**](Enrichment.md)|  | 

### Return type

[**Enrichment**](Enrichment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_facet_dictionary**
> FileResource create_facet_dictionary(enrichment_id, body)

Create a dictionary

Creates a new dictionary

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
api_instance = ibmwex.EnrichmentApi()
enrichment_id = 'enrichment_id_example' # str | The ID of the enrichment.
body = ibmwex.FileResource() # FileResource | 

try: 
    # Create a dictionary
    api_response = api_instance.create_facet_dictionary(enrichment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrichmentApi->create_facet_dictionary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrichment_id** | **str**| The ID of the enrichment. | 
 **body** | [**FileResource**](FileResource.md)|  | 

### Return type

[**FileResource**](FileResource.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_from_pear**
> Enrichment create_from_pear(file, name=name)

Create an enrichment from pear file

Create a new enrichment from pear file created by Studio.

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
api_instance = ibmwex.EnrichmentApi()
file = '/path/to/file.txt' # file | 
name = 'name_example' # str |  (optional)

try: 
    # Create an enrichment from pear file
    api_response = api_instance.create_from_pear(file, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrichmentApi->create_from_pear: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**|  | 
 **name** | **str**|  | [optional] 

### Return type

[**Enrichment**](Enrichment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> SimpleResponse delete(enrichment_id)

Delete an enrichment

Deletes an existing enrichment.

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
api_instance = ibmwex.EnrichmentApi()
enrichment_id = 'enrichment_id_example' # str | The ID of the enrichment.

try: 
    # Delete an enrichment
    api_response = api_instance.delete(enrichment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrichmentApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrichment_id** | **str**| The ID of the enrichment. | 

### Return type

[**SimpleResponse**](SimpleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Enrichment get(enrichment_id)

List enrichment details

Display detailed information about an existing enrichment.

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
api_instance = ibmwex.EnrichmentApi()
enrichment_id = 'enrichment_id_example' # str | The ID of the enrichment.

try: 
    # List enrichment details
    api_response = api_instance.get(enrichment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrichmentApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrichment_id** | **str**| The ID of the enrichment. | 

### Return type

[**Enrichment**](Enrichment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facet_dictionary**
> FileResource get_facet_dictionary(enrichment_id, dictionary_id)

List dictionary details

Display detailed information about an existing dictionary.

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
api_instance = ibmwex.EnrichmentApi()
enrichment_id = 'enrichment_id_example' # str | The ID of the enrichment.
dictionary_id = 'dictionary_id_example' # str | The ID of the dictionary.

try: 
    # List dictionary details
    api_response = api_instance.get_facet_dictionary(enrichment_id, dictionary_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrichmentApi->get_facet_dictionary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrichment_id** | **str**| The ID of the enrichment. | 
 **dictionary_id** | **str**| The ID of the dictionary. | 

### Return type

[**FileResource**](FileResource.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facet_dictionary_content**
> FacetDictionary get_facet_dictionary_content(enrichment_id, dictionary_id)

Fetch a dictionary content

Fetches a content of an existing dictionary.

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
api_instance = ibmwex.EnrichmentApi()
enrichment_id = 'enrichment_id_example' # str | The ID of the enrichment.
dictionary_id = 'dictionary_id_example' # str | The ID of the dictionary.

try: 
    # Fetch a dictionary content
    api_response = api_instance.get_facet_dictionary_content(enrichment_id, dictionary_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrichmentApi->get_facet_dictionary_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrichment_id** | **str**| The ID of the enrichment. | 
 **dictionary_id** | **str**| The ID of the dictionary. | 

### Return type

[**FacetDictionary**](FacetDictionary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reg_ex_config**
> RegExConfig get_reg_ex_config(enrichment_id)

Get the regular expression annotator rules

Get the regular expression annotator rules, the enrichment must be in type regex

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
api_instance = ibmwex.EnrichmentApi()
enrichment_id = 'enrichment_id_example' # str | The ID of the enrichment.

try: 
    # Get the regular expression annotator rules
    api_response = api_instance.get_reg_ex_config(enrichment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrichmentApi->get_reg_ex_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrichment_id** | **str**| The ID of the enrichment. | 

### Return type

[**RegExConfig**](RegExConfig.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ListResponseEnrichment list()

List enrichments

Display a list of existing enrichments.

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
api_instance = ibmwex.EnrichmentApi()

try: 
    # List enrichments
    api_response = api_instance.list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrichmentApi->list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListResponseEnrichment**](ListResponseEnrichment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_facet_dictionaries**
> ListResponseFileResource list_facet_dictionaries(enrichment_id)

List dictionaries

Display a list of IDs of existing dictionaries.

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
api_instance = ibmwex.EnrichmentApi()
enrichment_id = 'enrichment_id_example' # str | The ID of the enrichment.

try: 
    # List dictionaries
    api_response = api_instance.list_facet_dictionaries(enrichment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrichmentApi->list_facet_dictionaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrichment_id** | **str**| The ID of the enrichment. | 

### Return type

[**ListResponseFileResource**](ListResponseFileResource.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_facet_dictionary**
> SimpleResponse remove_facet_dictionary(enrichment_id, dictionary_id)

Remove a dictionary

Removes an existing dictionary from collection.

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
api_instance = ibmwex.EnrichmentApi()
enrichment_id = 'enrichment_id_example' # str | The ID of the enrichment.
dictionary_id = 'dictionary_id_example' # str | The ID of the dictionary.

try: 
    # Remove a dictionary
    api_response = api_instance.remove_facet_dictionary(enrichment_id, dictionary_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrichmentApi->remove_facet_dictionary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrichment_id** | **str**| The ID of the enrichment. | 
 **dictionary_id** | **str**| The ID of the dictionary. | 

### Return type

[**SimpleResponse**](SimpleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Enrichment update(enrichment_id, body)

Update an enrichment

Updates an existing enrichment

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
api_instance = ibmwex.EnrichmentApi()
enrichment_id = 'enrichment_id_example' # str | The ID of the enrichment.
body = ibmwex.Enrichment() # Enrichment | 

try: 
    # Update an enrichment
    api_response = api_instance.update(enrichment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrichmentApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrichment_id** | **str**| The ID of the enrichment. | 
 **body** | [**Enrichment**](Enrichment.md)|  | 

### Return type

[**Enrichment**](Enrichment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_facet_dictionary**
> FileResource update_facet_dictionary(enrichment_id, dictionary_id, body)

Update a dictionary

Updates an existing dictionary of collection.

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
api_instance = ibmwex.EnrichmentApi()
enrichment_id = 'enrichment_id_example' # str | The ID of the enrichment.
dictionary_id = 'dictionary_id_example' # str | The ID of the dictionary.
body = ibmwex.FileResource() # FileResource | 

try: 
    # Update a dictionary
    api_response = api_instance.update_facet_dictionary(enrichment_id, dictionary_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrichmentApi->update_facet_dictionary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrichment_id** | **str**| The ID of the enrichment. | 
 **dictionary_id** | **str**| The ID of the dictionary. | 
 **body** | [**FileResource**](FileResource.md)|  | 

### Return type

[**FileResource**](FileResource.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_facet_dictionary_content**
> FacetDictionary update_facet_dictionary_content(enrichment_id, dictionary_id, body)

Update a dictionary content

Updates a content of an existing dictionary.

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
api_instance = ibmwex.EnrichmentApi()
enrichment_id = 'enrichment_id_example' # str | The ID of the enrichment.
dictionary_id = 'dictionary_id_example' # str | The ID of the dictionary.
body = ibmwex.FacetDictionary() # FacetDictionary | 

try: 
    # Update a dictionary content
    api_response = api_instance.update_facet_dictionary_content(enrichment_id, dictionary_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrichmentApi->update_facet_dictionary_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrichment_id** | **str**| The ID of the enrichment. | 
 **dictionary_id** | **str**| The ID of the dictionary. | 
 **body** | [**FacetDictionary**](FacetDictionary.md)|  | 

### Return type

[**FacetDictionary**](FacetDictionary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_reg_ex_config**
> RegExConfig update_reg_ex_config(enrichment_id, body)

Create or update regular expression annotator rules

Create or update regular expression annotator rules, the enrichment must be in type regex

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
api_instance = ibmwex.EnrichmentApi()
enrichment_id = 'enrichment_id_example' # str | The ID of the enrichment.
body = ibmwex.RegExConfig() # RegExConfig | 

try: 
    # Create or update regular expression annotator rules
    api_response = api_instance.update_reg_ex_config(enrichment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrichmentApi->update_reg_ex_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrichment_id** | **str**| The ID of the enrichment. | 
 **body** | [**RegExConfig**](RegExConfig.md)|  | 

### Return type

[**RegExConfig**](RegExConfig.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

