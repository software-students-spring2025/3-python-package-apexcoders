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

def random_multiple_people_punishment():
    """Selects multiple people and assigns a punishment."""
    names = input("Enter names separated by commas (e.g., Alice, Bob, Charlie): ").split(",")
    names = [name.strip() for name in names]
    if not names or names == [""]:
        print("No names entered. Try again!")
        return
    
    try:
        num = int(input("How many people should be punished? "))
        if num <= 0 or num > len(names):
            print("Invalid number of people.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    punishments = [
        "Drink a shot!",
        "Do 10 jumping jacks!",
        "Sing a song!",
        "Wear socks on your hands for the next round!",
        "Speak in an accent for 5 minutes!"
    ]
    
    selected_people = random.sample(names, num)
    punishment = random.choice(punishments)
    print(f"{', '.join(selected_people)} must {punishment}")

def show_help():
    help_text = """
    GameMaster Package - Party Game Assistant
    
    Available Functions:
    1. random_multiple_people_punishment() - Selects random people and gives them a punishment.
    2. who_pays_the_bill() - Randomly picks a person to pay the bill.
    3. random_game_idea() - Suggests a random game for a given number of players.
    4. random_dare() - Generates a random dare task.
    5. random_truth_question() - Generates a random truth question.
    6. spin_the_bottle() - Picks a random person for a challenge.
    7. countdown_timer() - Starts a countdown timer.
    """
    print(help_text)

# Always execute this
show_help()


#test run or not
if __name__ == "__main__":
    random_multiple_people_punishment() 
