import os
import sys
import unittest
import datetime
from login import user_auth
from datetime import datetime


class OurTestCase(unittest.TestCase):
    def test_get_time_date(self):
        """
        This tests the get_time_date() function's 
        return value from login.user_auth.py.
        """
        now = datetime.now()
        date = now.strftime("%D")
        time = now.strftime("%H:%M")
        output = user_auth.get_time_date()
        dateAndTime = {
            "date": date,
            "time": time
        }
        self.assertEqual(dateAndTime, output)


    def test_get_user_details(self):
        """
        This tests the get_user_details() function's
        return type from login.user_auth.py.
        """
        getUserDetails = dict
        output = user_auth.get_user_details()
        self.assertEqual(getUserDetails, type(output))


    def test_remove_token(self):
        """
        This tests the remove_token() function's
        return value from login.user_auth.py.
        """
        output = user_auth.remove_token("test")
        self.assertTrue(output)


    def test_validate_email(self):
        """
        This tests the validate_email() function's
        output from login.user_auth.py.
        """
        pass


    def test_writing_to_json_file(self):
        """
        This tests the writing_to_json_file() function.
        """
        user_auth.writing_to_json_file()
        output = os.path.exists(f"{sys.path[0]}/files/json/.config.json")
        self.assertTrue(output)


    def test_get_user_status(self):
        """
        This tests the get_user_status() function.
        """
        pass


    def test_user_login(self):
        """
        This tests the user_login() function.
        """
        pass
    

    # def test_user_logout(self):
    #     """
    #     This tests the user_logout() function.
    #     """
    #     output = user_auth.user_logout()
    #     temp = output
    #     if os.path.exists(f"{sys.path[0]}/creds/token.pickle"):
    #         print('worked')
    #         self.assertTrue(temp)
    #     else:
    #         print('Hola')
    #         self.assertFalse(temp)

        
    def test_get_login_state(self):
        """
        This tests the get_login_state()function's
        return value from login.user_auth.py.
        """
        output = user_auth.get_login_state()
        if os.path.exists(f"{sys.path[0]}/creds/token.pickle"):
            self.assertTrue(output)
        else:
            self.assertFalse(output)


    # def test_show_config(self):
        # """
        # This tests the show_config() function.
        # """

        
    # def test_get_user_email():
        # """
        # This tests the get_user_email() function.
        # """
    
    
    # def test_auto_logout():
        # """
        # This tests the test_auto_logout() function.
        # """


if __name__ == "__main__":
    unittest.main()