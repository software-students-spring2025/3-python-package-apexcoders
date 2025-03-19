import random, time, datetime


def spin_the_bottle(name_list):
    # Validation
    if not isinstance(name_list, list):
        return "Error: The name list must be a list."

    if not all((isinstance(name, str) and name.strip()) for name in name_list):
        return "Error: Names in the name list must be a non-empty string."

    stripped_names = []
    for name in name_list:
        if name.strip():
            stripped_names.append(name.strip())

    if len(stripped_names) <= 0:
        return "Error: Name list must contain one or more person."

    if len(set(stripped_names)) < len(stripped_names):
        return "Error: Duplicate names are not allowed. Please provide unique names."

    # Function
    selected_people = random.choice(name_list)

    return f"{selected_people} is selected!"


def countdown(seconds):
    # Validation
    if not isinstance(seconds, int):
        return "Seconds must be a non-negative integer."
    if seconds <= 0:
        return "Seconds must be a non-negative integer."

    # Function
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer)
        time.sleep(1)
        seconds -= 1
    print("Time is up!")

    return datetime.datetime.now()


def random_multiple_people_punishment(num, name_list):
    # Validate if name_list is a list
    if not isinstance(name_list, list):
        return "Error: The name list must be a valid list."

    # Validate if all elements in name_list are non-empty strings
    if not all(isinstance(name, str) and name.strip() for name in name_list):
        return "Error: Please provide a list of non-empty strings."

    stripped_names = [name.strip() for name in name_list if name.strip()]

    # Check for duplicates
    if len(set(stripped_names)) < len(stripped_names):
        return "Error: Duplicate names are not allowed. Please provide unique names."

    if num <= 0:
        return "Error: The number of people to punish must be at least 1."

    if num > len(stripped_names):
        return f"Error: Cannot punish {num} people when only {len(stripped_names)} names are available."

    punishments = [
        "drink a shot!",
        "do 10 jumping jacks!",
        "sing a song!",
        "wear socks on your hands for the next round!",
        "speak in an accent for 5 minutes!",
    ]

    selected_people = random.sample(stripped_names, num)
    punishment = random.choice(punishments)

    return f"{', '.join(selected_people)} must {punishment}"


def random_truth(level_difficulty):
    if not isinstance(level_difficulty, str):
        return "Error: The level of difficulty must be a string. Enter easy, medium or hard to set the level of difficulty."
    if level_difficulty not in {"easy","medium","hard"}:
        return "Error: The level of difficulty entered must be easy, medium or hard"
    
    # Truth prompts based on difficulty level
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

    # Select a random truth question based on the difficulty level
    return random.choice(truths[level_difficulty])


def random_dare(difficulty):
    # Validation
    if not isinstance(difficulty, str):
        return "Error: The level of difficulty must be a string. Enter easy, medium or hard to set the level of difficulty."
    if difficulty not in {"easy", "medium", "hard"}:
        return "Error: The level of difficulty entered must be easy, medium or hard"

    # function: returns a random dare task based on the level of diffivulty
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
    return random.choice(dares.get(difficulty))


def who_pays_the_bill(names_list):
    """
    Randomly select one person from the provided list of names to pay the bill.

    Args:
        names_list (list of str): List of players' names.

    Returns:
        str or None: The chosen player's name, or None if the list is empty.
    """
    if not isinstance(names_list, list):
        raise ValueError("names_list must be a list of names.")

    if len(names_list) == 0:
        raise ValueError("names_list cannot be empty.")

    if len(set(names_list)) != len(names_list):
        raise ValueError("names_list cannot contain duplicates.")

    for name in names_list:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("names_list cannot contain empty or invalid strings.")


    # Simulate a roulette selection by randomly choosing a name
    return random.choice(names_list)


def random_game_idea(num_players):
    """
    Generate a random game idea based on the number of players (1 to 5 players supported).

    Args:
        num_players (int): The number of players.

    Returns:
        str: A recommended game idea for the specified number of players.
    """
    # Validation
    if not isinstance(num_players, int):
        return "Error: The number of players must be between 1 and 5. Only numbers are allowed."
    if num_players <= 0 or num_players > 5:
        return "Error: The number of players must be between 1 and 5."

    # Practical, easy-to-play games
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
    
    # select a random game based on given number of players
    return random.choice(games[num_players])


def show_help():
    help_text = """
        Available Functions:
        1. random_multiple_people_punishment(2, ["Rin", "Elena", "Tony", "Corrine"]) - Selects 2 random people and gives them a punishment. 
        2. who_pays_the_bill(["Rin", "Elena", "Tony", "Corrine"]) - Randomly picks a person to pay the bill. 
        3. random_game_idea(num) - Suggests a random game for 1-5 players. 
        4. random_dare("medium") - Generates a random dare task. Choose from: "easy", "medium", or "hard".
        5. random_truth("medium") - Generates a truth question. Choose from: "easy", "medium", or "hard".
        6. spin_the_bottle(["Rin", "Elena", "Tony", "Corrine"]) - Picks a random person for a challenge. 
        7. countdown_timer(30) - Starts a 30-second countdown. 
        """
    return help_text.strip()


