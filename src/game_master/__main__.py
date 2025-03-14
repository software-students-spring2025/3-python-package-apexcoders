"""
In Python packages, this file called __main__.py is run when the package is run
directly from command line, as opposed to importing it into another program.
"""

import game_master


def main():
    """
    Display available functions using show_help().
    """
    print(game_master.show_help())


if __name__ == "__main__":
    # run the main function
    main()