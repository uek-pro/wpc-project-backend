import json, boto3, os

def lambda_handler(order_animation_request, context):
    
    sqs = boto3.client('sqs', region_name='eu-central-1') # NOTE:
    
    if not 'order_id' in order_animation_request:
        raise ValueError('order_id is required')

    if not 'email' in order_animation_request:
        raise ValueError('email is required')
        
    if not 'photos' in order_animation_request:
        raise ValueError('photos are required')
    
    sqs.send_message(
        QueueUrl=os.getenv('QUEUE_URL'),
        MessageBody=json.dumps(order_animation_request)
    )
    
    return {
        'statusCode': 200,
        'body': {
            'message': 'Wysłano pomyślnie do kolejki'
        }
    }