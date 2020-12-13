import unittest
from calendar_setup import *
from datetime import *
from login.user_auth import *
from bookings.create_event import *

class MyProjectTest(unittest.TestCase):

    def test_get_date_time_return_type(self):
        date_and_time = get_time_date()
        self.assertTrue(type(get_time_date()), dict)


    def test_get_user_details_return_type(self):
        user_details = get_user_details()
        self.assertTrue(type(get_user_details()), dict)    


    def test_remove_token_return_type(self):
        is_found = remove_token()
        self.assertTrue(type(remove_token()), bool)

    # def test_date_and_time_google_str(self):
    #     date = date_and_time_str_google()
    #     self.assertEqual(type(date_and_time_str_google()), dict)


    def test_weekdays_returning_type(self):

        day = 1
        week_days = {
            1: "Monday",
        }
        week_days[day] = weekdays(day)
        self.assertEqual(type(weekdays(day)), str)


    def test_get_login_state_return_type(self):

        self.assertTrue(type(get_login_state()), bool)    

    #def get_user_event_input(self):
            





if __name__ == "__main__":
    unittest.main()        