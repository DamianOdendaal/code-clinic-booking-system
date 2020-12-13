import unittest
from python_api_mock.users import get_users

class BasicTest(unittest.TestCase):
    def test_request_response(self):
        response = get_users()
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()    
