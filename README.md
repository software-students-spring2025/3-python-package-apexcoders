![CI/CD Build & Test](https://github.com/software-students-spring2025/3-python-package-apexcoders/actions/workflows/ci.yml/badge.svg)

# Game Master



An entertaining Python package that helps make party games more fun by providing random game ideas, challenges, and tools for game masters and party hosts.

## Description

Game Master is a fun and lighthearted Python package designed to bring joy to your gatherings. It provides a variety of functions to help you run party games, including selecting random participants, generating game ideas, creating dares, managing countdowns, and more.

[View Game Master on PyPI](https://pypi.org/project/game-master/)

## Features

- Spin the bottle to randomly select participants
- Create countdown timers for game activities
- Generate random punishments for multiple players
- Suggest game ideas based on player count
- Create random dares with varying difficulty levels
- Randomly select who pays the bill
- Show help text with function descriptions

## Installation

Install Game Master using pip:

```bash
pip install game_master
```

## Usage

### Importing in Python Code

```python
from game_master import spin_the_bottle, countdown, random_multiple_people_punishment, random_game_idea, random_dare, who_pays_the_bill, show_help
```

### Function Examples

#### Spin the Bottle

```python
from game_master import spin_the_bottle

# Randomly select someone from a list of names
names = ["Rin", "Elena", "Tony", "Corrine"]
result = spin_the_bottle(names)
print(result)  # Output: "[Name] is selected!"
```

#### Countdown Timer

```python
from game_master import countdown

# Create a countdown timer for 30 seconds
end_time = countdown(30)
print(f"Timer ended at: {end_time}")
```

#### Random Punishment

```python
from game_master import random_multiple_people_punishment

# Select 2 people from a list and assign a random punishment
names = ["Rin", "Elena", "Tony", "Corrine"]
result = random_multiple_people_punishment(2, names)
print(result)  # Output: "[Name1], [Name2] must [punishment]!"
```

#### Random Game Idea

```python
from game_master import random_game_idea

# Get a random game idea for 4 players
game = random_game_idea(4)  # Accepts 2, 4, 6, or 8 players
print(game)  # Output: "Game for 4 players: [Game Idea]"
```

#### Random Dare

```python
from game_master import random_dare

# Generate a random dare with medium difficulty
dare = random_dare("medium")  # Accepts "easy", "medium", or "hard"
print(dare)  # Output: "[Random dare text]"
```

#### Who Pays the Bill

```python
from game_master import who_pays_the_bill

# Randomly select someone to pay the bill
names = ["Rin", "Elena", "Tony", "Corrine"]
payer = who_pays_the_bill(names)
print(f"{payer} will pay the bill!")
```

#### Show Help

```python
from game_master import show_help

# Display help information about all available functions
help_text = show_help()
print(help_text)
```

### Command Line Usage

You can also use Game Master from the command line:

```bash
# Spin the bottle
python -m game_master --bottle Rin Elena Tony Corrine

# Countdown timer
python -m game_master --countdown 30

# Random game idea
python -m game_master --game 4

# Random dare
python -m game_master --dare medium

# Show help
python -m game_master --help
```

## Example Program

Here's a complete example that uses all the functions:

```python
from game_master import (
    spin_the_bottle, 
    countdown, 
    random_multiple_people_punishment, 
    random_game_idea, 
    random_dare,
    who_pays_the_bill,
    show_help
)

def run_party_night():
    print("Welcome to Party Night!")
    
    # Set up player names
    players = ["Rin", "Elena", "Tony", "Corrine"]
    print(f"Players tonight: {', '.join(players)}")
    
    # Start with a game idea
    print("\nLet's start with a game:")
    game = random_game_idea(4)
    print(game)
    
    # Spin the bottle to pick a player
    print("\nLet's see who goes first...")
    chosen = spin_the_bottle(players)
    print(chosen)
    
    # Give a dare
    print("\nTime for a dare!")
    dare = random_dare("medium")
    print(f"Your dare is: {dare}")
    
    # Countdown for the dare
    print("\nYou have 10 seconds to complete the dare!")
    countdown(10)
    
    # Random punishment for multiple people
    print("\nTime for punishment!")
    punishment = random_multiple_people_punishment(2, players)
    print(punishment)
    
    # Decide who pays for pizza
    print("\nWho's paying for pizza tonight?")
    payer = who_pays_the_bill(players)
    print(f"{payer} will pay for pizza!")
    
    # Show help at the end
    print("\nNeed more ideas? Here's all you can do:")
    print(show_help())

if __name__ == "__main__":
    run_party_night()
```

## Development Setup

### Prerequisites

- Python 3.9 or higher
- pipenv

### Setup Steps

1. Clone the repository:
```bash
git clone https://github.com/software-students-spring2025/3-python-package-apexcoders.git
cd 3-python-package-apexcoders
```

2. Set up the virtual environment and install dependencies:
```bash
pipenv install --dev
```

3. Activate the virtual environment:
```bash
pipenv shell
```

### Testing

Run the tests with pytest:

```bash
pytest
```

### Building the Package

Build the package using the build module:

```bash
python -m build
```

This will create distribution packages in the `dist/` directory.

### Installing Locally for Development

You can install the package in development mode:

```bash
pip install -e .
```

## Contributing

1. Fork the repository
2. Create a new feature branch:
```bash
git checkout -b feature/your-feature-name
```

3. Make your changes and write tests
4. Run tests to ensure they pass:
```bash
pytest
```

5. Create a pull request to the `main` branch
6. Request a code review from another developer
7. After approval, merge the pull request and delete the feature branch

## Team

- [Tony Zhao](https://github.com/Tonyzsp)
- [Rin Qi](https://github.com/RinQi)
- [Corrine Huang](https://github.com/CorrineHuang)
- [Huixin Li](https://github.com/HuixinLi-Elena)

## License

This project is licensed under the GNU General Public License v3 (GPLv3) - see the LICENSE file for details.
