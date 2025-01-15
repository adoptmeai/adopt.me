import unittest
from bot import generate_dog_image

class TestBot(unittest.TestCase):
    def test_generate_dog_image(self):
        image_url = generate_dog_image()
        self.assertTrue(image_url.startswith("http"))

if __name__ == "__main__":
    unittest.main()
