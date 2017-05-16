from __future__ import print_function
import boto3
import time

def lambda_handler(event, context):
    order_table = boto3.resource('dynamodb').Table('order')
    size_serial_no = event['body-json']
    order_id = event['params']['path']['order_id']

    result = order_table.get_item(
        Key={
            'order_id': order_id
        }
        )

    # create a response
    response = {
        "body": result['Item']
    }

    return response
