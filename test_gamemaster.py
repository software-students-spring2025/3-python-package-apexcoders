import pytest, datetime, random
from game_master import spin_the_bottle, countdown, random_multiple_people_punishment


class Tests:

    def test_spin_the_bottle(self):
        # Test：With valid input
        name_list = ["Rin", "Elena", "Tony", "Corrine"]
        actual = spin_the_bottle(name_list).split()[0]
        assert actual in name_list

        # Test: Input is not a list
        actual = spin_the_bottle("Rin, Elena, Tony, Corrine")
        assert (
            actual == "Error: The name list must be a list."
        ), "Should return error for non-list input"

        # Test: List with invalid entries (None, numbers, empty strings)
        actual = spin_the_bottle(["Rin", " ", ""])
        assert (
            actual == "Error: Names in the name list must be a non-empty string."
        ), "Should return error for invalid entries"
        actual = spin_the_bottle(["Rin", 42])
        assert (
            actual == "Error: Names in the name list must be a non-empty string."
        ), "Should return error for invalid entries"
        actual = spin_the_bottle(["Rin", None])
        assert (
            actual == "Error: Names in the name list must be a non-empty string."
        ), "Should return error for invalid entries"

        # Test: Empty list
        actual = spin_the_bottle([])
        assert (
            actual == "Error: Name list must contain one or more person."
        ), "Should return error for zero punishments"

        # Test: Duplicate names
        actual = spin_the_bottle(["Rin", "Rin", "Elena", "Tony"])
        assert (
            actual
            == "Error: Duplicate names are not allowed. Please provide unique names."
        ), "Should return error for duplicate names"

    def test_countdown(self):
        # Test: With valid input
        t = 3
        now = datetime.datetime.now()
        expected_low = now + datetime.timedelta(seconds=t)
        expected_high = now + datetime.timedelta(seconds=t + 1)
        actual = countdown(t)
        assert expected_low <= actual <= expected_high

        # Test: With invalid input
        t = "tester"
        actual = countdown(t)
        # assert actual == "Seconds must be a non-negative integer."
        assert (
            actual == "intended to test fail cases in github actions. Will revise later"
        )

        # Test: With invalid input
        t = None
        actual = countdown(t)
        assert actual == "Seconds must be a non-negative integer."

        # Test: With invalid input
        t = -1
        actual = countdown(t)
        assert actual == "Seconds must be a non-negative integer."

    def test_random_multiple_people_punishment(self):
        # Test: Valid input
        names = ["Rin", "Elena", "Tony", "Corrine"]
        result = random_multiple_people_punishment(2, names)
        assert isinstance(result, str), "Output should be a string"
        assert "must" in result, "Output should contain 'must'"

        # Test: Input is not a list
        result = random_multiple_people_punishment(2, "Rin, Elena, Tony")
        assert (
            result == "Error: The name list must be a valid list."
        ), "Should return error for non-list input"

        # Test: List with invalid entries (None, numbers, empty strings)
        result = random_multiple_people_punishment(2, ["Rin", "", None, 42])
        assert (
            result == "Error: Please provide a list of non-empty strings."
        ), "Should return error for invalid entries"

        # Test: Zero people to punish
        result = random_multiple_people_punishment(0, ["Rin", "Elena"])
        assert (
            result == "Error: The number of people to punish must be at least 1."
        ), "Should return error for zero punishments"

        # Test: More punishments than available names
        result = random_multiple_people_punishment(5, ["Rin", "Elena"])
        assert (
            result == "Error: Cannot punish 5 people when only 2 names are available."
        ), "Should return error for too many punishments"

        # Test: Handling duplicate names
        result = random_multiple_people_punishment(2, ["Rin", "Rin", "Elena", "Elena"])
        assert (
            result
            == "Error: Duplicate names are not allowed. Please provide unique names."
        ), "Should return error for duplicate names"

    # Run the test if this script is executed directly
    if __name__ == "__main__":
        pytest.main()
