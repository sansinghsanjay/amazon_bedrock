# packages
import boto3
import json

# make API call
bedrock = boto3.client(
	service_name='bedrock'
)

# get list of models
models = bedrock.list_foundation_models().get('modelSummaries')

# print details of all models
for model in models:
	print(model)
