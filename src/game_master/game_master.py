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

def random_game_idea(num_players):
    # Validation
    if not isinstance(num_players, int):
        return "Error: The number of players involved in the game must be 2,4,6 or 8. Only numbers are allowed."
    if num_players <= 0:
        return "Error: The number of players involved in the game must be 2,4,6 or 8. Negative number are not allowed."
    if num_players not in {2,4,6,8}:
        return "Error: The number of players involved in the game must be 2,4,6 or 8."

    #Function: Returns a game idea based on the number of players.
    games = {
        2: [
            "Chess - A strategic board game.",
            "Checkers - A classic game of capturing pieces.",
            "Card Duel - Try out a fast-paced card game.",
            "Tic-Tac-Toe - Simple but intense!",
            "Jenga - Test your steady hands.",
            "Rock, Paper, Scissors - Best of 5 wins!"
        ],
        4: [
            "Werewolf - A social deduction game.",
            "UNO - A fun and chaotic card game.",
            "Codenames - Work in teams to find secret words.",
            "Exploding Kittens - A hilarious card game.",
            "Pictionary - Draw and guess words.",
            "Jenga - Can you survive the tower collapse?"
        ],
        6: [
            "Monopoly - The classic property trading game.",
            "Spyfall - Find out who the spy is!",
            "Hidden Role Party - A game of deception and deduction.",
            "Dixit - A game of imagination and storytelling.",
            "Coup - Bluff your way to victory!",
            "The Resistance - Can you find the traitors?"
        ],
        8: [
            "Mafia - A game of deception and strategy.",
            "Pictionary - A fun drawing and guessing game.",
            "Charades - Act out words without speaking.",
            "Team Trivia - Test your general knowledge in teams.",
            "Telestrations - A hilarious drawing game.",
            "Murder Mystery - Solve the crime as a team."
        ]
    }
    #select a random game based on given number of players
    return random.choice(games[num_players])


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
