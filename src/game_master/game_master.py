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
    if not names_list:
        return None
    # Simulate a roulette selection by randomly choosing a name
    return random.choice(names_list)


def random_game_idea(num_players):
    # Validation
    if not isinstance(num_players, int):
        return "Error: The number of players involved in the game must be 2,4,6 or 8. Only numbers are allowed."
    if num_players <= 0:
        return "Error: The number of players involved in the game must be 2,4,6 or 8. Negative number are not allowed."
    if num_players not in {2, 4, 6, 8}:
        return "Error: The number of players involved in the game must be 2,4,6 or 8."

    # Function: Returns a game idea based on the number of players.
    games = {
        2: [
            "Chess - A strategic board game.",
            "Checkers - A classic game of capturing pieces.",
            "Card Duel - Try out a fast-paced card game.",
            "Tic-Tac-Toe - Simple but intense!",
            "Jenga - Test your steady hands.",
            "Rock, Paper, Scissors - Best of 5 wins!",
        ],
        4: [
            "Werewolf - A social deduction game.",
            "UNO - A fun and chaotic card game.",
            "Codenames - Work in teams to find secret words.",
            "Exploding Kittens - A hilarious card game.",
            "Pictionary - Draw and guess words.",
            "Jenga - Can you survive the tower collapse?",
            ],
        6: [
            "Monopoly - The classic property trading game.",
            "Spyfall - Find out who the spy is!",
            "Hidden Role Party - A game of deception and deduction.",
            "Dixit - A game of imagination and storytelling.",
            "Coup - Bluff your way to victory!",
            "The Resistance - Can you find the traitors?",
            ],
        8: [
            "Mafia - A game of deception and strategy.",
            "Pictionary - A fun drawing and guessing game.",
            "Charades - Act out words without speaking.",
            "Team Trivia - Test your general knowledge in teams.",
            "Telestrations - A hilarious drawing game.",
            "Murder Mystery - Solve the crime as a team.",
             ],
    }
    
    # select a random game based on given number of players
    return random.choice(games[num_players])


def show_help():
    help_text = """
        Available Functions:
        1. random_multiple_people_punishment(2, ["Rin", "Elena", "Tony", "Corrine"]) - Selects 2 random people and gives them a punishment. 
        2. who_pays_the_bill(["Rin", "Elena", "Tony", "Corrine"]) - Randomly picks a person to pay the bill. 
        3. random_game_idea(4) - Suggests a random game for 4 players. 
        4. random_dare("medium") - Generates a random dare task. Choose from: "easy", "medium", or "hard".
        5. random_truth("medium") - Generates a truth question. Choose from: "easy", "medium", or "hard".
        6. spin_the_bottle(["Rin", "Elena", "Tony", "Corrine"]) - Picks a random person for a challenge. 
        7. countdown_timer(30) - Starts a 30-second countdown. 
        """
    return help_text.strip()
