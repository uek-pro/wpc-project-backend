import json, boto3, os
from media_manipulation import create_slide_show
from order_sending import send_order_result

BUCKET_NAME = os.getenv('BUCKET_NAME')
HOST_URL = os.getenv('HOST_URL')

s3 = boto3.client('s3', region_name = 'eu-central-1')



def ensure_request_dir(order_id):
    os.system("mkdir -p /tmp/{}/source".format(order_id))
    os.system("mkdir -p /tmp/{}/video".format(order_id))
    
def copy_object_to_dir(s3_input_key, order_id, destination):
    print("try to download {}".format(s3_input_key))
    os.system("mkdir -p /tmp/{}/source".format(order_id))
    with open(destination, 'wb+') as data:
        s3.download_fileobj(BUCKET_NAME, s3_input_key, data)

def upload_object(source, key):
    with open(source, 'rb') as f:
        s3.put_object(
            Key=key,
            Body=f,
            Bucket=BUCKET_NAME,
            ACL='public-read'
        )

def clear_workspace(order_id):
    os.system("rm -rf /tmp/{}".format(order_id))


def lambda_handler(event, context):  
    for record in event['Records']:
        
        ordr = json.loads(record['body'])
        order_id = ordr['order_id']
        email = ordr['email']
        photos = ordr['photos']
        print(photos)
        
        ensure_request_dir(order_id)
        for i, photo_key in zip(range(0, len(photos)), photos):
            source_filename = "/tmp/{}/source/photo_{}".format(order_id, i)
            copy_object_to_dir(photo_key, order_id, source_filename)
        
        create_slide_show(
            ["/tmp/{}/source/photo_{}".format(order_id, i) for i in range(0, len(photos))],
            "/tmp/{}/output.mp4".format(order_id)
        )

        output_relative_path = "uek-krakow/order/{}/video.mp4".format(order_id)
        upload_object(
            "/tmp/{}/output.mp4".format(order_id),
            output_relative_path
        )

        animation_url = "{}/{}".format(HOST_URL, output_relative_path)

        send_order_result(email, animation_url)
        print('Wykonało się chyba')

        clear_workspace(order_id)