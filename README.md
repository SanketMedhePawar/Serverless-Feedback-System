📝 Project Overview
This project demonstrates a serverless feedback system using AWS services.
It allows users to send feedback via an API Gateway, which triggers an AWS Lambda function that:

Validates and saves the data to DynamoDB,

Publishes a notification to SNS, which sends an email alert.


☁️ AWS Services Used
AWS Lambda — Processes the request.

Amazon API Gateway — Enables POST requests.

DynamoDB — Persists the feedback.

Amazon SNS — Notifies via email.

CloudWatch Logs — Logs requests and errors.

⚡️ Setup Instructions
Create a DynamoDB Table named FeedbackTable:

Primary Key: feedbackId (String)

Create an SNS Topic:

Name: feedback-topic

Subscribe your email.

Create a Lambda Function:

Name: FeedbackCollectorFunction

Upload the code (lambda_function.py).

Set environment and attach required IAM policies.

Set Up an API Gateway Route:

Route: POST /

Integrate it with the Lambda.

📋 Testing the Endpoint
Send a POST request to the API:

Request
http
Copy
Edit
POST https://<your-api-id>.execute-api.<region>.amazonaws.com/

Content-Type: application/json

{
  "name": "Sanket",
  "email": "sanketmedhe311@gmail.com",
  "message": "This feedback system is awesome!"
}

Response
json
Copy
Edit
{
  "message": "Feedback received successfully!",
  "feedbackId": "<your-feedback-id>"
}
