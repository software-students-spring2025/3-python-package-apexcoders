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
    parser = argparse.ArgumentParser(
        description="GameMaster - A Fun Party Game Generator! 🎲\n"
        "Use the following commands to play different party games."
    )

    parser.add_argument(
        "--bottle",
        nargs="+",
        help="Spin the bottle with a list of names.\n"
        "Example: python -m game_master --bottle Alice Bob Charlie",
    )

    parser.add_argument(
        "--countdown",
        type=int,
        help="Countdown timer in seconds.\n"
        "Example: python -m game_master --countdown 10",
    )

    parser.add_argument(
        "--punish",
        nargs="+",
        help="Punish a random number of players from a list.\n"
        "Example: python -m game_master --punish 2 Alice Bob Charlie",
    )

    parser.add_argument(
        "--game",
        type=int,
        help="Suggest a random game for 2, 4, 6, or 8 players.\n"
        "Example: python -m game_master --game 4",
    )

    parser.add_argument(
        "--dare",
        type=str,
        help="Generate a random dare based on difficulty level (easy, medium, hard).\n"
        "Example: python -m game_master --dare hard",
    )

    args = parser.parse_args()
    try:
        if args.bottle:
            print("Bottle is spinning..." + spin_the_bottle(args.bottle))

        elif args.countdown:
            print("Start counting...")
            result = countdown(args.countdown)
            print(f"Countdown finished at: {result}")

        elif args.punish:
            num = int(args.punish[0])
            names = args.punish[1:]
            print(random_multiple_people_punishment(num, names))

        elif args.game:
            print(random_game_idea(args.game))

        elif args.dare:
            print(random_dare(args.dare))

        else:
            print("Use --help to see available options.")
    except (ValueError, Exception) as e:
        print(f"Error: {e}")  # Print the custom or unexpected error message
        print("Please check your input and try again.")


if __name__ == "__main__":
    # run the main function
    main()
