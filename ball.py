# ball.py
import turtle
from constants import BALL_RADIUS, BALL_DX, BALL_DY

class Ball(turtle.Turtle):
    """
    Ball class represents the ball in the Breakout game.
    It inherits from turtle.Turtle and handles movement and bouncing.
    """

    def __init__(self):
        """
        Initialize the ball at the center of the screen with
        a circular shape, given radius, and initial velocity.
        """
        super().__init__()
        self.shape("circle")
        # Adjust shape size: default circle diameter is 20px
        self.shapesize(stretch_wid=BALL_RADIUS/10, stretch_len=BALL_RADIUS/10)
        self.color("white")
        self.penup()           # disable drawing trail
        self.speed(0)          # animation speed set to max
        self.goto(0, 0)        # start in the middle
        # set velocity components
        self.dx = BALL_DX
        self.dy = BALL_DY

    def move(self):
        """
        Move the ball by its current velocity.
        Called on each game loop iteration.
        """
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_x(self):
        """
        Invert the horizontal velocity component.
        Use when the ball hits a vertical surface or the paddle sides.
        """
        self.dx *= -1

    def bounce_y(self):
        """
        Invert the vertical velocity component.
        Use when the ball hits a horizontal surface or bricks.
        """
        self.dy *= -1

    def reset_position(self):
        """
        Reset the ball to the center of the screen and reverse
        its vertical direction so it moves toward the player.
        """
        self.goto(0, 0)
        self.bounce_y()
