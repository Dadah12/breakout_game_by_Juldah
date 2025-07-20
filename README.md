# Breakout Game by Juldah

This is a Python implementation of the classic 80s arcade game **Breakout**, created using the `turtle` module. The player controls a paddle at the bottom of the screen to bounce a ball and break bricks arranged at the top. Features include levels, scoring, high score tracking, pause/resume functionality, mouse and keyboard controls, and game state persistence.

---

## Features

* **Classic Breakout gameplay** with paddle, ball, and brick wall.
* **Multiple levels**: Ball speed increases by 10% each level.
* **Persistent level save**: Player returns to the last unfinished level on restart.
* **High score tracking**: All-time high score saved in `highscore.txt`.
* **Pause & Resume**:

  * **Left click** to start or resume the game.
  * **Right click** or press **P** to pause the game.
* **Mouse & Keyboard Controls**:

  * Move paddle with **mouse movement** or **arrow keys**.
* **Stage Instructions**: Display stage number and controls on screen.
* **Restart on Game Over**: After losing all lives, click to restart from level 1.

---

## Installation & Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Dadah12/breakout_game_by_Juldah.git
   cd breakout_game_by_Juldah
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install requirements**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the game**:

   ```bash
   python main.py
   ```

---

## File Structure

* `main.py` - Main game logic, screen setup, event handling.
* `constants.py` - Configuration constants (dimensions, speeds, colors).
* `paddle.py` - Paddle class and movement logic.
* `ball.py` - Ball class with movement, bouncing, and sound effects.
* `brick.py` - Brick class and grid creation function.
* `scoreboard.py` - Scoreboard class with score, lives, and high score tracking.
* `highscore.txt` - Stores the all-time high score.
* `savegame.txt` - Stores the last unfinished level.

---

## Controls

* **Start/Resume**: Left-click anywhere on the game screen.
* **Pause**: Right-click or press **P**.
* **Move Paddle**: Move the mouse horizontally or press **Left/Right Arrow** keys.

---

## License

This project is open source and available under the [MIT License](LICENSE).

**Created by Juldah Torralba**
**Project: 100days of gold**
