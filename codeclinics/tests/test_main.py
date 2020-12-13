import os
import sys
import unittest
from unittest.mock import patch
from login import user_auth
from datetime import datetime, timedelta
"""Calendar setup imports"""
import googleapiclient.discovery
from calendar_setup import calendar_service
import pytz
"""Bookings imports"""
import io
from io import StringIO
from unittest.mock import patch
from bookings import list_calendars
from bookings import patient
from bookings import processing_data
from bookings import volunteer


class LoginTestCase(unittest.TestCase):
    """
    This class contains all the tests for the user_auth module in the login package
    """

    def test_get_time_date(self):
<<<<<<< HEAD
        """
        This tests the get_time_date() function's 
        return value from login.user_auth.py.
        """
        now = datetime.now()
        date = now.strftime("%D")
        time = now.strftime("%H:%M")
        output = user_auth.get_time_date()
=======
        """This tests the get_time_date() function's return value from 
        login.user_auth.py."""

        now = datetime.now()
        date = now.strftime("%D")
        time = now.strftime("%H:%M")

        output = user_auth.get_time_date()

>>>>>>> b10a7418481b6d76f486bc6e6ffdc1e8fa54226e
        dateAndTime = {
            "date": date,
            "time": time
        }
<<<<<<< HEAD
=======

>>>>>>> b10a7418481b6d76f486bc6e6ffdc1e8fa54226e
        self.assertEqual(dateAndTime, output)


    def test_get_user_details(self):
<<<<<<< HEAD
        """
        This tests the get_user_details() function's
        return type from login.user_auth.py.
        """

        output = user_auth.get_user_details()
=======
        """This tests the get_user_details() function's return type from 
        login.user_auth.py."""

        output = user_auth.get_user_details()

>>>>>>> b10a7418481b6d76f486bc6e6ffdc1e8fa54226e
        self.assertEqual(dict, type(output))
        self.assertEqual(len(output), 4)


    def test_remove_token(self):
<<<<<<< HEAD
        """
        This tests the remove_token() function's
        return value from login.user_auth.py.
        """
=======
        """This tests the remove_token() function's return value from 
        login.user_auth.py."""

>>>>>>> b10a7418481b6d76f486bc6e6ffdc1e8fa54226e
        output = os.path.exists(f"{sys.path[0]}/creds/token.pickle")
        
        if output:
            self.assertTrue(output)
        else:
            self.assertFalse(output)


    @patch('login.user_auth.validate_email',return_value='jdoe@wethinkcode.co.za')
    def test_validate_email(self, input):
<<<<<<< HEAD
        """
        This tests the validate_email() function's
        output from login.user_auth.py.
        """
        output = user_auth.validate_email(user_email=str)
=======
        """This tests the validate_email() function's output from 
        login.user_auth.py."""

        output = user_auth.validate_email(user_email=str)

>>>>>>> b10a7418481b6d76f486bc6e6ffdc1e8fa54226e
        self.assertEqual(output, 'jdoe@wethinkcode.co.za')


    def test_writing_to_json_file(self):
<<<<<<< HEAD
        """
        This tests the writing_to_json_file() function.
        """
=======
        """This tests the writing_to_json_file() function."""
        
>>>>>>> b10a7418481b6d76f486bc6e6ffdc1e8fa54226e
        user_auth.writing_to_json_file()
        output = os.path.exists(f"{sys.path[0]}/.config.json")
        if output:
            self.assertTrue(output)
        else:
            self.assertFalse(output)


    # def test_get_user_status(self):
    #     """
    #     This tests the get_user_status() function.
    #     """
    #     pass


    # def test_user_login(self):
    #     """
    #     This tests the user_login() function.
    #     """
    #     pass


    # @patch('sys.stdout', new_callable=io.StringIO)
    # def test_user_logout(self, mock_stdout):
    #     """
    #     This tests the user_logout() function.
    #     """
    #     user_auth.user_logout()
    #     self.assertEqual("\x1b[33mYou have successfully logged out!\x1b[0m\n", mock_stdout.getvalue())

    #     # output = os.path.exists(f"{sys.path[0]}/creds/token.pickle")
    #     # self.assertTrue(user_auth.user_logout())        


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
    #     """
    #     This tests the show_config() function.
    #     """
    #     pass

        
    def test_get_user_email(self):
        """
        This tests the get_user_email() function.
        """

        output = user_auth.get_user_email()
        self.assertEqual(type(output), str)
        self.assertNotEqual(output, '')

    
    # def test_auto_logout(self):
    #     """
    #     This tests the test_auto_logout() function.
    #     """
        
    #     # output = user_auth.auto_logout()

    #     #must use datetime stuff
    #     pass


class CalendarSetupTestCase(unittest.TestCase):
    """
    This class contains all the tests for the modules in the calendar_setup 
    package
    """

<<<<<<< HEAD
    """
    Test cases for the "calendar_service" module
    """
=======
>>>>>>> b10a7418481b6d76f486bc6e6ffdc1e8fa54226e
    def test_get_service(self):
        """
        This tests the get_service() function
        """
<<<<<<< HEAD
        output = calendar_service.get_service()
=======
        
        output = calendar_service.get_service()

>>>>>>> b10a7418481b6d76f486bc6e6ffdc1e8fa54226e
        self.assertEqual(type(output), googleapiclient.discovery.Resource)


    def test_get_events_results(self):
<<<<<<< HEAD
        """
        This tests the get_events_results() function
        """

        output = calendar_service.get_events_results()
