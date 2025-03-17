import pytest, datetime, random
from src.game_master.game_master import spin_the_bottle, countdown, random_multiple_people_punishment, show_help, who_pays_the_bill, random_game_idea


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
        ), "Should return error for empty list"

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
        assert actual == "Seconds must be a non-negative integer."

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


    def test_who_pays_the_bill_with_names(self):
        names = ["Alice", "Bob", "Charlie"]
        result = who_pays_the_bill(names)
        # The chosen name must be one from the list
        assert result in names, "The selected name should be one of the provided names."

    def test_who_pays_the_bill_empty_list(self):
        result = who_pays_the_bill([])
        # When an empty list is provided, the function should return None
        assert result is None, "When the names list is empty, the function should return None."

    def test_random_game_idea_valid_players(self):
        players = 4
        result = random_game_idea(players)
        # Check that the output string starts with the expected prefix
        expected_prefix = f"Game for {players} players:"
        assert result.startswith(expected_prefix), f"The output should start with '{expected_prefix}'"

    def test_random_game_idea_invalid_players(self):
        # When there are less than two players, an error message should be returned.
        result = random_game_idea(players=1)
        assert "At least two players" in result, "For less than two players, the function should indicate that more players are needed."



    def test_show_help(self):
        """Test if show_help() returns the correct help text."""

        expected_output = """
        Available Functions:
        1. random_multiple_people_punishment(2, ["Rin", "Elena", "Tony", "Corrine"]) - Selects 2 random people and gives them a punishment. 
        2. who_pays_the_bill(["Rin", "Elena", "Tony", "Corrine"]) - Randomly picks a person to pay the bill. 
        3. random_game_idea(4) - Suggests a random game for 4 players. 
        4. random_dare("medium") - Generates a random dare task. Choose from: "easy", "medium", or "hard".
        5. random_truth_question("medium") - Generates a truth question. Choose from: "easy", "medium", or "hard".
        6. spin_the_bottle(["Rin", "Elena", "Tony", "Corrine"]) - Picks a random person for a challenge. 
        7. countdown_timer(30) - Starts a 30-second countdown. 
        """

        actual_output = show_help()
        # Ensure function returns a string
        assert isinstance(actual_output, str), "Expected show_help() to return a string."
    
        # Ensure the function returns the expected text
        assert actual_output.strip() == expected_output.strip(), "Help text output is incorrect."
    
        # Ensure the returned text has the correct length
        assert len(actual_output.strip()) == len(expected_output.strip()), f"Expected length {len(expected_output.strip())}, but got {len(actual_output.strip())}"

    # Run the test if this script is executed directly
    if __name__ == "__main__":
        pytest.main()
