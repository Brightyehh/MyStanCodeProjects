"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random


BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels) (initial: 50)
PADDLE_OFFSET = 60     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball (initial: 5)
NUM_LIVES = 3		   # Number of attempts, initial3
BALL_COLOR = 'black'
BRICK_COLS_SAME_COLOR = 2
NORMAL_SCORE = 1
BONUS_SCORE = 2


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, lives=NUM_LIVES, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=self.window.height-paddle_offset+self.paddle.height)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = BALL_COLOR
        self.reset_ball()

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.reset_ball()

        # Initialize our mouse listeners
        self.moving = False
        self.start = False
        onmouseclicked(self.start_ball)
        onmousemoved(self.paddle_move)

        # for break condition
        self.brick_num = brick_rows * brick_cols
        self.remove_num = 0

        # for score label
        self.score = 0
        self.score_label = GLabel('Score: ' + str(self.score))
        self.score_label.font = '-12'
        self.window.add(self.score_label, x=0, y=self.window.height-self.score_label.height)

        # for lives
        self.live = lives
        self.live_label = GLabel('Live: ' + str(self.live))
        self.live_label.font = '-12'
        self.window.add(self.live_label, x=self.window.width-self.live_label.width-5, y=self.window.height - self.live_label.height)

        # Draw bricks
        n = BRICK_COLS_SAME_COLOR
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.bricks = GRect(brick_width, brick_height)
                self.bricks.filled = True
                if n*0 <= j < n*1:
                    self.bricks.fill_color = 'red'
                if n*1 <= j < n*2:
                    self.bricks.fill_color = 'orange'
                if n*2 <= j < n*3:
                    self.bricks.fill_color = 'yellow'
                if n*3 <= j < n*4:
                    self.bricks.fill_color = 'green'
                if n*4 <= j < n*5:
                    self.bricks.fill_color = 'blue'
                self.window.add(self.bricks, x=i*(brick_width+brick_spacing), y=j*(brick_height+brick_spacing))

    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def start_ball(self, __):
        self.start = True
        self.moving = True

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def paddle_move(self, event):
        self.paddle.x = event.x - (self.paddle.width/2)
        if self.paddle.x <= 0:
            self.paddle.x = 0
        if self.paddle.x+self.paddle.width >= self.window.width:
            self.paddle.x = self.window.width-self.paddle.width

    def ball_out_of_window(self):
        if self.ball.y + self.ball.height >= self.window.height:
            self.live -= 1
            self.start = False
            self.moving = False
            return True

    def reset_ball(self):
        self.set_ball_velocity()
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2, y=(self.window.height - self.ball.height) / 2)

    def collision_1(self):
        # upper left point
        # c1 = self.window.get_object_at(self.ball.x, self.ball.y)
        # upper point
        c1 = self.window.get_object_at(self.ball.x + self.ball.width/2, self.ball.y-1)
        if c1 is self.score_label or c1 is self.live_label:
            return None
        if c1 is not self.paddle and c1 is not None:
            # print(c1, c1.color, c1.fill_color)
            if c1.fill_color.r == 255:
                # print('Brick is RED')
                self.score += BONUS_SCORE
            self.score += NORMAL_SCORE
            self.window.remove(c1)
            self.remove_num += 1
        return c1

    def collision_2(self):
        # upper right point
        # c2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        # lower point
        c2 = self.window.get_object_at(self.ball.x + self.ball.width/2, self.ball.y+1 + self.ball.height)
        if c2 is self.score_label or c2 is self.live_label:
            return None
        if c2 is not self.paddle and c2 is not None:
            if c2.fill_color.r == 255:
                self.score += BONUS_SCORE
            self.score += NORMAL_SCORE
            self.window.remove(c2)
            self.remove_num += 1
        return c2

    def collision_3(self):
        # left lower point
        # c3 = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height)
        # left point
        c3 = self.window.get_object_at(self.ball.x-1, self.ball.y + self.ball.height/2)
        if c3 is self.score_label or c3 is self.live_label:
            return None
        if c3 is not self.paddle and c3 is not None:
            if c3.fill_color.r == 255:
                self.score += BONUS_SCORE
            self.score += NORMAL_SCORE
            self.window.remove(c3)
            self.remove_num += 1
        return c3

    def collision_4(self):
        # right lower point
        # c4 = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height)
        # right point
        c4 = self.window.get_object_at(self.ball.x+1 + self.ball.width, self.ball.y + self.ball.height/2)
        if c4 is self.score_label or c4 is self.live_label:
            return None
        if c4 is not self.paddle and c4 is not None:
            if c4.fill_color.r == 255:
                self.score += BONUS_SCORE
            self.score += NORMAL_SCORE
            self.window.remove(c4)
            self.remove_num += 1
        return c4

    def score_update(self):
        self.score_label.text = 'Score: ' + str(self.score)

    def live_update(self):
        self.live_label.text = 'Live: ' + str(self.live)

    def fail(self):
        if self.live == 0:
            gg = GLabel('GAME OVER')
            gg.font = '-40'
            self.window.add(gg, x=self.window.width/2-gg.width/2, y=self.window.height/2-gg.height/2)
            return True

    def clear(self):
        if self.brick_num == self.remove_num:
            return True
