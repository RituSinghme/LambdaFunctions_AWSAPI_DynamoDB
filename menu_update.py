from __future__ import print_function
import boto3

def lambda_handler(event, context):
    table = boto3.resource('dynamodb').Table('menu')
    data = event['body-json']

    result = table.update_item(
    Key={
        'menu_id': event['params']['path']['menu-id']
        },
    UpdateExpression="set selection= :r",
    ExpressionAttributeValues={
        ':r': data['selection']
    },
    ReturnValues="ALL_NEW"
    )

    # create a response
    response = {
        "statusCode": "200 OK",
        #"body": result['Attributes']
    }
    return response
