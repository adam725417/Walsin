# ClassifierModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkpoint_file_resource_id** | **str** | (Used by system) | [optional] 
**creation_end_time** | **int** | Timestamp when the model creation ends | [optional] 
**creation_start_time** | **int** | Timestamp when the model creation starts | [optional] 
**config** | **dict(str, str)** | Map of properties that can be passed to training process as arguments | [optional] 
**description** | **str** | User-provided description | [optional] 
**id** | **str** | ID | [optional] 
**initialized_time** | **int** | Timestamp when the model is initialized | [optional] 
**l1_regularization_strength** | **float** | L1 regularization strength | [optional] 
**l2_regularization_strength** | **float** | L2 regularization strength | [optional] 
**learning_rate** | **float** | Learning rate | [optional] 
**metadata** | **object** | (Used by system) | [optional] 
**model_file_resource_id** | **str** | (Used by system) | [optional] 
**name** | **str** | Name | [optional] 
**prob_threshold** | **float** | Threshold of probabilities to output predicted labels | [optional] 
**resource_set_id** | **str** | ID of the resource set used to train this model | [optional] 
**state** | **str** | Current state of this model | [optional] 
**tags** | **dict(str, object)** | (Used by system) | [optional] 
**test_eval_result_file_resource_id** | **str** | (Used by system) | [optional] 
**training_history** | [**list[ValidationMetrics]**](ValidationMetrics.md) | History of loss values during the training | [optional] 
**validation_eval_result_file_resource_id** | **str** | (Used by system) | [optional] 
**deployable_file_resources** | **list[str]** | (Used by system) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


