import pytest, datetime, random
from src.game_master.game_master import (
    spin_the_bottle,
    countdown,
    random_multiple_people_punishment,
    show_help,
    who_pays_the_bill,
    random_dare,
    random_truth,
    random_game_idea,
)


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

    def test_random_truth(self):
        # Test: Valid difficulty levels
        difficulties = ["easy", "medium", "hard"]
        truths = {
        "easy": [
            "What is your favorite food?",
            "Do you have a secret talent?",
            "What is the last movie you watched?",
            "Have you ever sung in the shower?",
            "Who is your celebrity crush?",
            "What is your favorite holiday destination?",
            "Have you ever had a funny dream? Describe it!",
            "What is your guilty pleasure?"
        ],
        "medium": [
            "What is one thing you regret doing?",
            "Have you ever lied to get out of trouble?",
            "What is the most embarrassing thing that has happened to you?",
            "What is your worst habit?",
            "What is the biggest secret you have kept from your parents?",
            "If you had to change one thing about yourself, what would it be?",
            "What is the weirdest thing you've ever eaten?",
            "Have you ever had a crush on a teacher?"
        ],
        "hard": [
            "What is the biggest lie you have ever told?",
            "Have you ever cheated on a test or in a game?",
            "What is the most illegal thing you have ever done?",
            "What is something you've never told anyone?",
            "Have you ever betrayed a friend's trust? What happened?",
            "What is the biggest mistake you have made in a relationship?",
            "What is the one thing you would never admit to your parents?",
            "Have you ever spread a rumor about someone?"
        ],
    }
        for difficulty in difficulties:
            result = random_truth(difficulty)
            assert isinstance(result, str), f"Output should be a string for difficulty '{difficulty}'."
            assert len(result) > 0, f"Output should not be empty for difficulty '{difficulty}'."
            assert any(result == truth for truth in truths[difficulty]), f"Output should match for a known truth in '{difficulty}'."

        # Test: Invalid difficulty levels
        result = random_truth("harder")
        assert result == "Error: The level of difficulty entered must be easy, medium or hard"

        result = random_truth("MEDIUM")
        assert result == "Error: The level of difficulty entered must be easy, medium or hard"

        result = random_truth("5")
        assert result == "Error: The level of difficulty entered must be easy, medium or hard"

        # Test: Non-string input
        result = random_truth(None)
        assert result == "Error: The level of difficulty must be a string. Enter easy, medium or hard to set the level of difficulty."

        result = random_truth(7)
        assert result == "Error: The level of difficulty must be a string. Enter easy, medium or hard to set the level of difficulty."

        result = random_truth([])
        assert result == "Error: The level of difficulty must be a string. Enter easy, medium or hard to set the level of difficulty."

        result = random_truth({})
        assert result == "Error: The level of difficulty must be a string. Enter easy, medium or hard to set the level of difficulty."

    def test_random_dare(self):
        # Test: Valid difficulty levels
        difficulties = ["easy", "medium", "hard"]
        dares = {
        "easy": [
            "Do 10 jumping jacks.",
            "Dance for 30 seconds without music.",
            "Say a tongue twister three times fast.",
            "Spin around 10 times and try to walk straight.",
            "Hold a silly face for 1 minute.",
            "Talk in a funny accent for 2 minutes.",
            "Act like a monkey for the next 3 turns.",
            "Tell a joke and make everyone laugh.",
        ],
        "medium": [
            "Meow like a cat for 30 seconds.",
            "Call a friend and sing them a song.",
            "Let another player draw something on your face with a marker.",
            "Send a funny text to the 5th person in your contact list.",
            "Walk like a duck for the next 3 minutes.",
            "Let another player post something on your social media.",
            "Do a freestyle rap about the group for 30 seconds.",
            "Mimic a celebrity and let others guess who you are.",
        ],
        "hard": [
            "Drink a mixed drink created by other players.",
            "Let someone else change your profile picture for 10 minutes.",
            "Act like a famous movie character until your next turn.",
            "Send a voice note of you singing an embarrassing song to a friend.",
            "Wear socks on your hands for the rest of the game.",
            "Do 20 push-ups or take a shot.",
            "Reveal the last text message you sent.",
            "Call a random contact and confess your love to them.",
        ],
    }
        for difficulty in difficulties:
            result = random_dare(difficulty)
            assert isinstance(result, str), f"Output should be a string for difficulty '{difficulty}'."
            assert len(result) > 0, f"Output should not be empty for difficulty '{difficulty}'."
            assert any(result == dare for dare in dares[difficulty]), f"Output should match a known dare for '{difficulty}'."

        # Test: Invalid difficulty levels
        result = random_dare("harder")
        assert result == "Error: The level of difficulty entered must be easy, medium or hard"

        result = random_dare("EASY")
        assert result == "Error: The level of difficulty entered must be easy, medium or hard"

        result = random_dare("123")
        assert result == "Error: The level of difficulty entered must be easy, medium or hard"

        # Test: Non-string input
        result = random_dare(None)
        assert result == "Error: The level of difficulty must be a string. Enter easy, medium or hard to set the level of difficulty."

        result = random_dare(5)
        assert result == "Error: The level of difficulty must be a string. Enter easy, medium or hard to set the level of difficulty."

        result = random_dare([])
        assert result == "Error: The level of difficulty must be a string. Enter easy, medium or hard to set the level of difficulty."

        result = random_dare({})
        assert result == "Error: The level of difficulty must be a string. Enter easy, medium or hard to set the level of difficulty."


    def test_who_pays_the_bill(self):
        # Test with valid input - names list
        names = ["Alice", "Bob", "Charlie"]
        result = who_pays_the_bill(names)
        # The chosen name must be one from the list
        assert result in names, "The selected name should be one of the provided names."
        # Verify the return type is string when names are provided
        assert isinstance(result, str), "The function should return a string when given a non-empty list"
        
        # Test with empty list
        result = who_pays_the_bill([])
        assert result == "Error: names_list cannot be empty.", "Should return error message for empty list"
        
        # Test with non-list input (string)
        result = who_pays_the_bill("Not a list")
        assert result == "Error: names_list must be a list of names.", "Should return error message for string input"
        
        # Test with non-list input (integer)
        result = who_pays_the_bill(1)
        assert result == "Error: names_list must be a list of names.", "Should return error message for integer input"
        
        # Test with non-list input (None)
        result = who_pays_the_bill(None)
        assert result == "Error: names_list must be a list of names.", "Should return error message for None input"
        
        # Test with list containing invalid entries
        result = who_pays_the_bill(["Alice", "", "Charlie"])
        assert result == "Error: names_list cannot contain empty or invalid strings.", "Should return error message for list with empty strings"
        
        # Test with duplicate names
        result = who_pays_the_bill(["Alice", "Bob", "Alice"])
        assert result == "Error: names_list cannot contain duplicates.", "Should return error message for duplicate names"


    def test_random_game_idea(self):
        """Test if random_game_idea() returns valid game suggestions from the correct category and handles errors properly."""

        #Test valid cases (must return a value from the corresponding game list)
        games = {
        1: [
            "Solitaire - A classic card game for one player.",
            "Sudoku - A logic puzzle to test your brain.",
            "Crossword Puzzle - Improve vocabulary while having fun.",
            "Tetris - A quick reflex block-stacking game.",
            "Memory Game - Challenge yourself to remember card positions.",
        ],
        2: [
            "Rock, Paper, Scissors - Best of 5 to determine the winner!",
            "Tic-Tac-Toe - Play on paper or an app!",
            "Chess - A deep strategic board game.",
            "Checkers - A simple yet fun game of capturing pieces.",
            "Table Tennis - If you have paddles and a ball, go for it!",
            "Arm Wrestling - Test your strength!",
        ],
        3: [
            "Three-way Rock, Paper, Scissors - Sudden death elimination!",
            "Uno - A fun and fast-paced card game.",
            "Truth or Dare - A classic game for laughs.",
            "20 Questions - One person thinks of something, others guess.",
            "Speed Typing Challenge - Who can type the fastest?",
        ],
        4: [
            "Cards Against Humanity - Hilarious fill-in-the-blank card game.",
            "Charades - Act out words without speaking.",
            "Pictionary - Draw and guess the word.",
            "Jenga - Test your steady hands!",
            "Simon Says - A fun game to test listening skills.",
        ],
        5: [
            "Mafia - A deception-based party game.",
            "Never Have I Ever - Share fun or embarrassing facts.",
            "Freeze Dance - Play music, and freeze when it stops!",
            "Would You Rather? - Make tough choices with friends.",
            "Musical Chairs - Remove a chair each round!",
        ],
        }

        for num_players in games.keys():
            result = random_game_idea(num_players)
            assert isinstance(result, str), f"Expected a string for {num_players} players, but got {type(result)}."
            assert result in games[num_players], f"Unexpected game suggestion '{result}' for {num_players} players."


        #Test invalid cases (should return error messages)
        invalid_inputs = [0, 6, -1, "two", None]
        expected_errors = [
            "Error: The number of players must be between 1 and 5.",
            "Error: The number of players must be between 1 and 5.",
            "Error: The number of players must be between 1 and 5.",
            "Error: The number of players must be between 1 and 5. Only numbers are allowed.",
            "Error: The number of players must be between 1 and 5. Only numbers are allowed.",
        ]

        for test_input, expected_error in zip(invalid_inputs, expected_errors):
            result = random_game_idea(test_input)
            assert result == expected_error, f"Expected '{expected_error}' for input {test_input}, but got '{result}'."


    def test_show_help(self):
        """Test if show_help() returns the correct help text."""

        expected_output = """
        Available Functions:
        1. random_multiple_people_punishment(2, ["Rin", "Elena", "Tony", "Corrine"]) - Selects 2 random people and gives them a punishment. 
        2. who_pays_the_bill(["Rin", "Elena", "Tony", "Corrine"]) - Randomly picks a person to pay the bill. 
        3. random_game_idea(4) - Suggests a random game for 4 players. 
        4. random_dare("medium") - Generates a random dare task. Choose from: "easy", "medium", or "hard".
        5. random_truth("medium") - Generates a truth question. Choose from: "easy", "medium", or "hard".
        6. spin_the_bottle(["Rin", "Elena", "Tony", "Corrine"]) - Picks a random person for a challenge. 
        7. countdown_timer(30) - Starts a 30-second countdown. 
        """

        actual_output = show_help()
        # Ensure function returns a string
        assert isinstance(
            actual_output, str
        ), "Expected show_help() to return a string."

        # Ensure the function returns the expected text
        assert (
            actual_output.strip() == expected_output.strip()
        ), "Help text output is incorrect."

        # Ensure the returned text has the correct length
        assert len(actual_output.strip()) == len(
            expected_output.strip()
        ), f"Expected length {len(expected_output.strip())}, but got {len(actual_output.strip())}"

    # Run the test if this script is executed directly
    if __name__ == "__main__":
        pytest.main()
