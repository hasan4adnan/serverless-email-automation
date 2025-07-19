import json
import boto3
import os

ses_client = boto3.client('ses', region_name='us-east-1')

TO_ADDRESS = "seninkimailin@gmail.com"  # Burayı kendi verified mail adresinle değiştir

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        subject = "New file uploaded to S3"
        body = f"File '{key}' was uploaded to bucket '{bucket}'."

        ses_client.send_email(
            Source=TO_ADDRESS,
            Destination={'ToAddresses': [TO_ADDRESS]},
            Message={
                'Subject': {'Data': subject},
                'Body': {
                    'Text': {'Data': body}
                }
            }   
        )


    return {
        'statusCode': 200,
        'body': json.dumps('Email sent successfully!')
    }
