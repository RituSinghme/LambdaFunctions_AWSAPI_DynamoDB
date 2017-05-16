from __future__ import print_function
import boto3
import json

def lambda_handler(event, context):
    # TODO implement
    dynamodbTable = boto3.resource('dynamodb').Table('menu')
    api_menu = event['params']['path']['menu-id']

    result = dynamodbTable.get_item(
        Key={
            'menu_id': api_menu
        }
        )

    # create a response
    response = {
        "body": result['Item']
    }

    return response
