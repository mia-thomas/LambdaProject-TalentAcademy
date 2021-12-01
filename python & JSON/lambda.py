import logging
import boto3
import json
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # Retrieve the list of existing buckets
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    print(response)
    
    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')
    
        
    bucket_name = event["S3Bucket"]
    key = event["S3Prefix"]
    s3_object = s3.get_object(Bucket=bucket_name, Key=key)
    print("This is the whole content of JSON File: ")
    body = json.loads(s3_object['Body'].read())
    print(body)
    
    for name in body['pets']:
        if name == event['Meowsalot']:
            return {
                'statusCode' : 200,
                'body' : json.dumps(body['favFoods'])
            }
