import unittest
import os
import uuid
from image_manipulation import transform_img_to_img
# source .venv/bin/activate
class TestImgToImgTransformation(unittest.TestCase):
    
    def test_create_video_based_on_img(self):
        #Arrange
        source_file1 = self.there_is_image_src_file("var/1.jpg")
        source_file2 = self.there_is_image_src_file("var/2.jpg")
        video_dest_path = self.i_expect_video_to_be_created_within_path()
        
        #Act
        transform_img_to_img(source_file1, source_file2, video_dest_path)
        
        #Assert
        self.there_is_video_file_in_path(video_dest_path)
        
    def there_is_image_src_file(self, src):
        return os.path.join(
            os.path.dirname(__file__),
            src
        )
        
    def i_expect_video_to_be_created_within_path(self):
        return "/tmp/{}/video2.mp4".format(uuid.uuid4())
        
    def there_is_video_file_in_path(self, path):
        assert os.path.isfile(path)