=======
        """This tests the get_events_results() function."""

        output = calendar_service.get_events_results()

>>>>>>> b10a7418481b6d76f486bc6e6ffdc1e8fa54226e
        self.assertEqual(type(output), dict)
        self.assertTrue(len(output) > 0)


    def test_get_time_constraints(self):
<<<<<<< HEAD
        """
        This tests the get_time_constraints() function
        """
        now = datetime.now(pytz.timezone("Africa/Cairo"))
=======
        """This tests the get_time_constraints() function."""

        now = datetime.now(pytz.timezone("Africa/Johannesburg"))
>>>>>>> b10a7418481b6d76f486bc6e6ffdc1e8fa54226e
        end = now + timedelta(days=7)
        start = now.strftime("%Y-%m-%dT%H:%M:%S") + "Z"
        end = end.strftime("%Y-%m-%dT%H:%M:%S") + "Z"

        output = calendar_service.get_time_constraints()
<<<<<<< HEAD
        self.assertEqual(output, (start, end))


    """
    Test cases for the "setup" module
    """
=======

        self.assertEqual(output, (start, end))
    
>>>>>>> b10a7418481b6d76f486bc6e6ffdc1e8fa54226e

class BookingsTestCase(unittest.TestCase):
    """
    This class contains all the tests for the modules in the bookings
    package
    """

    """
    Test cases for the "list_calendars" module
    """

    # def test_formatted_data_output(self):
    #     output = list_calendars.formatted_data_output(data=list)
    #     self.assertEqual(type(output), list)


    # def test_get_date_and_time(self):
    #     output = list_calendars.get_date_and_time(date_time=datetime)
    #     self.assertEqual(type(output), str)


    def test_get_code_clinics_calendar(self):
<<<<<<< HEAD
=======
        """
        This tests the get_code_clinics_calandar() function
        """

>>>>>>> b10a7418481b6d76f486bc6e6ffdc1e8fa54226e
        output = list_calendars.get_code_clinics_calendar()
        self.assertEqual(type(output), list)


    def test_get_primary_calendar(self):
<<<<<<< HEAD
=======
        """
        This tests the get_primary_calendar()
        """

>>>>>>> b10a7418481b6d76f486bc6e6ffdc1e8fa54226e
        output = list_calendars.get_primary_calendar()
        self.assertEqual(type(output), list)


    """
    Test cases for the "patient" module
    """

    # def test_is_booking_valid(self):
    #     output = patient.is_booking_valid(id=str)
    #     self.assertEqual(type(output), bool)


    """
    Test cases for the "processing_data" module
    """

    def test_get_user(self):
<<<<<<< HEAD
=======
        """
        This tests the get_user() function
        """

>>>>>>> b10a7418481b6d76f486bc6e6ffdc1e8fa54226e
        output = processing_data.get_user()
        self.assertEqual(type(output), tuple)


<<<<<<< HEAD
    # def test_load_data(self):
    #     output = processing_data.load_data()
    #     self.assertSetEqual(type(output), None)
=======
    def test_load_data(self):
        """
        This tests the load_data() funciton
        """

        output = processing_data.load_data()
        self.assertEqual(type(output), list())
>>>>>>> b10a7418481b6d76f486bc6e6ffdc1e8fa54226e


    """
    Test cases for the "volunteer" module
    """

    def test_weekdays(self):
<<<<<<< HEAD
=======
        """ This tests the weekdays() function """

>>>>>>> b10a7418481b6d76f486bc6e6ffdc1e8fa54226e
        output = volunteer.weekdays(day=1)
        self.assertEqual(type(output), str)


    def test_is_volunteering_valid(self):
<<<<<<< HEAD
=======
        """ This tests is_volunteering() function """

>>>>>>> b10a7418481b6d76f486bc6e6ffdc1e8fa54226e
        output = volunteer.is_volunteering_valid(start=str, user_email=str)
        self.assertEqual(type(output), bool)


    @patch('bookings.volunteer.get_date', return_value='13')
    def test_get_date(self, input):
<<<<<<< HEAD
=======
        """ This tests get_date() """

>>>>>>> b10a7418481b6d76f486bc6e6ffdc1e8fa54226e
        output = volunteer.get_date()
        self.assertEqual(output, '13')


    @patch('bookings.volunteer.get_time',return_value='10:00:00')
    def test_get_time(self, input):
<<<<<<< HEAD
=======
        """ This tests get_time() function """

>>>>>>> b10a7418481b6d76f486bc6e6ffdc1e8fa54226e
        output = volunteer.get_time()
        self.assertEqual(output, '10:00:00')


    @patch('bookings.volunteer.get_summary_and_description', return_value='loops')
    def test_get_summary_and_description(self, input):
<<<<<<< HEAD
=======
        """ This tests get_summary_and_description() """

>>>>>>> b10a7418481b6d76f486bc6e6ffdc1e8fa54226e
        output = volunteer.get_summary_and_description()
        self.assertEqual(output, 'loops')


    @patch('bookings.volunteer.get_params',return_value=('13','10:00:00'))
    def test_get_params(self, input):
<<<<<<< HEAD
=======
        """ This tests the get_params """

>>>>>>> b10a7418481b6d76f486bc6e6ffdc1e8fa54226e
        output = volunteer.get_params()
        self.assertEqual(output, ('13','10:00:00'))


    # def test_create_event(self):
    #     output = volunteer.create_event(start=str,end=str,summary=str,description=str,email=str)
    #     self.assertEqual(type(output), dict)


if __name__ == "__main__":
    unittest.main()