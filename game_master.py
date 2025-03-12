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
        "let someone draw something on your face with a marker!"
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


#test run or not
if __name__ == "__main__":
    print(random_multiple_people_punishment(2, ["Alice", "Bob", "Charlie", "David"]))
