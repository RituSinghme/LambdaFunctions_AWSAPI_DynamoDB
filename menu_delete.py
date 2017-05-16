from __future__ import print_function
import boto3

def lambda_handler(event, context):
    Table = boto3.resource('dynamodb').Table('menu')
    api_menu = event['params']['path']['menu-id']


    Table.delete_item(
        Key={
            'menu_id': api_menu
        }
        )

    # create a response
    response = {
        "statusCode": "200 OK"
    }

    return response
