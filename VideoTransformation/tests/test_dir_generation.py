import unittest
from dir_management import generate_dirname

class TestDirGeneration(unittest.TestCase):
    
    def test_generate_dir_name(self):
        
        # Arrange / Given
        name = "katalog daniela b"
        
        # Act / When
        result_name = generate_dirname(name)
        
        # Assert / Then / Expect
        assert result_name == "katalog-daniela-b"
        
    def test_addition(self):
        assert 2 + 2 == 4