import random, time, datetime


def spin_the_bottle(name_list):
    # Validation
    if not isinstance(name_list, list):
        return("Error: The name list must be a list.")

    if not all((isinstance(name, str) and name.strip()) for name in name_list):
        return("Error: Names in the name list must be a non-empty string.")

    stripped_names = []
    for name in name_list:
        if name.strip():
            stripped_names.append(name.strip())

    if len(stripped_names) <= 0:
        return("Error: Name list must contain one or more person.")

    if len(set(stripped_names)) < len(stripped_names):
        return("Error: Duplicate names are not allowed. Please provide unique names.")

    # Function
    selected_people = random.choice(name_list)

    return f"{selected_people} is selected!"


def countdown(seconds):
    # Validation
    if not isinstance(seconds, int):
        return("Seconds must be a non-negative integer.")
    if seconds <= 0:
        return("Seconds must be a non-negative integer.")

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
    if num > len(name_list):
        return "Error: Number of people to pick is greater than the list size."

    punishments = [
        "drink a shot!",
        "sing a song!",
        "do 10 push-ups!",
        "dance for 30 seconds!",
        "tell an embarrassing story!",
        "post an embarrassing childhood photo on social media!",
        "let someone else send a text from your phone!",
        "let someone draw something on your face with a marker!",
    ]

    selected_people = random.sample(name_list, num)
    punishment = random.choice(punishments)

    return f"{', '.join(selected_people)} must {punishment}"


def show_help():
    help_text = """
    GameMaster Package - Party Game Assistant
    
    Available Functions:
    1. random_multiple_people_punishment(num, name_list) - Selects 'num' people and gives them a random punishment.
    2. who_pays_the_bill(names_list) - Randomly picks a person to pay the bill.
    3. random_game_idea(players=4) - Suggests a random game for the given number of players.
    4. random_dare(level="medium") - Generates a random dare task.
    5. random_truth_question(level="medium") - Generates a random truth question.
    6. spin_the_bottle(names_list) - Picks a person for a challenge.
    7. countdown_timer(seconds) - Starts a countdown timer.
    """
    print(help_text)


# Always execute this
show_help()


# test run or not
if __name__ == "__main__":
    print(random_multiple_people_punishment(2, ["Alice", "Bob", "Charlie", "David"]))
