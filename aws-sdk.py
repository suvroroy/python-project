import boto3
import json

# s3 = boto3.resource('s3')
#
# for bucket in s3.buckets.all():
#     print(bucket.name)

client = boto3.client('inspector2')

# response = client.batch_get_account_status( # batch get account status
#     accountIds=[
#         '684578858341',
#     ]
# )

response = client.list_findings(
    filterCriteria={'findingArn':[{'comparison': 'EQUALS', 'value': 'arn:aws:inspector2:us-east-1:109655449219:finding/0d76203ab689cc017401e8c29f75903c'},]})

# pretty_format = json.dumps(response)

print(response)