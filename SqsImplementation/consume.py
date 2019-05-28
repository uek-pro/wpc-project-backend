import boto3, json, time

sqs = boto3.client('sqs', region_name='eu-central-1')
QUEUE_URL = ''

def handle(order):
    print("i am processing {}", order['email'])
    for i in range(10):
        print(".")
        time.sleep(1)

while True:
    response = sqs.receive_message(
        QueueUrl=QUEUE_URL,
        WaitTimeSeconds=10
    )
    if not 'Messages' in response:
        continue

    for m in response['Messages']:
        print(m)
        data = json.loads(m['Body'])
        handle(data)
        sqs.delete_message(
            QueueUrl=QUEUE_URL,
            ReceiptHandle=m['ReceiptHandle']
        )