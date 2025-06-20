import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')
table = dynamodb.Table('FeedbackTable')
SNS_TOPIC_ARN = 'arn:aws:sns:ap-south-1:802936990671:feedback-topic'

def lambda_handler(event, context):
    try:
        # ✅ Print the received event
        print(f"[INFO] Event received: {event}")

        # Parse the body
        data = json.loads(event['body'])
        print(f"[INFO] Parsed data: {data}")

        # Prepare item
        feedback_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat()
        item = {
            'feedbackId': feedback_id,
            'name': data['name'],
            'email': data['email'],
            'message': data['message'],
            'timestamp': timestamp
        }
        print(f"[INFO] Prepared item for DynamoDB: {item}")

        # Save to DynamoDB
        table.put_item(Item=item)
        print(f"[INFO] Item saved successfully to DynamoDB.")

        # Publish to SNS
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=f"New Feedback Received from {data['name']}.\nMessage: {data['message']}",
            Subject='New Feedback Notification'
        )
        print(f"[INFO] Notification sent via SNS for feedbackId: {feedback_id}")

        # Final Response
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Feedback received successfully!', 'feedbackId': feedback_id})
        }

    except Exception as e:
        # ✅ Print error traceback
        print(f"[ERROR] An error occurred: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
