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
        "Drink a shot!",
        "Do 10 jumping jacks!",
        "Sing a song!",
        "Wear socks on your hands for the next round!",
        "Speak in an accent for 5 minutes!",
    ]

    selected_people = random.sample(stripped_names, num)
    punishment = random.choice(punishments)

    return f"{', '.join(selected_people)} must {punishment}"


def random_dare(difficulty):
    # Validation
    if not isinstance(difficulty, str):
        return "Error: The level of difficulty must be a string. Enter easy, medium or hard to set the level of difficulty."
    if difficulty not in {"easy","medium","hard"}:
        return "Error: The level of difficulty entered must be easy, medium or hard"
    
    #function: returns a random dare task based on the level of diffivulty
    dares = {
        "easy": [
            "Do 10 jumping jacks.",
            "Dance for 30 seconds without music.",
            "Say a tongue twister three times fast.",
            "Spin around 10 times and try to walk straight.",
            "Hold a silly face for 1 minute.",
            "Talk in a funny accent for 2 minutes.",
            "Act like a monkey for the next 3 turns.",
            "Tell a joke and make everyone laugh."
        ],
        "medium": [
            "Meow like a cat for 30 seconds.",
            "Call a friend and sing them a song.",
            "Let another player draw something on your face with a marker.",
            "Send a funny text to the 5th person in your contact list.",
            "Walk like a duck for the next 3 minutes.",
            "Let another player post something on your social media.",
            "Do a freestyle rap about the group for 30 seconds.",
            "Mimic a celebrity and let others guess who you are."
        ],
        "hard": [
            "Drink a mixed drink created by other players.",
            "Let someone else change your profile picture for 10 minutes.",
            "Act like a famous movie character until your next turn.",
            "Send a voice note of you singing an embarrassing song to a friend.",
            "Wear socks on your hands for the rest of the game.",
            "Do 20 push-ups or take a shot.",
            "Reveal the last text message you sent.",
            "Call a random contact and confess your love to them."
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
    if not names_list:
        return None
    # Simulate a roulette selection by randomly choosing a name
    return random.choice(names_list)

def random_game_idea(players=4):
    """
    Generate a random game idea based on the number of players.

    Args:
        players (int): Number of players. Defaults to 4.

    Returns:
        str: A recommended game idea for the specified number of players.
    """
    # Add type checking for players parameter
    if not isinstance(players, int):
        return "Error: The number of players must be an integer."
        
    if players < 2:
        return "At least two players are required to play."
    
    # Define a list of game ideas suitable for a drinking game theme
    game_ideas = [
        "Truth or Dare",
        "Never Have I Ever",
        "Spin the Bottle",
        "Beer Pong",
        "Kings",
        "Flip Cup",
        "Drinking Roulette",
        "Card Game Challenge"
    ]
    
    idea = random.choice(game_ideas)
    return f"Game for {players} players: {idea}"



def show_help():
    help_text = """
        Available Functions:
        1. random_multiple_people_punishment(2, ["Rin", "Elena", "Tony", "Corrine"]) - Selects 2 random people and gives them a punishment. 
        2. who_pays_the_bill(["Rin", "Elena", "Tony", "Corrine"]) - Randomly picks a person to pay the bill. 
        3. random_game_idea(4) - Suggests a random game for 4 players. 
        4. random_dare("medium") - Generates a random dare task. Choose from: "easy", "medium", or "hard".
        5. random_truth_question("medium") - Generates a truth question. Choose from: "easy", "medium", or "hard".
        6. spin_the_bottle(["Rin", "Elena", "Tony", "Corrine"]) - Picks a random person for a challenge. 
        7. countdown_timer(30) - Starts a 30-second countdown. 
        """
    return help_text.strip()
