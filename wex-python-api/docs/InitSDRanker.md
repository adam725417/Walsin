# InitSDRanker

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Required property to deserialize the JSON string correctly | [default to 'SimilarDocumentRanker']
**description** | **str** | Description of the ranker | [optional] 
**correct_answer_field** | **str** | Name of the field that contains information to detect truly similar documents | 
**correct_answer_field_type** | **str** | Type of the answer field | 
**doc_id_field** | **str** | User defined document ID field that is used when the value of correctAnswerFieldType is ID | [optional] 
**name** | **str** | Name | [optional] 
**source_dataset_id** | **str** | ID of the training dataset | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


