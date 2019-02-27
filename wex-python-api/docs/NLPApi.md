# ibmwex.NLPApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze**](NLPApi.md#analyze) | **POST** /api/v1/collections/{collectionId}/analyze | Analyze documents with enrichments of a specified collection


# **analyze**
> RichDocument analyze(collection_id, document=document)

Analyze documents with enrichments of a specified collection

Real-time NLP allows users to analyze their documents with enrichments of a specified collection. Results describe enriched document that will be stored when indexed (not during the call of this API).

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
api_instance = ibmwex.NLPApi()
collection_id = 'collection_id_example' # str | The ID of the collection.
document = ibmwex.NLPDocument() # NLPDocument | Set a document to analyze. Document has two fields, **fields** and metadata. You only need to deal with **fields** for analysis. Fields holds key-value pairs that a text or string value is associated with a field name of dataset used by a collection. Note that annotators will be processed basically against **analyzable** **text** **content** **fields**, which can be checked in enrichFieldGroups of collection configuration or in collection edition UI. The other types of fields can be used for another purpose. For example, a classifier can use those fields when it uses such fields as features.  (optional)

try: 
    # Analyze documents with enrichments of a specified collection
    api_response = api_instance.analyze(collection_id, document=document)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NLPApi->analyze: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The ID of the collection. | 
 **document** | [**NLPDocument**](NLPDocument.md)| Set a document to analyze. Document has two fields, **fields** and metadata. You only need to deal with **fields** for analysis. Fields holds key-value pairs that a text or string value is associated with a field name of dataset used by a collection. Note that annotators will be processed basically against **analyzable** **text** **content** **fields**, which can be checked in enrichFieldGroups of collection configuration or in collection edition UI. The other types of fields can be used for another purpose. For example, a classifier can use those fields when it uses such fields as features.  | [optional] 

### Return type

[**RichDocument**](RichDocument.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

