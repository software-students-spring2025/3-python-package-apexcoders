"""
In Python packages, this file called __main__.py is run when the package is run
directly from command line, as opposed to importing it into another program.
"""

import argparse
from .game_master import (
    spin_the_bottle,
    countdown,
    random_multiple_people_punishment,
    random_game_idea,
    random_dare,
)

def main():
    """
    Commandline interface for gameMaster package
    """
    parser = argparse.ArgumentParser(description="Welcome to GameMaster, a fun party game generator for you!")
    
    parser.add_argument('--bottle', nargs="+", help="Spin the bottle with a list of names.")
    parser.add_argument('--countdown', type=int, help="Countdown timer in second")
    parser.add_argument('--punish', nargs="+", help="Punish a random number of players from a list.")
    parser.add_argument("--game", type=int, help="Suggest a random game for 2, 4, 6, or 8 players.")
    parser.add_argument("--dare", type=str, help="Generate a random dare based on the level of difficulty(easy, medium, hard).")

    args = parser.parse_args()

    if args.bottle:
        print("Bottle is spinning..."+spin_the_bottle(args.bottle))

    elif args.countdown:
        print("Start counting...")
        result=countdown(args.countdown)
        print(f"Countdown finished at: {result}")

    elif args.punish:
        num = args.punish[0]
        names = args.push[1:]
        print(random_multiple_people_punishment(num, names))
    
    elif args.game:
        print(random_game_idea(args.game))

    elif args.dare:
        print(random_dare(args.dare))

    elif args.help_with_example:
        print(help())

    else:
        print("Use --help to see available options.")


if __name__ == "__main__":
    # run the main function
    main()