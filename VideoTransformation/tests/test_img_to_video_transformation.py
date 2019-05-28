import unittest
import os
import uuid
from image_manipulation import transform_img_to_mov

class TestImgToVideoTransformation(unittest.TestCase):
    
    def test_create_video_based_on_img(self):
        #Arrange
        source_file = self.there_is_image_src_file()
        video_dest_path = self.i_expect_video_to_be_created_within_path()
        
        #Act
        transform_img_to_mov(source_file, video_dest_path)
        
        #Assert
        self.there_is_video_file_in_path(video_dest_path)
        
    def there_is_image_src_file(self):
        return os.path.join(
            os.path.dirname(__file__),
            "var/1.jpg"
        )
        
    def i_expect_video_to_be_created_within_path(self):
        return "/tmp/{}/video.mp4".format(uuid.uuid4())
        
    def there_is_video_file_in_path(self, path):
        assert os.path.isfile(path)