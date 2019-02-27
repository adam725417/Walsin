# ibmwex.SimilarDocumentRankerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_model_training**](SimilarDocumentRankerApi.md#cancel_model_training) | **DELETE** /api/v1/sdrankers/{rankerId}/models/{modelId}/task | Cancel ranker model training task
[**create**](SimilarDocumentRankerApi.md#create) | **POST** /api/v1/sdrankers | Create a similar document ranker
[**create_collection**](SimilarDocumentRankerApi.md#create_collection) | **POST** /api/v1/sdrankers/{rankerId}/collection | Create and set a collection
[**create_model_from_source_dataset**](SimilarDocumentRankerApi.md#create_model_from_source_dataset) | **POST** /api/v1/sdrankers/{rankerId}/models/all | Create a similar document ranker model
[**delete**](SimilarDocumentRankerApi.md#delete) | **DELETE** /api/v1/sdrankers/{rankerId} | Delete a ranker
[**get**](SimilarDocumentRankerApi.md#get) | **GET** /api/v1/sdrankers/{rankerId} | Show similar document ranker details
[**get_instances**](SimilarDocumentRankerApi.md#get_instances) | **GET** /api/v1/sdrankers/{rankerId}/models/{modelId}/instances | List ranker instances where the model deployed
[**get_instances_latest**](SimilarDocumentRankerApi.md#get_instances_latest) | **GET** /api/v1/sdrankers/{rankerId}/models/latest/instances | List ranker instances where the latest ranker model deployed
[**get_model**](SimilarDocumentRankerApi.md#get_model) | **GET** /api/v1/sdrankers/{rankerId}/models/{modelId} | Show similar document ranker model details
[**get_model_latest**](SimilarDocumentRankerApi.md#get_model_latest) | **GET** /api/v1/sdrankers/{rankerId}/models/latest | Show the latest similar document ranker model details
[**get_model_status**](SimilarDocumentRankerApi.md#get_model_status) | **GET** /api/v1/sdrankers/{rankerId}/models/{modelId}/status | Show ranker model status
[**get_resource_set**](SimilarDocumentRankerApi.md#get_resource_set) | **GET** /api/v1/sdrankers/{rankerId}/resources/{resourceSetId} | Show ranker resource set details
[**get_test_evals**](SimilarDocumentRankerApi.md#get_test_evals) | **GET** /api/v1/sdrankers/{rankerId}/test-evals | List ranking evaluation results
[**get_test_rank_eval**](SimilarDocumentRankerApi.md#get_test_rank_eval) | **GET** /api/v1/sdrankers/{rankerId}/models/{modelId}/test-rank | Show ranking evaluation result of the model
[**list**](SimilarDocumentRankerApi.md#list) | **GET** /api/v1/sdrankers | List similar document rankers
[**set_model**](SimilarDocumentRankerApi.md#set_model) | **PUT** /api/v1/sdrankers/{rankerId}/models | Set a similar document ranker model
[**set_resource_set**](SimilarDocumentRankerApi.md#set_resource_set) | **PUT** /api/v1/sdrankers/{rankerId}/resources | Set a ranker resource set
[**update**](SimilarDocumentRankerApi.md#update) | **PUT** /api/v1/sdrankers/{rankerId} | Update a similar document ranker


# **cancel_model_training**
> SimpleResponse cancel_model_training(ranker_id, model_id)

Cancel ranker model training task

Cancel ranker model training task

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
api_instance = ibmwex.SimilarDocumentRankerApi()
ranker_id = 'ranker_id_example' # str | The ID of the ranker.
model_id = 'model_id_example' # str | The ID of the model.

try: 
    # Cancel ranker model training task
    api_response = api_instance.cancel_model_training(ranker_id, model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimilarDocumentRankerApi->cancel_model_training: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ranker_id** | **str**| The ID of the ranker. | 
 **model_id** | **str**| The ID of the model. | 

### Return type

[**SimpleResponse**](SimpleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> SDRanker create(body)

Create a similar document ranker

Create a new similar document ranker

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
api_instance = ibmwex.SimilarDocumentRankerApi()
body = ibmwex.InitSDRanker() # InitSDRanker | 

try: 
    # Create a similar document ranker
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimilarDocumentRankerApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InitSDRanker**](InitSDRanker.md)|  | 

### Return type

[**SDRanker**](SDRanker.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_collection**
> Collection create_collection(ranker_id, body)

Create and set a collection

Create a collection to process the source dataset of the ranker

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
api_instance = ibmwex.SimilarDocumentRankerApi()
ranker_id = 'ranker_id_example' # str | The ID of the ranker.
body = ibmwex.MLCollection() # MLCollection | 

try: 
    # Create and set a collection
    api_response = api_instance.create_collection(ranker_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimilarDocumentRankerApi->create_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ranker_id** | **str**| The ID of the ranker. | 
 **body** | [**MLCollection**](MLCollection.md)|  | 

### Return type

[**Collection**](Collection.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_model_from_source_dataset**
> ClassifierModel create_model_from_source_dataset(ranker_id, body, resource_name=resource_name, model_name=model_name)

Create a similar document ranker model

Create and train a ranker model by separating the source training dataset into training, validation, and test sets Parameters used in training process can be set by adding config parameter of body *Example* For controlling training process   name | description  ---- | -----------  flag.batch_size | Int value. Batch size of examples per step  flag.max_steps | Int value. Max number of step for training  flag.val_monitor_every_n_steps |Int value. Step interval between validation  flag.val_monitor_early_stopping_rounds | Int value. Number of retry until cancel training (early stopping)

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
api_instance = ibmwex.SimilarDocumentRankerApi()
ranker_id = 'ranker_id_example' # str | The ID of the ranker.
body = ibmwex.InitDatasetConfig() # InitDatasetConfig | Configuration to split the source training dataset
resource_name = 'resource_name_example' # str | Name of the resource set created by this method (optional)
model_name = 'model_name_example' # str | Name of the model created by this method (optional)

try: 
    # Create a similar document ranker model
    api_response = api_instance.create_model_from_source_dataset(ranker_id, body, resource_name=resource_name, model_name=model_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimilarDocumentRankerApi->create_model_from_source_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ranker_id** | **str**| The ID of the ranker. | 
 **body** | [**InitDatasetConfig**](InitDatasetConfig.md)| Configuration to split the source training dataset | 
 **resource_name** | **str**| Name of the resource set created by this method | [optional] 
 **model_name** | **str**| Name of the model created by this method | [optional] 

### Return type

[**ClassifierModel**](ClassifierModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> SimpleResponse delete(ranker_id)

Delete a ranker

Delete an existing ranker

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
api_instance = ibmwex.SimilarDocumentRankerApi()
ranker_id = 'ranker_id_example' # str | The ID of the ranker.

try: 
    # Delete a ranker
    api_response = api_instance.delete(ranker_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimilarDocumentRankerApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ranker_id** | **str**| The ID of the ranker. | 

### Return type

[**SimpleResponse**](SimpleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> SDRanker get(ranker_id)

Show similar document ranker details

Show detailed information of an existing ranker

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
api_instance = ibmwex.SimilarDocumentRankerApi()
ranker_id = 'ranker_id_example' # str | The ID of the ranker.

try: 
    # Show similar document ranker details
    api_response = api_instance.get(ranker_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimilarDocumentRankerApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ranker_id** | **str**| The ID of the ranker. | 

### Return type

[**SDRanker**](SDRanker.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instances**
> ListResponseString get_instances(ranker_id, model_id)

List ranker instances where the model deployed

Show IDs of ranker instances where the specified model deployed.

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
api_instance = ibmwex.SimilarDocumentRankerApi()
ranker_id = 'ranker_id_example' # str | The ID of the ranker.
model_id = 'model_id_example' # str | The ID of the model.

try: 
    # List ranker instances where the model deployed
    api_response = api_instance.get_instances(ranker_id, model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimilarDocumentRankerApi->get_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ranker_id** | **str**| The ID of the ranker. | 
 **model_id** | **str**| The ID of the model. | 

### Return type

[**ListResponseString**](ListResponseString.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instances_latest**
> ListResponseString get_instances_latest(ranker_id)

List ranker instances where the latest ranker model deployed

Show IDs of enrichments where the latest ranker model deployed.

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
api_instance = ibmwex.SimilarDocumentRankerApi()
ranker_id = 'ranker_id_example' # str | The ID of the ranker.

try: 
    # List ranker instances where the latest ranker model deployed
    api_response = api_instance.get_instances_latest(ranker_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimilarDocumentRankerApi->get_instances_latest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ranker_id** | **str**| The ID of the ranker. | 

### Return type

[**ListResponseString**](ListResponseString.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model**
> ClassifierModel get_model(ranker_id, model_id)

Show similar document ranker model details

Show detailed information of an existing ranker model

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
api_instance = ibmwex.SimilarDocumentRankerApi()
ranker_id = 'ranker_id_example' # str | The ID of the ranker.
model_id = 'model_id_example' # str | The ID of the model.

try: 
    # Show similar document ranker model details
    api_response = api_instance.get_model(ranker_id, model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimilarDocumentRankerApi->get_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ranker_id** | **str**| The ID of the ranker. | 
 **model_id** | **str**| The ID of the model. | 

### Return type

[**ClassifierModel**](ClassifierModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_latest**
> ClassifierModel get_model_latest(ranker_id)

Show the latest similar document ranker model details

Show detailed information of the latest model of the ranker

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
api_instance = ibmwex.SimilarDocumentRankerApi()
ranker_id = 'ranker_id_example' # str | The ID of the ranker.

try: 
    # Show the latest similar document ranker model details
    api_response = api_instance.get_model_latest(ranker_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimilarDocumentRankerApi->get_model_latest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ranker_id** | **str**| The ID of the ranker. | 

### Return type

[**ClassifierModel**](ClassifierModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_status**
> ClassifierModelStatus get_model_status(ranker_id, model_id)

Show ranker model status

Show status of the specified ranker model

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
api_instance = ibmwex.SimilarDocumentRankerApi()
ranker_id = 'ranker_id_example' # str | The ID of the ranker.
model_id = 'model_id_example' # str | The ID of the model.

try: 
    # Show ranker model status
    api_response = api_instance.get_model_status(ranker_id, model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimilarDocumentRankerApi->get_model_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ranker_id** | **str**| The ID of the ranker. | 
 **model_id** | **str**| The ID of the model. | 

### Return type

[**ClassifierModelStatus**](ClassifierModelStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_set**
> ResourceSet get_resource_set(ranker_id, resource_set_id)

Show ranker resource set details

Show detailed information of an existing ranker resource set

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
api_instance = ibmwex.SimilarDocumentRankerApi()
ranker_id = 'ranker_id_example' # str | The ID of the ranker.
resource_set_id = 'resource_set_id_example' # str | The ID of the resource set.

try: 
    # Show ranker resource set details
    api_response = api_instance.get_resource_set(ranker_id, resource_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimilarDocumentRankerApi->get_resource_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ranker_id** | **str**| The ID of the ranker. | 
 **resource_set_id** | **str**| The ID of the resource set. | 

### Return type

[**ResourceSet**](ResourceSet.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_evals**
> ListResponseRankerEvalResult get_test_evals(ranker_id)

List ranking evaluation results

List ranking evaluation results using the test dataset of all models of the specified ranker.

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
api_instance = ibmwex.SimilarDocumentRankerApi()
ranker_id = 'ranker_id_example' # str | The ID of the ranker.

try: 
    # List ranking evaluation results
    api_response = api_instance.get_test_evals(ranker_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimilarDocumentRankerApi->get_test_evals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ranker_id** | **str**| The ID of the ranker. | 

### Return type

[**ListResponseRankerEvalResult**](ListResponseRankerEvalResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_rank_eval**
> RankerEvalResult get_test_rank_eval(ranker_id, model_id)

Show ranking evaluation result of the model

Show ranking evaluation result of the specified ranker model using the test dataset.

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
api_instance = ibmwex.SimilarDocumentRankerApi()
ranker_id = 'ranker_id_example' # str | The ID of the ranker.
model_id = 'model_id_example' # str | The ID of the model.

try: 
    # Show ranking evaluation result of the model
    api_response = api_instance.get_test_rank_eval(ranker_id, model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimilarDocumentRankerApi->get_test_rank_eval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ranker_id** | **str**| The ID of the ranker. | 
 **model_id** | **str**| The ID of the model. | 

### Return type

[**RankerEvalResult**](RankerEvalResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ListResponseSDRanker list()

List similar document rankers

Display a list of existing similar document rankers

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
api_instance = ibmwex.SimilarDocumentRankerApi()

try: 
    # List similar document rankers
    api_response = api_instance.list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimilarDocumentRankerApi->list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListResponseSDRanker**](ListResponseSDRanker.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_model**
> ClassifierModel set_model(ranker_id, body)

Set a similar document ranker model

Set a ranker model to the ranker

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
api_instance = ibmwex.SimilarDocumentRankerApi()
ranker_id = 'ranker_id_example' # str | The ID of the ranker.
body = ibmwex.ClassifierModel() # ClassifierModel | 

try: 
    # Set a similar document ranker model
    api_response = api_instance.set_model(ranker_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimilarDocumentRankerApi->set_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ranker_id** | **str**| The ID of the ranker. | 
 **body** | [**ClassifierModel**](ClassifierModel.md)|  | 

### Return type

[**ClassifierModel**](ClassifierModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_resource_set**
> ResourceSet set_resource_set(ranker_id, body)

Set a ranker resource set

Set a ranker resource set

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
api_instance = ibmwex.SimilarDocumentRankerApi()
ranker_id = 'ranker_id_example' # str | The ID of the ranker.
body = ibmwex.ResourceSet() # ResourceSet | 

try: 
    # Set a ranker resource set
    api_response = api_instance.set_resource_set(ranker_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimilarDocumentRankerApi->set_resource_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ranker_id** | **str**| The ID of the ranker. | 
 **body** | [**ResourceSet**](ResourceSet.md)|  | 

### Return type

[**ResourceSet**](ResourceSet.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> SDRanker update(ranker_id, body)

Update a similar document ranker

Update an existing ranker

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
api_instance = ibmwex.SimilarDocumentRankerApi()
ranker_id = 'ranker_id_example' # str | The ID of the ranker.
body = ibmwex.SDRanker() # SDRanker | 

try: 
    # Update a similar document ranker
    api_response = api_instance.update(ranker_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimilarDocumentRankerApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ranker_id** | **str**| The ID of the ranker. | 
 **body** | [**SDRanker**](SDRanker.md)|  | 

### Return type

[**SDRanker**](SDRanker.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

