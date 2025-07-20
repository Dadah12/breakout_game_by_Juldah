# main.py

import turtle
import os
import atexit
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BG_COLOR,
    TITLE,
    REFRESH_RATE,
    BALL_RADIUS,
    PADDLE_WIDTH,
    PADDLE_HEIGHT,
    BRICK_WIDTH,
    BRICK_HEIGHT,
    BALL_DX,
    BALL_DY
)
from paddle import Paddle
from ball import Ball
from brick import create_bricks
from scoreboard import Scoreboard

SAVE_FILE = "savegame.txt"


def main():
    """
    Initialize game, show stage instructions, handle pause/resume,
    display level/state, and save progress on exit.
    """
    # Load saved level or default to 1
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, 'r') as f:
                level = int(f.read().strip())
        except Exception:
            level = 1
    else:
        level = 1

    # Save level on exit
    def save_level():
        with open(SAVE_FILE, 'w') as f:
            f.write(str(level))
    atexit.register(save_level)

    # Setup screen
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor(BG_COLOR)
    screen.title(TITLE)
    screen.tracer(0)
    screen.listen()

    # Create game objects
    paddle = Paddle(SCREEN_WIDTH)
    ball = Ball()
    # Scale ball speed by level
    ball.dx = BALL_DX * (1.1 ** (level - 1))
    ball.dy = BALL_DY * (1.1 ** (level - 1))
    bricks = create_bricks()
    scoreboard = Scoreboard(initial_lives=3)

    # State flags
    paused = True
    started = False

    # Writers for text
    instr_writer = turtle.Turtle()
    instr_writer.hideturtle()
    instr_writer.penup()
    instr_writer.color("white")
    level_writer = turtle.Turtle()
    level_writer.hideturtle()
    level_writer.penup()
    level_writer.color("white")
    pause_writer = turtle.Turtle()
    pause_writer.hideturtle()
    pause_writer.penup()
    pause_writer.color("white")

    # Show stage and controls instructions
    def show_instructions():
        instr_writer.clear()
        instr_writer.goto(0, 40)
        instr_writer.write(f"STAGE {level}", align="center", font=("Arial", 24, "bold"))
        instr_writer.goto(0, 0)
        instr_writer.write("Left click to start / Resume", align="center", font=("Arial", 16, "normal"))
        instr_writer.goto(0, -30)
        instr_writer.write("Right click to Pause / Press 'P' to toggle", align="center", font=("Arial", 16, "normal"))
        instr_writer.goto(0, -60)
        instr_writer.write("Use arrow keys or mouse to move paddle", align="center", font=("Arial", 16, "normal"))

    show_instructions()

    # Display current level
    def update_level_display():
        level_writer.clear()
        level_writer.goto(0, SCREEN_HEIGHT/2 - 30)
        level_writer.write(f"Level: {level}", align="center", font=("Arial", 16, "normal"))

    update_level_display()

    # Paddle control via mouse
    canvas = screen.getcanvas()
    def on_mouse_move(event):
        x = event.x - SCREEN_WIDTH/2
        half = PADDLE_WIDTH / 2
        x = max(-SCREEN_WIDTH/2 + half, min(SCREEN_WIDTH/2 - half, x))
        paddle.goto(x, paddle.ycor())
    canvas.bind("<Motion>", on_mouse_move)

    # Pause display
    def display_pause():
        pause_writer.clear()
        pause_writer.goto(0, 0)
        pause_writer.write("PAUSED", align="center", font=("Arial", 32, "bold"))

    def clear_pause():
        pause_writer.clear()

    # Pause and resume handlers
    def pause_game(x=None, y=None):
        nonlocal paused
        if started and not paused:
            paused = True
            display_pause()

    def resume_game(x=None, y=None):
        nonlocal paused, started
        if not started:
            started = True
            paused = False
            instr_writer.clear()
            game_loop()
        elif paused:
            paused = False
            clear_pause()
            game_loop()

    def toggle_pause():
        nonlocal paused
        if started:
            if paused:
                paused = False
                clear_pause()
                game_loop()
            else:
                paused = True
                display_pause()

    # Bind controls
    screen.onscreenclick(resume_game, btn=1)
    screen.onscreenclick(pause_game, btn=3)
    screen.onkeypress(toggle_pause, 'p')
    screen.onkeypress(toggle_pause, 'P')
    screen.onkeypress(paddle.move_left, 'Left')
    screen.onkeypress(paddle.move_right, 'Right')

    # Main game loop
    def game_loop():
        nonlocal level, bricks, paused
        if paused:
            return

        ball.move()

        # Wall collisions
        if ball.xcor() > SCREEN_WIDTH/2 - BALL_RADIUS or ball.xcor() < -SCREEN_WIDTH/2 + BALL_RADIUS:
            ball.bounce_x()
        if ball.ycor() > SCREEN_HEIGHT/2 - BALL_RADIUS:
            ball.bounce_y()
        # Paddle collision
        if (ball.ycor() < paddle.ycor() + PADDLE_HEIGHT/2 + BALL_RADIUS and
            abs(ball.xcor() - paddle.xcor()) < PADDLE_WIDTH/2 + BALL_RADIUS):
            ball.bounce_y()
        # Brick collision
        for brick in bricks:
            if ball.distance(brick) < max(BRICK_WIDTH, BRICK_HEIGHT)/2 + BALL_RADIUS:
                brick.destroy()
                bricks.remove(brick)
                scoreboard.add_score(10)
                ball.bounce_y()
                break
        # Bottom collision
        if ball.ycor() < -SCREEN_HEIGHT/2:
            scoreboard.lose_life()
            if scoreboard.lives == 0:
                # Reset level to 1
                level = 1
                # DELETE save file kung meron
                if os.path.exists(SAVE_FILE):
                    os.remove(SAVE_FILE)
                screen.title(f"{TITLE} - Game Over")
                scoreboard.game_over()
                return
            ball.reset_position()
        # Check level completion
        if not bricks:
            level += 1
            screen.title(f"{TITLE} - Level {level}")
            update_level_display()
            bricks = create_bricks()
            ball.dx *= 1.1
            ball.dy *= 1.1

        screen.update()
        screen.ontimer(game_loop, REFRESH_RATE)

    # Start main loop
    screen.mainloop()


if __name__ == "__main__":
    main()
