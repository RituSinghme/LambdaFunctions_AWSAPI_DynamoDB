from __future__ import print_function
import json
import boto3

def lambda_handler(event, context):
    order_table = boto3.resource('dynamodb').Table('order')
    menu_table = boto3.resource('dynamodb').Table('menu')
    payload = event['body-json']

    request_menu_id = payload['menu_id']
    request_order_id = payload['order_id']
    customer_name = payload['customer_name']
    customer_email_id = payload['customer_email']

    result = order_table.put_item(
    Item = {
        'order_id' : request_order_id,
        'menu_id' : request_menu_id,
        'customer_name' : customer_name,
        'customer_email_id' : customer_email_id,
        'order_status' : 'NewOrder',
        'order_details' : {
                'selection' : 'null',
                'size' : 'null',
                'cost' : 'null',
                'order_time' : 'null'
         }
      }
    )
    menu_options  = menu_table.get_item(
    Key = {
    'menu_id' : request_menu_id
    }
    )

    menu_data = menu_options['Item']
    db_data ={}
    message  = "Hi " + customer_name + " , please choose one of the selections :"

    d = 1
    for item in menu_data['selection']:
        message = message + str(d)
        message = message + ". "+ item +", "
        d  = d + 1
    message = message[:-2]
    db_data['Message'] = message

        # create a response
    response = {
        "statusCode": "200 OK",
        "body": db_data
    }
    return response
