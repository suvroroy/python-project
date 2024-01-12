import boto3
import json

client = boto3.client('inspector2')

# get config

# response = client.get_configuration()
response = client.list_findings(
    filterCriteria={'findingArn':[{'comparison': 'EQUALS', 'value': 'arn:aws:inspector2:us-east-1:590910745065:finding/25858500b959503efae4f6bbee1ea9c7'}]})
print (response)