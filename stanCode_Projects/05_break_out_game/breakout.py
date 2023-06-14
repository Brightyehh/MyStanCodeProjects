"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
import math


FRAME_RATE = 10         # 100 frames per second, initial 10
NUM_LIVES = 3			# Number of attempts, initial3


def main():
    graphics = BreakoutGraphics()
    graphics.set_ball_velocity()
    dx = graphics.get_dx()
    dy = graphics.get_dy()
    lives = NUM_LIVES

    # Add the animation loop here!
    while True:
        pause(FRAME_RATE)
        brick_num = graphics.brick_num
        remove_num = graphics.remove_num
        # Check if clear
        if brick_num == remove_num:
            break
        # Check the lives
        if graphics.ball_out_of_window():
            lives -= 1
            graphics.reset_ball()
            graphics.set_ball_velocity()
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            if lives == 0:
                break
        # Check the condition and moving the ball, collision with window
        if graphics.start:
            if graphics.moving:
                graphics.ball.move(dx, dy)
        if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
            dx = -dx
        if graphics.ball.y <= 0:
            dy = -dy
        # collision 1 ball upper point, 2 for lower point, 3 for left point, 4 for right point
        # use math.fabs to avoid the problem that ball stack in the paddle
        if graphics.collision_1():
            dy = math.fabs(dy)
        if graphics.collision_2():
            dy = -math.fabs(dy)
        if graphics.collision_3():
            dx = math.fabs(dx)
        if graphics.collision_4():
            dx = -math.fabs(dx)


if __name__ == '__main__':
    main()
