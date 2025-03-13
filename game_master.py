import random, time, datetime

def spin_the_bottle(name_list):
    if len(name_list)<=0:
        raise ValueError("name_list must contain one or more person.")
    selected_people = random.choice(name_list)
    
    return f"{selected_people} is selected!"

def countdown(seconds):
    if seconds < 0:
        raise ValueError("Seconds must be a non-negative number.")
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer)
        time.sleep(1)
        seconds -= 1
    print('Time is up!')
   
    return(datetime.datetime.now())

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
        "Speak in an accent for 5 minutes!"
    ]

    selected_people = random.sample(stripped_names, num)
    punishment = random.choice(punishments)
    
    return f"{', '.join(selected_people)} must {punishment}"


def show_help():
    help_text = """
    GameMaster Package - Party Game Assistant
    
    Available Functions:
    1. random_multiple_people_punishment(2, ["Rin", "Elena", "Tony", "Corrine"]) - Selects 2 random people and gives them a punishment. 
    2. who_pays_the_bill(["Rin", "Elena", "Tony", "Corrine"]) - Randomly picks a person to pay the bill. 
    3. random_game_idea(4) - Suggests a random game for 4 players. 
    4. random_dare("medium") - Generates a random dare task.
    5. random_truth_question("medium") - Generates a truth question. 
    6. spin_the_bottle(["Rin", "Elena", "Tony", "Corrine"]) - Picks a random person for a challenge. 
    7. countdown_timer(30) - Starts a 30-second countdown. 
    """
    print(help_text)



# Always execute this for testing    
show_help()
result = random_multiple_people_punishment(2, ["a"])
print(result)

