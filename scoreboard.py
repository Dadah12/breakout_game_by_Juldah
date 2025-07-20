# scoreboard.py
import turtle
import os
from constants import (
    FONT_NAME, FONT_SIZE, FONT_COLOR,
    SCORE_POSITION, LIVES_POSITION
)

HIGHSCORE_FILE = "highscore.txt"

class Scoreboard(turtle.Turtle):
    """
    Scoreboard handles displaying and updating the player's score, lives,
    and tracks the all-time high score persistently.
    """

    def __init__(self, initial_lives: int):
        """
        Initialize the scoreboard with starting score, lives,
        and load the high score from file.

        Args:
            initial_lives (int): Number of lives at game start.
        """
        super().__init__()
        self.score = 0
        self.lives = initial_lives
        # Load high score or default to 0
        if os.path.exists(HIGHSCORE_FILE):
            try:
                with open(HIGHSCORE_FILE, 'r') as f:
                    self.highscore = int(f.read().strip())
            except Exception:
                self.highscore = 0
        else:
            self.highscore = 0

        self.penup()
        self.hideturtle()
        self.color(FONT_COLOR)
        self.speed(0)
        self._display()

    def _display(self):
        """
        Draw the current score, high score, and lives at designated positions.
        """
        # Score and high score
        self.goto(SCORE_POSITION)
        self.write(
            f"Score: {self.score}  High Score: {self.highscore}",
            align="left",
            font=(FONT_NAME, FONT_SIZE, "normal")
        )
        # Lives
        self.goto(LIVES_POSITION)
        self.write(
            f"Lives: {self.lives}",
            align="left",
            font=(FONT_NAME, FONT_SIZE, "normal")
        )

    def _refresh(self):
        """
        Clear and redraw the score display.
        """
        self.clear()
        self._display()

    def add_score(self, points: int):
        """
        Increase the score, update high score if beaten, and refresh display.

        Args:
            points (int): points to add.
        """
        self.score += points
        if self.score > self.highscore:
            self.highscore = self.score
            try:
                with open(HIGHSCORE_FILE, 'w') as f:
                    f.write(str(self.highscore))
            except Exception:
                pass
        self._refresh()

    def lose_life(self):
        """
        Decrement lives by one and refresh display.
        """
        self.lives -= 1
        self._refresh()

    def game_over(self):
        """
        Display "GAME OVER" at the center of the screen.
        """
        self.goto(0, 0)
        self.write(
            "GAME OVER",
            align="center",
            font=(FONT_NAME, FONT_SIZE * 2, "bold")
        )

    def win(self):
        """
        Display "YOU WIN!" at the center of the screen.
        """
        self.goto(0, 0)
        self.write(
            "YOU WIN!",
            align="center",
            font=(FONT_NAME, FONT_SIZE * 2, "bold")
        )
