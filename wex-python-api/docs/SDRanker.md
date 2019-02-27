# SDRanker

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Required property to deserialize the JSON string correctly | [default to 'SimilarDocumentRanker']
**configs** | [**list[DatasetConfig]**](DatasetConfig.md) | Settings to split the source dataset into training, validation, and test sets | [optional] 
**description** | **str** | Description of the ranker | [optional] 
**correct_answer_field** | **str** | Name of the field that contains information to detect truly similar documents | 
**correct_answer_field_type** | **str** | Type of the correct answer field | 
**doc_id_field** | **str** | User defined document ID field that is used when the value of correctAnswerFieldType is ID | [optional] 
**id** | **str** | ID | [optional] 
**metadata** | **object** | (Used by system) | [optional] 
**ml_collection_id** | **str** | ID of the collection storing the source dataset | [optional] 
**models** | [**list[ClassifierModel]**](ClassifierModel.md) | Ranker models | [optional] 
**name** | **str** | Name | [optional] 
**resources** | [**list[ResourceSet]**](ResourceSet.md) | Resource sets | [optional] 
**source_dataset_id** | **str** | ID of the source dataset | [optional] 
**tags** | **dict(str, object)** | (Used by system) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


