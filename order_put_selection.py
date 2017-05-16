from __future__ import print_function
import boto3
from datetime import datetime

def lambda_handler(event, context):
    order_table = boto3.resource('dynamodb').Table('order')
    menu_table = boto3.resource('dynamodb').Table('menu')
    selection_no = event['body-json']['input']
    order_id = event['params']['path']['order_id']


    order_record  = order_table.get_item(
    Key = {
    'order_id' : order_id
    }
    )

    menu_id1 = order_record['Item']['menu_id']

    menu_choices  = menu_table.get_item(
    Key = {
    'menu_id' : menu_id1
    }
    )

    order_selection_done = order_record['Item']['order_details']['selection']

    if order_selection_done == "null":

        selection_made = menu_choices['Item']['selection'][int(selection_no)-1]

        result = order_table.update_item(
        Key={
            'order_id': order_id
            },
        UpdateExpression="set order_details.selection= :r",
        ExpressionAttributeValues={
            ':r': selection_made
        },
        ReturnValues="UPDATED_NEW"
        )

        size_options = menu_choices['Item']['size']

        ask_size ={}

        message  = "Which size do you want:"
        s = 1
        for item in size_options:
            message = message + str(s)
            message = message + ". "+ item +", "
            s  = s + 1
        message = message[:-2]

        ask_size['Message'] = message

        return ask_size

    else:
        time=datetime.now().strftime("%m-%d-%y %H:%M")

        result = order_table.update_item(
        Key={
            'order_id': order_id
            },
        UpdateExpression="set order_details.size= :s , order_details.cost= :p, order_details.order_time = :t, order_status = :o",
        ExpressionAttributeValues={
            ':s':menu_choices['Item']['size'][int(selection_no)-1],
            ':p': menu_choices['Item']['price'][int(selection_no)-1],
            ':t': time,
            ':o': "Processing",

        },
        ReturnValues="UPDATED_NEW"
        )

        # create a response
        response = {
            "statusCode": "200 OK",
            "body": "Your order costs $"+ str(menu_choices['Item']['price'][int(selection_no)-1]) +"We will email you when the order is ready. Thank you!"
        }
        return response
