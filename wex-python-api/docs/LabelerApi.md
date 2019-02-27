# ibmwex.LabelerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_model_training**](LabelerApi.md#cancel_model_training) | **DELETE** /api/v1/labelers/{labelerId}/models/{modelId}/task | Cancel labeler model training task
[**create**](LabelerApi.md#create) | **POST** /api/v1/labelers | Create a labeler
[**create_collection**](LabelerApi.md#create_collection) | **POST** /api/v1/labelers/{labelerId}/collection | Create and set a collection
[**create_model_from_source_dataset**](LabelerApi.md#create_model_from_source_dataset) | **POST** /api/v1/labelers/{labelerId}/models/all | Create a labeler model
[**delete**](LabelerApi.md#delete) | **DELETE** /api/v1/labelers/{labelerId} | Delete a labeler
[**get**](LabelerApi.md#get) | **GET** /api/v1/labelers/{labelerId} | Show labeler details
[**get_enrichment**](LabelerApi.md#get_enrichment) | **GET** /api/v1/labelers/{labelerId}/models/{modelId}/enrichments | List enrichments where the labeler model deployed
[**get_enrichment_latest**](LabelerApi.md#get_enrichment_latest) | **GET** /api/v1/labelers/{labelerId}/models/latest/enrichments | List enrichments where the latest labeler model deployed
[**get_model**](LabelerApi.md#get_model) | **GET** /api/v1/labelers/{labelerId}/models/{modelId} | Show labeler model details
[**get_model_latest**](LabelerApi.md#get_model_latest) | **GET** /api/v1/labelers/{labelerId}/models/latest | Show the latest labeler model details
[**get_model_status**](LabelerApi.md#get_model_status) | **GET** /api/v1/labelers/{labelerId}/models/{modelId}/status | Show labeler model status
[**get_resource_set**](LabelerApi.md#get_resource_set) | **GET** /api/v1/labelers/{labelerId}/resources/{resourceSetId} | Show labeler resource set details
[**get_test_eval**](LabelerApi.md#get_test_eval) | **GET** /api/v1/labelers/{labelerId}/models/{modelId}/test | Show test evaluation result of the model
[**get_test_evals**](LabelerApi.md#get_test_evals) | **GET** /api/v1/labelers/{labelerId}/test-evals | List test evaluation results
[**get_validation_eval**](LabelerApi.md#get_validation_eval) | **GET** /api/v1/labelers/{labelerId}/models/{modelId}/validation | Show validation evaluation result of the model
[**list**](LabelerApi.md#list) | **GET** /api/v1/labelers | List labelers
[**set_model**](LabelerApi.md#set_model) | **PUT** /api/v1/labelers/{labelerId}/models | Set a labeler model
[**set_resource_set**](LabelerApi.md#set_resource_set) | **PUT** /api/v1/labelers/{labelerId}/resources | Set a labeler resource set
[**update**](LabelerApi.md#update) | **PUT** /api/v1/labelers/{labelerId} | Update a labeler


# **cancel_model_training**
> SimpleResponse cancel_model_training(labeler_id, model_id)

Cancel labeler model training task

Cancel labeler model training task

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
api_instance = ibmwex.LabelerApi()
labeler_id = 'labeler_id_example' # str | The ID of the labeler.
model_id = 'model_id_example' # str | The ID of the model.

try: 
    # Cancel labeler model training task
    api_response = api_instance.cancel_model_training(labeler_id, model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelerApi->cancel_model_training: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **labeler_id** | **str**| The ID of the labeler. | 
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
> Labeler create(body)

Create a labeler

Create a new labeler.

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
api_instance = ibmwex.LabelerApi()
body = ibmwex.InitLabeler() # InitLabeler | 

try: 
    # Create a labeler
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelerApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InitLabeler**](InitLabeler.md)|  | 

### Return type

[**Labeler**](Labeler.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_collection**
> Collection create_collection(labeler_id, body)

Create and set a collection

Create a collection to process the source dataset of the labeler

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
api_instance = ibmwex.LabelerApi()
labeler_id = 'labeler_id_example' # str | The ID of the labeler.
body = ibmwex.MLCollection() # MLCollection | 

try: 
    # Create and set a collection
    api_response = api_instance.create_collection(labeler_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelerApi->create_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **labeler_id** | **str**| The ID of the labeler. | 
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
> ClassifierModel create_model_from_source_dataset(labeler_id, body, resource_name=resource_name, model_name=model_name, feature_threshold=feature_threshold, label_threshold=label_threshold, learning_rate=learning_rate, prob_threshold=prob_threshold)

Create a labeler model

Create and train a labeler model by separating the given source training dataset into training, validation, and test sets. About \"(For experts)\" parameters, refer [this](https://www.tensorflow.org/tutorials/wide#adding_regularization_to_prevent_overfitting) documentation.  Parameters used in training process can be set by adding config parameter of body  *Example*  For controlling training process   name | description  ---- | -----------  flag.batch_size | Int value. Batch size of examples per step  flag.max_steps | Int value. Max number of step for training  flag.val_monitor_every_n_steps |Int value. Step interval between validation  flag.val_monitor_early_stopping_rounds | Int value. Number of retry until cancel training (early stopping)  flag.early_stopping_improvement_ratio | loat value. Threshold of early stopping. The larger, the earlier trianing may stop.  For detailed model information*   name | description  ---- | -----------  flag.confusion_matrix_visible | True or False. Labelwise confusion matrix will be included. Currently only for classifier  flag.predictions_visible | True or False. Prediction results of documents in test dataset will be included. Currently only for classfier  flag.weights_visible | True or False. Weights of trained model will be included. Currenlty only for classifier 

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
api_instance = ibmwex.LabelerApi()
labeler_id = 'labeler_id_example' # str | The ID of the labeler.
body = ibmwex.InitDatasetConfig() # InitDatasetConfig | Configuration to split the source training dataset
resource_name = 'resource_name_example' # str | Name of the resource set created by this method (optional)
model_name = 'model_name_example' # str | Name of the model created by this method (optional)
feature_threshold = 2 # float | Used during training a model. Threshold of the feature occurrences.  If this value is set at 2, metadata and words in text content fields occurred in only 1 document in the training set are not used as features. (optional) (default to 2)
label_threshold = 2 # float | Used during training a model. Threshold of the label occurrences.  If this value is set at 2, labels occurred in only 1 document in the training set are not used for the training and the prediction. (optional) (default to 2)
learning_rate = 0.1 # float | (For experts) Learning rate used in the training (optional) (default to 0.1)
prob_threshold = 0.5 # float | Used during using a deployed model. Threshold for the label prediction probabilities. If the predicted probability of a label is less than this value, the label is not included as the prediction result of this labeler in the runtime. A better value is calculcated and set while training. (optional) (default to 0.5)

try: 
    # Create a labeler model
    api_response = api_instance.create_model_from_source_dataset(labeler_id, body, resource_name=resource_name, model_name=model_name, feature_threshold=feature_threshold, label_threshold=label_threshold, learning_rate=learning_rate, prob_threshold=prob_threshold)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelerApi->create_model_from_source_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **labeler_id** | **str**| The ID of the labeler. | 
 **body** | [**InitDatasetConfig**](InitDatasetConfig.md)| Configuration to split the source training dataset | 
 **resource_name** | **str**| Name of the resource set created by this method | [optional] 
 **model_name** | **str**| Name of the model created by this method | [optional] 
 **feature_threshold** | **float**| Used during training a model. Threshold of the feature occurrences.  If this value is set at 2, metadata and words in text content fields occurred in only 1 document in the training set are not used as features. | [optional] [default to 2]
 **label_threshold** | **float**| Used during training a model. Threshold of the label occurrences.  If this value is set at 2, labels occurred in only 1 document in the training set are not used for the training and the prediction. | [optional] [default to 2]
 **learning_rate** | **float**| (For experts) Learning rate used in the training | [optional] [default to 0.1]
 **prob_threshold** | **float**| Used during using a deployed model. Threshold for the label prediction probabilities. If the predicted probability of a label is less than this value, the label is not included as the prediction result of this labeler in the runtime. A better value is calculcated and set while training. | [optional] [default to 0.5]

### Return type

[**ClassifierModel**](ClassifierModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> SimpleResponse delete(labeler_id)

Delete a labeler

Delete an existing labeler

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
api_instance = ibmwex.LabelerApi()
labeler_id = 'labeler_id_example' # str | The ID of the labeler.

try: 
    # Delete a labeler
    api_response = api_instance.delete(labeler_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelerApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **labeler_id** | **str**| The ID of the labeler. | 

### Return type

[**SimpleResponse**](SimpleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Labeler get(labeler_id)

Show labeler details

Show detailed information of an existing labeler

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
api_instance = ibmwex.LabelerApi()
labeler_id = 'labeler_id_example' # str | The ID of the labeler.

try: 
    # Show labeler details
    api_response = api_instance.get(labeler_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelerApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **labeler_id** | **str**| The ID of the labeler. | 

### Return type

[**Labeler**](Labeler.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enrichment**
> ListResponseString get_enrichment(labeler_id, model_id)

List enrichments where the labeler model deployed

Show IDs of enrichments where the specified labeler model deployed.

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
api_instance = ibmwex.LabelerApi()
labeler_id = 'labeler_id_example' # str | The ID of the labeler.
model_id = 'model_id_example' # str | The ID of the model.

try: 
    # List enrichments where the labeler model deployed
    api_response = api_instance.get_enrichment(labeler_id, model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelerApi->get_enrichment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **labeler_id** | **str**| The ID of the labeler. | 
 **model_id** | **str**| The ID of the model. | 

### Return type

[**ListResponseString**](ListResponseString.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enrichment_latest**
> ListResponseString get_enrichment_latest(labeler_id)

List enrichments where the latest labeler model deployed

Show IDs of enrichments where the latest labeler model deployed.

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
api_instance = ibmwex.LabelerApi()
labeler_id = 'labeler_id_example' # str | The ID of the labeler.

try: 
    # List enrichments where the latest labeler model deployed
    api_response = api_instance.get_enrichment_latest(labeler_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelerApi->get_enrichment_latest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **labeler_id** | **str**| The ID of the labeler. | 

### Return type

[**ListResponseString**](ListResponseString.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model**
> ClassifierModel get_model(labeler_id, model_id)

Show labeler model details

Show detailed information of an existing labeler model

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
api_instance = ibmwex.LabelerApi()
labeler_id = 'labeler_id_example' # str | The ID of the labeler.
model_id = 'model_id_example' # str | The ID of the model.

try: 
    # Show labeler model details
    api_response = api_instance.get_model(labeler_id, model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelerApi->get_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **labeler_id** | **str**| The ID of the labeler. | 
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
> ClassifierModel get_model_latest(labeler_id)

Show the latest labeler model details

Show detailed information of the latest model of the labeler

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
api_instance = ibmwex.LabelerApi()
labeler_id = 'labeler_id_example' # str | The ID of the labeler.

try: 
    # Show the latest labeler model details
    api_response = api_instance.get_model_latest(labeler_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelerApi->get_model_latest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **labeler_id** | **str**| The ID of the labeler. | 

### Return type

[**ClassifierModel**](ClassifierModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_status**
> ClassifierModelStatus get_model_status(labeler_id, model_id)

Show labeler model status

Show status of the specified labeler model

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
api_instance = ibmwex.LabelerApi()
labeler_id = 'labeler_id_example' # str | The ID of the labeler.
model_id = 'model_id_example' # str | The ID of the model.

try: 
    # Show labeler model status
    api_response = api_instance.get_model_status(labeler_id, model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelerApi->get_model_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **labeler_id** | **str**| The ID of the labeler. | 
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
> ResourceSet get_resource_set(labeler_id, resource_set_id)

Show labeler resource set details

Show detailed information of an existing labeler resource set

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
api_instance = ibmwex.LabelerApi()
labeler_id = 'labeler_id_example' # str | The ID of the labeler.
resource_set_id = 'resource_set_id_example' # str | The ID of the resource set.

try: 
    # Show labeler resource set details
    api_response = api_instance.get_resource_set(labeler_id, resource_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelerApi->get_resource_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **labeler_id** | **str**| The ID of the labeler. | 
 **resource_set_id** | **str**| The ID of the resource set. | 

### Return type

[**ResourceSet**](ResourceSet.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_eval**
> LabelerEvalResult get_test_eval(labeler_id, model_id)

Show test evaluation result of the model

Show test evaluation result of the specified labeler model.

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
api_instance = ibmwex.LabelerApi()
labeler_id = 'labeler_id_example' # str | The ID of the labeler.
model_id = 'model_id_example' # str | The ID of the model.

try: 
    # Show test evaluation result of the model
    api_response = api_instance.get_test_eval(labeler_id, model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelerApi->get_test_eval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **labeler_id** | **str**| The ID of the labeler. | 
 **model_id** | **str**| The ID of the model. | 

### Return type

[**LabelerEvalResult**](LabelerEvalResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_evals**
> ListResponseLabelerEvalResult get_test_evals(labeler_id)

List test evaluation results

List test evaluation results of all models of the specified labeler.

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
api_instance = ibmwex.LabelerApi()
labeler_id = 'labeler_id_example' # str | The ID of the labeler.

try: 
    # List test evaluation results
    api_response = api_instance.get_test_evals(labeler_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelerApi->get_test_evals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **labeler_id** | **str**| The ID of the labeler. | 

### Return type

[**ListResponseLabelerEvalResult**](ListResponseLabelerEvalResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_validation_eval**
> LabelerEvalResult get_validation_eval(labeler_id, model_id)

Show validation evaluation result of the model

Show validation evaluation result of the specified labeler model.

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
api_instance = ibmwex.LabelerApi()
labeler_id = 'labeler_id_example' # str | The ID of the labeler.
model_id = 'model_id_example' # str | The ID of the model.

try: 
    # Show validation evaluation result of the model
    api_response = api_instance.get_validation_eval(labeler_id, model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelerApi->get_validation_eval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **labeler_id** | **str**| The ID of the labeler. | 
 **model_id** | **str**| The ID of the model. | 

### Return type

[**LabelerEvalResult**](LabelerEvalResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ListResponseLabeler list()

List labelers

Display a list of existing labelers

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
api_instance = ibmwex.LabelerApi()

try: 
    # List labelers
    api_response = api_instance.list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelerApi->list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListResponseLabeler**](ListResponseLabeler.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_model**
> ClassifierModel set_model(labeler_id, body)

Set a labeler model

Set a labeler model to the labeler

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
api_instance = ibmwex.LabelerApi()
labeler_id = 'labeler_id_example' # str | The ID of the labeler.
body = ibmwex.ClassifierModel() # ClassifierModel | 

try: 
    # Set a labeler model
    api_response = api_instance.set_model(labeler_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelerApi->set_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **labeler_id** | **str**| The ID of the labeler. | 
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
> ResourceSet set_resource_set(labeler_id, body)

Set a labeler resource set

Set a labeler resource set

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
api_instance = ibmwex.LabelerApi()
labeler_id = 'labeler_id_example' # str | The ID of the labeler.
body = ibmwex.ResourceSet() # ResourceSet | 

try: 
    # Set a labeler resource set
    api_response = api_instance.set_resource_set(labeler_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelerApi->set_resource_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **labeler_id** | **str**| The ID of the labeler. | 
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
> Labeler update(labeler_id, body)

Update a labeler

Update an existing labeler

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
api_instance = ibmwex.LabelerApi()
labeler_id = 'labeler_id_example' # str | The ID of the labeler.
body = ibmwex.Labeler() # Labeler | 

try: 
    # Update a labeler
    api_response = api_instance.update(labeler_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelerApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **labeler_id** | **str**| The ID of the labeler. | 
 **body** | [**Labeler**](Labeler.md)|  | 

### Return type

[**Labeler**](Labeler.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

