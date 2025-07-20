# constants.py

# Screen configuration
SCREEN_WIDTH = 800            # width of the game window in pixels
SCREEN_HEIGHT = 600           # height of the game window in pixels
BG_COLOR = "black"           # background color of the game window
TITLE = "Breakout Game by Juldah, 100daysofcode"      # title of the game window

# Paddle settings
PADDLE_WIDTH = 100            # paddle width in pixels
PADDLE_HEIGHT = 20            # paddle height in pixels
PADDLE_SPEED = 20             # paddle movement speed in pixels per key press

# Ball settings
BALL_RADIUS = 10              # radius of the ball in pixels
BALL_SPEED = 5                # initial speed magnitude of the ball
BALL_DX = BALL_SPEED          # initial horizontal velocity component
BALL_DY = -BALL_SPEED         # initial vertical velocity component (moving upward)

# Brick layout settings
BRICK_ROWS = 5                # number of brick rows
BRICK_COLUMNS = 10            # number of brick columns
BRICK_WIDTH = 60              # width of each brick in pixels
BRICK_HEIGHT = 20             # height of each brick in pixels
BRICK_PADDING = 10            # space between adjacent bricks in pixels
BRICK_OFFSET_TOP = 50         # vertical offset from top edge to first brick row
BRICK_OFFSET_LEFT = 35        # horizontal offset from left edge to first brick column
BRICK_COLORS = [              # colors for each brick row (top to bottom)
    "red",
    "orange",
    "yellow",
    "green",
    "blue"
]

# Score and Lives display settings
FONT_NAME = "Arial"          # font for displaying text on screen
FONT_SIZE = 16                # size of the font for score and lives
FONT_COLOR = "white"         # color of the text for score and lives
SCORE_POSITION = (-350, 260)  # (x, y) position to display the score
LIVES_POSITION = (250, 260)   # (x, y) position to display remaining lives

# Game update rate
REFRESH_RATE = 20             # screen refresh interval in milliseconds
