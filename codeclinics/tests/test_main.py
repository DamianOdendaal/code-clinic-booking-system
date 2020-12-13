import os
import sys
import unittest
from login import user_auth
from datetime import datetime, timedelta
##### Calendar setup imports
import googleapiclient.discovery
from calendar_setup import calendar_service, setup 
# import datetime
import pytz
##### Bookings imports


class LoginTestCase(unittest.TestCase):
    """
    This class contains all the tests for the user_auth module in the login package
    """

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

        output = user_auth.get_user_details()
        self.assertEqual(dict, type(output))
        self.assertEqual(len(output), 4)


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
        output = os.path.exists(f"{sys.path[0]}/.config.json")
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
        
    

    def test_user_logout(self):
        """
        This tests the user_logout() function.
        """
        output = None
        if os.path.exists(f"{sys.path[0]}/creds/token.pickle"):
            output = user_auth.user_logout("test")
            self.assertTrue(output)
        else:
            output = user_auth.user_logout("test")
            self.assertFalse(output)

        
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


    def test_show_config(self):
        """
        This tests the show_config() function.
        """
        pass

        
    def test_get_user_email(self):
        """
        This tests the get_user_email() function.
        """

        output = user_auth.get_user_email()
        self.assertEqual(type(output), str)
        # self.assertNotEqual(output, '')

    
    def test_auto_logout(self):
        """
        This tests the test_auto_logout() function.
        """
        
        # output = user_auth.auto_logout()

        #must use datetime stuff
        pass


class CalendarSetupTestCase(unittest.TestCase):
    """
    This class contains all the tests for the modules in the calendar_setup 
    package
    """

    """
    Test cases for the "calendar_service" module
    """
    def test_get_service(self):
        """
        This tests the get_service() function
        """
        output = calendar_service.get_service()
        self.assertEqual(type(output), googleapiclient.discovery.Resource)


    def test_get_events_results(self):
        """
        This tests the get_events_results() function
        """

        output = calendar_service.get_events_results()
        self.assertEqual(type(output), dict)
        self.assertTrue(len(output) > 0)


    def test_get_time_constraints(self):
        """
        This tests the get_time_constraints() function
        """
        now = datetime.now(pytz.timezone("Africa/Cairo"))
        end = now + timedelta(days=7)
        start = now.strftime("%Y-%m-%dT%H:%M:%S") + "Z"
        end = end.strftime("%Y-%m-%dT%H:%M:%S") + "Z"

        output = calendar_service.get_time_constraints()
        self.assertEqual(output, (start, end))


    """
    Test cases for the "setup" module
    """
    def test_install_packages(self):
        """
        This tests the install_packages() function
        """

        pass


class BookingsTestCase(unittest.TestCase):
    """
    This class contains all the tests for the modules in the bookings
    package
    """

    """
    Test cases for the "list_calendars" module
    """


    """
    Test cases for the "patient" module
    """


    """
    Test cases for the "processing_data" module
    """


    """
    Test cases for the "volunteer" module
    """


if __name__ == "__main__":
    unittest.main()
