# gamejams-quisling

**Studio Rakkas**' contribution to the **pyWeek38** game jam, with the theme "Traitor".

## Requirements

To run this project, ensure you have at least **Python 3.12** installed.

### Installation

You can run the game without installing dependencies globally by using a virtual environment, to do so, navigate to the quisling directory and then:

1. **Create a virtual environment:**
   ```bash
   pipenv run install-req
   ```

2. **Run the game:**
   ```bash
   pipenv run start 
   ```

### Alternative: Install Globally

1. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the game:**
   - Using terminal:
     ```bash
     python path/to/main.py
     ```
   - Or run main.py within your IDE.

## How to play the game

This is a 2-player game where players take turns making their moves. Here’s how it works:

1. Each player takes turns to make their moves.
2. When you are satisfied with your round or if you run out of stamina, click End Turn. This resets your position, and it becomes the next player's turn.
3. After both players have completed their turns, the Resolve moves phase begins. During this phase, players moves gets executed at the same time.
4. If a player is hit by an attack, they lose health. The game ends when one player's health reaches zero, and the other player is declared the winner.

## Enjoy the Game!
Feel free to reach out for any issues or feedback. Happy gaming!


