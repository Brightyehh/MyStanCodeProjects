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


def main():
    graphics = BreakoutGraphics(brick_rows=10, brick_cols=10, paddle_width=150)
    graphics.set_ball_velocity()
    dx = graphics.get_dx()
    dy = graphics.get_dy()

    # for check
    c1 = graphics.collision_1()
    c2 = graphics.collision_2()
    c3 = graphics.collision_3()
    c4 = graphics.collision_4()

    # Add the animation loop here!
    while True:
        pause(FRAME_RATE)
        # Check if clear
        if graphics.clear():
            break
        # Check the lives
        if graphics.ball_out_of_window():
            graphics.reset_ball()
            graphics.set_ball_velocity()
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            graphics.live_update()
            if graphics.fail():
                break
        # speed up!!!
        if graphics.remove_num >= graphics.brick_num/2:
            if graphics.start:
                if graphics.moving:
                    graphics.ball.move(dx*1.5, dy*1.5)
        # Check the condition and moving the ball, collision with window
        else:
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
        graphics.score_update()


if __name__ == '__main__':
    main()
