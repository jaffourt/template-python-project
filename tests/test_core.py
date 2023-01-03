import unittest

from my_package.core import make_request


class TestMakeRequest(unittest.TestCase):

    def test_make_request(self):
        # Test default behavior
        default = make_request()
        self.assertEqual(default.status_code, 200)

        # Test with custom webpage
        custom = make_request("https://www.google.com")
        self.assertEqual(custom.status_code, 200)


if __name__ == '__main__':
    unittest.main()
