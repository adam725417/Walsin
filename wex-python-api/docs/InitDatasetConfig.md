# InitDatasetConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **dict(str, str)** | Map of properties that can be passed to training process as arguments. Should start with *flag.* This will be passed to model&#39;s config when model creation started by &#x60;POST /api/v1/labelers/{labelerId}/models/all&#x60;  | [optional] 
**description** | **str** | Description | [optional] 
**kept_ml_datasets** | **list[str]** | Type of datasets specified to be kept by users | [optional] 
**name** | **str** | Name | [optional] 
**test_ratio** | **int** | Ratio of test set to divide the source dataset | [optional] 
**training_ratio** | **int** | Ratio of training set to divide the source dataset | [optional] 
**validation_ratio** | **int** | Ratio of validation set to divide the source dataset | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


