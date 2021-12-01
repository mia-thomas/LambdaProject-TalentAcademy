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
    body = json.loads(s3_object['Body'].read())
    print(body)
    pet_name=event["PetName"]
    
    
    foods=body['pets']
    print(foods)
    
    # print("Meowsalot Fav Food is:")
    # for food in body:
    #     print(favFoods)
    
    
    
    # x = body['favFoods']
    # pet_name = event[PetName]
    # for food in pet_name
    
    

# }
# x = thisdict["model"]
# {
#   "S3Bucket": "mia-l-function-s3",
#   "S3Prefix": "sample_data.json",
#   "PetName": "Meowsalot"
# }