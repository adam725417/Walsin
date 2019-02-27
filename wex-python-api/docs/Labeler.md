# Labeler

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Required property to deserialize the JSON string correctly | [default to 'Labeler']
**configs** | [**list[DatasetConfig]**](DatasetConfig.md) | Settings to split the source dataset into training, validation, and test sets | [optional] 
**description** | **str** | Description of the labeler | [optional] 
**ground_truth_label_facet** | **str** | Name of the answer field that contains correct labels of a document | 
**id** | **str** | ID | [optional] 
**metadata** | **object** | (Used by system) | [optional] 
**ml_collection_id** | **str** | ID of the collection created by POST /api/v1/labelers/{labelerId}/collection | [optional] 
**models** | [**list[ClassifierModel]**](ClassifierModel.md) | Labeler models | [optional] 
**name** | **str** | Name | [optional] 
**predicted_label_facet** | **str** | Name of the field that contains predicted labels given by this labeler | 
**resources** | [**list[ResourceSet]**](ResourceSet.md) | Resource sets | [optional] 
**source_dataset_id** | **str** | ID of the source dataset provided when creating this labeler | [optional] 
**tags** | **dict(str, object)** | (Used by system) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


