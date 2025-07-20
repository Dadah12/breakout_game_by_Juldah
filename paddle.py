# paddle.py
import turtle
from constants import PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_SPEED, SCREEN_HEIGHT

class Paddle(turtle.Turtle):
    """
    Paddle class represents the player's paddle in the Breakout game.
    It inherits from turtle.Turtle.
    """

    def __init__(self, screen_width):
        """
        Initialize the paddle at the bottom center of the screen.

        Args:
            screen_width (int): width of the game screen, used to limit paddle movement.
        """
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=PADDLE_HEIGHT/20, stretch_len=PADDLE_WIDTH/20)
        self.color("white")
        self.penup()
        # Position paddle slightly above bottom using screen height constant
        self.goto(0, -SCREEN_HEIGHT/2 + PADDLE_HEIGHT/2)
        self.speed(0)
        self.screen_width = screen_width

    def move_left(self):
        """
        Move paddle left by PADDLE_SPEED, without going off-screen.
        """
        new_x = self.xcor() - PADDLE_SPEED
        left_limit = -self.screen_width/2 + PADDLE_WIDTH/2
        if new_x < left_limit:
            new_x = left_limit
        self.goto(new_x, self.ycor())

    def move_right(self):
        """
        Move paddle right by PADDLE_SPEED, without going off-screen.
        """
        new_x = self.xcor() + PADDLE_SPEED
        right_limit = self.screen_width/2 - PADDLE_WIDTH/2
        if new_x > right_limit:
            new_x = right_limit
        self.goto(new_x, self.ycor())
