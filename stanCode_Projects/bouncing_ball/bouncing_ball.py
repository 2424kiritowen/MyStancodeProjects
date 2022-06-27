"""
File: bouncing ball
Name: Danny
-------------------------
Pre-condition: The program shows a ball, while user clink the mouse, the ball starts to bounce.
Post-condition: After three times of click, the ball will stop bouncing and stick to the original point.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40


window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
is_not_click = False
count = 1


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball)
    if not is_not_click:
        onmouseclicked(bounce)


def bounce(event):
    vy = 0
    global is_not_click
    global count
    if not is_not_click and count < 4:
        is_not_click = True
        while True:
            ball.move(VX, vy)
            vy += GRAVITY
            pause(DELAY)
            if ball.y >= window.height:
                vy = -(vy*REDUCE)
                pause(DELAY)
            if ball.x >= window.width:
                is_not_click = False
                count += 1
                break
        ball.x = START_X
        ball.y = START_Y











if __name__ == "__main__":
    main()
