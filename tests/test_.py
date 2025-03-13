import datetime, pytest
from game_master import spin_the_bottle, countdown


class Tests:

    def test_spin_the_bottle(self):
        #Test：With valid input
        name_list = ["Rin", "Elena", "Tony", "Corrine"]
        actual = spin_the_bottle(name_list).split()[0]
        assert actual in name_list

        # Test: Input is not a list
        actual = spin_the_bottle("Rin, Elena, Tony, Corrine")  # Call your function with an invalid input
        assert actual == "Error: The name list must be a list.", "Should return error for non-list input"

        # Test: List with invalid entries (None, numbers, empty strings)
        actual = spin_the_bottle(["Rin", " ", ""])
        assert actual == "Error: Names in the name list must be a non-empty string.", "Should return error for invalid entries"
        actual = spin_the_bottle(["Rin",42])
        assert actual == "Error: Names in the name list must be a non-empty string.", "Should return error for invalid entries"
        actual = spin_the_bottle(["Rin", None])
        assert actual == "Error: Names in the name list must be a non-empty string.", "Should return error for invalid entries"

        # Test: Empty list
        actual = spin_the_bottle([])
        assert actual == "Error: Name list must contain one or more person.", "Should return error for zero punishments"

        # Test: Duplicate names 
        actual = spin_the_bottle(["Rin", "Rin", "Elena", "Tony"])
        assert actual == "Error: Duplicate names are not allowed. Please provide unique names.", "Should return error for duplicate names"


    def test_countdown(self):
        #Test: With valid input
        t = 3
        now = datetime.datetime.now()
        expected_low = now + datetime.timedelta(seconds=t)
        expected_high = now + datetime.timedelta(seconds=t + 1)
        actual = countdown(t)
        assert expected_low <= actual <= expected_high

        #Test: With invalid input
        t = "tester"
        actual = countdown(t)
        assert actual == "Seconds must be a non-negative integer."

        #Test: With invalid input
        t = None
        actual = countdown(t)
        assert actual == "Seconds must be a non-negative integer."

        #Test: With invalid input
        t=-1
        actual = countdown(t)
        assert actual == "Seconds must be a non-negative integer."
