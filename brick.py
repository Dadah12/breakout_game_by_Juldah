# brick.py
import turtle
from constants import (
    BRICK_ROWS, BRICK_COLUMNS,
    BRICK_WIDTH, BRICK_HEIGHT,
    BRICK_PADDING, BRICK_OFFSET_TOP,
    BRICK_OFFSET_LEFT, BRICK_COLORS
)

class Brick(turtle.Turtle):
    """
    Represents a single brick in the Breakout game.
    Inherits from turtle.Turtle to draw and manage its state.
    """

    def __init__(self, x: float, y: float, color: str):
        """
        Initialize a brick at the given position with the specified color.

        Args:
            x (float): The x-coordinate for the brick's center.
            y (float): The y-coordinate for the brick's center.
            color (str): The fill color of the brick.
        """
        super().__init__()
        self.shape("square")
        # Adjust the shape size: default square is 20x20 px
        self.shapesize(stretch_wid=BRICK_HEIGHT/20, stretch_len=BRICK_WIDTH/20)
        self.color(color)
        self.penup()
        self.goto(x, y)

    def destroy(self):
        """
        Remove the brick from the screen and hide it.
        Call this when the ball collides with the brick.
        """
        self.hideturtle()
        self.clear()


def create_bricks():
    """
    Create and return a list of Brick instances arranged in a grid.

    Uses constants for rows, columns, spacing, and colors.

    Returns:
        list[Brick]: All bricks placed on the screen.
    """
    bricks = []
    # Calculate starting positions based on constants
    for row in range(BRICK_ROWS):
        for col in range(BRICK_COLUMNS):
            x = - (BRICK_COLUMNS * (BRICK_WIDTH + BRICK_PADDING) - BRICK_PADDING) / 2
            x += col * (BRICK_WIDTH + BRICK_PADDING) + BRICK_WIDTH / 2
            y = BRICK_OFFSET_TOP + row * (BRICK_HEIGHT + BRICK_PADDING)
            # Select color per row
            color = BRICK_COLORS[row % len(BRICK_COLORS)]
            brick = Brick(x, y, color)
            bricks.append(brick)
    return bricks
