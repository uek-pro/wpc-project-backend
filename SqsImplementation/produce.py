import boto3, json

sqs = boto3.client('sqs', region_name='eu-central-1')
QUEUE_URL = ''

createVideoRequest = {
    "email": '',
    "photos": [
        "uek/user-1/1.jpg", 
        "uek/user-1/2.jpg",
        "uek/user-1/3.jpg" 
    ]
}

sqs.send_message(
    QueueUrl = QUEUE_URL,
    MessageBody = json.dumps(createVideoRequest)
)