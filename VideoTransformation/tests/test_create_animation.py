import unittest
import os
import boto3

class TestCreateAnimation(unittest.TestCase):
    def test_create_based_on_request(self):
        
        # Arrange
        img_src = self.there_is_file_uploaded_to_s3(
            'tests/photostore/user1/test_image.jpg'    
        )
        video_dest = self.i_expect_animation_to_here()
        
        # Act
        api = VideoCreationHandler()
        createAnimationRequest = {
            'src': img_src,
            'dest': video_dest
        }
        api.handle(createAnimationRequest)
        
        # Assert
        self.there_is_video_file_in_s3(video_path)
        
    def there_is_file_uploaded_to_s3(self, dest):
        test_img_src = os.path.join(
            os.path.dirname(__file__),
            'var/1.jpg'
        )
        
        s3 = boto3.client('s3', region_name = 'eu-central-1')
        
        with open(test_img_src, 'rb') as f:
            s3.put_object(
                Key=dest,
                Body=f,
                Bucket=os.getenv('TEST_BUCKET_NAME')
            )
            
            
# TEST_BUCKET_NAME=185777 pytest test_create_animation.py
# PYTHONPATH=./ TEST_BUCKET_NAME=185777 pytest tests/test_create_animation.py 