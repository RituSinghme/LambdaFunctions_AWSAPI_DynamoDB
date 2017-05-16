from __future__ import print_function
import boto3

def lambda_handler(event, context):
    dynamodbTable = boto3.resource('dynamodb').Table('menu')
    request_body = event['body-json']
    dynamodbTable.put_item(Item=request_body)
    return "200 OK"
    
