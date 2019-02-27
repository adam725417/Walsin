# ibmwex.ExplorationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query**](ExplorationApi.md#query) | **GET** /api/v1/explore/{collectionId}/query | Searches for documents
[**querymodifier**](ExplorationApi.md#querymodifier) | **GET** /api/v1/explore/{collectionId}/querymodifier | Searches for documents


# **query**
> QueryResult query(collection_id, q, start=start, rows=rows, lang=lang, sort=sort, fl=fl, facet=facet, facet_field=facet_field, facet_stats=facet_stats, facet_limit=facet_limit, rq=rq, qdocid=qdocid, qdoc=qdoc, wt=wt, facet_sentiment=facet_sentiment, csv_facet_attr=csv_facet_attr, csv_comment=csv_comment, rapi_file_encoding=rapi_file_encoding, rapi_file_name=rapi_file_name, date_format=date_format, tz=tz)

Searches for documents

Query syntax is based on [Apache Solr's Extended Dismax Query Parser](https://lucene.apache.org/solr/guide/7_3/the-extended-dismax-query-parser.html). Query response writer 'csv_facet' also use parameter in [CSV Parameters](https://lucene.apache.org/solr/guide/7_3/response-writers.html#csv-parameters) except csv.header and csv.null. 

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
api_instance = ibmwex.ExplorationApi()
collection_id = 'collection_id_example' # str | The ID of the collection.
q = 'q_example' # str | Query string
start = 56 # int | Position of the first result to return (optional)
rows = 56 # int | Determines the number of results to return for a single request (optional)
lang = 'lang_example' # str | Language used to analyze the query string. (optional)
sort = 'sort_example' # str | Specifies sort fields of search results in either ascending (asc) or descending (desc) order. For example, \"genre asc, price asc\" sorts by the contents of the genre field in descending order, then within those results sorts in ascending order by the contents of the price field. By default, relevancy is used as the only sort key. (optional)
fl = 'fl_example' # str | Specifies the information included in a query response to a list of fields. Fields should be separated by commas. (optional)
facet = 'facet_example' # str | Flag to return facets or not. (optional)
facet_field = ['facet_field_example'] # list[str] | Facet names to return. (optional)
facet_stats = 'facet_stats_example' # str | Facet statistics to be returned. (optional)
facet_limit = 56 # int | Number of facet values to return for each facet field. (optional)
rq = 'rq_example' # str | Specify query string used for result re-ranking. For example, to enable structured simlar document search, specify \"{!sss}\". (optional)
qdocid = 'qdocid_example' # str | Specify an existing indexed document id for similar document search. (optional)
qdoc = 'qdoc_example' # str | Specify a document JSON for similar document search. The format of searched document must be compliant to NLP API format. (optional)
wt = 'wt_example' # str | Type of [QueryResponseWriter](https://wiki.apache.org/solr/QueryResponseWriter) (optional)
facet_sentiment = true # bool | Enable sentiment analysis if available (optional)
csv_facet_attr = ['csv_facet_attr_example'] # list[str] | wt=csv_facet only: Limitting table of facet attributes. By default, export everything. ```sentiment_*``` only available if ```facet.sentiment``` is enabled.  (optional)
csv_comment = 'csv_comment_example' # str | wt=csv_facet only: Comment character in CSV file. By default, no comments will be in CSV file.  (optional)
rapi_file_encoding = 'rapi_file_encoding_example' # str | wt=csv_facet only: Encoding of CSV file. Default is UTF-8  (optional)
rapi_file_name = 'rapi_file_name_example' # str | wt=csv_facet only: Additional response header will be added. ```Content-Disposition: attachment;filename=\"rapi.file.name\"```  (optional)
date_format = 'date_format_example' # str | wt=csv_facet only: Valid pattern of ```java.time.format.DateTimeFormatter```  (optional)
tz = 'tz_example' # str | Valid time zone of ```java.time.ZoneId``` (optional)

try: 
    # Searches for documents
    api_response = api_instance.query(collection_id, q, start=start, rows=rows, lang=lang, sort=sort, fl=fl, facet=facet, facet_field=facet_field, facet_stats=facet_stats, facet_limit=facet_limit, rq=rq, qdocid=qdocid, qdoc=qdoc, wt=wt, facet_sentiment=facet_sentiment, csv_facet_attr=csv_facet_attr, csv_comment=csv_comment, rapi_file_encoding=rapi_file_encoding, rapi_file_name=rapi_file_name, date_format=date_format, tz=tz)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExplorationApi->query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The ID of the collection. | 
 **q** | **str**| Query string | 
 **start** | **int**| Position of the first result to return | [optional] 
 **rows** | **int**| Determines the number of results to return for a single request | [optional] 
 **lang** | **str**| Language used to analyze the query string. | [optional] 
 **sort** | **str**| Specifies sort fields of search results in either ascending (asc) or descending (desc) order. For example, \&quot;genre asc, price asc\&quot; sorts by the contents of the genre field in descending order, then within those results sorts in ascending order by the contents of the price field. By default, relevancy is used as the only sort key. | [optional] 
 **fl** | **str**| Specifies the information included in a query response to a list of fields. Fields should be separated by commas. | [optional] 
 **facet** | **str**| Flag to return facets or not. | [optional] 
 **facet_field** | [**list[str]**](str.md)| Facet names to return. | [optional] 
 **facet_stats** | **str**| Facet statistics to be returned. | [optional] 
 **facet_limit** | **int**| Number of facet values to return for each facet field. | [optional] 
 **rq** | **str**| Specify query string used for result re-ranking. For example, to enable structured simlar document search, specify \&quot;{!sss}\&quot;. | [optional] 
 **qdocid** | **str**| Specify an existing indexed document id for similar document search. | [optional] 
 **qdoc** | **str**| Specify a document JSON for similar document search. The format of searched document must be compliant to NLP API format. | [optional] 
 **wt** | **str**| Type of [QueryResponseWriter](https://wiki.apache.org/solr/QueryResponseWriter) | [optional] 
 **facet_sentiment** | **bool**| Enable sentiment analysis if available | [optional] 
 **csv_facet_attr** | [**list[str]**](str.md)| wt&#x3D;csv_facet only: Limitting table of facet attributes. By default, export everything. &#x60;&#x60;&#x60;sentiment_*&#x60;&#x60;&#x60; only available if &#x60;&#x60;&#x60;facet.sentiment&#x60;&#x60;&#x60; is enabled.  | [optional] 
 **csv_comment** | **str**| wt&#x3D;csv_facet only: Comment character in CSV file. By default, no comments will be in CSV file.  | [optional] 
 **rapi_file_encoding** | **str**| wt&#x3D;csv_facet only: Encoding of CSV file. Default is UTF-8  | [optional] 
 **rapi_file_name** | **str**| wt&#x3D;csv_facet only: Additional response header will be added. &#x60;&#x60;&#x60;Content-Disposition: attachment;filename&#x3D;\&quot;rapi.file.name\&quot;&#x60;&#x60;&#x60;  | [optional] 
 **date_format** | **str**| wt&#x3D;csv_facet only: Valid pattern of &#x60;&#x60;&#x60;java.time.format.DateTimeFormatter&#x60;&#x60;&#x60;  | [optional] 
 **tz** | **str**| Valid time zone of &#x60;&#x60;&#x60;java.time.ZoneId&#x60;&#x60;&#x60; | [optional] 

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **querymodifier**
> querymodifier(collection_id, q, lang=lang, querymodifier_minimum_required_terms=querymodifier_minimum_required_terms)

Searches for documents

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
api_instance = ibmwex.ExplorationApi()
collection_id = 'collection_id_example' # str | The ID of the collection.
q = 'q_example' # str | Query string to be modified
lang = 'lang_example' # str | Language used to analyze the query string (optional)
querymodifier_minimum_required_terms = 56 # int | Threshold to converts AND operators into OR operators, if the modified query has more terms than this threshold (optional)

try: 
    # Searches for documents
    api_instance.querymodifier(collection_id, q, lang=lang, querymodifier_minimum_required_terms=querymodifier_minimum_required_terms)
except ApiException as e:
    print("Exception when calling ExplorationApi->querymodifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The ID of the collection. | 
 **q** | **str**| Query string to be modified | 
 **lang** | **str**| Language used to analyze the query string | [optional] 
 **querymodifier_minimum_required_terms** | **int**| Threshold to converts AND operators into OR operators, if the modified query has more terms than this threshold | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

