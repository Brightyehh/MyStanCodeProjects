"""
File: best_photoshop_award.py
Name: Bright Yeh
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

THRESHOLD = 1.25
BLACK = 120


def main():
    """
    創作理念： A Surprising Discovery: stanCode will make Programming into Your Hobby!
    """
    fig = SimpleImage('images/fig1.jpg')  # 6200 x 4600
    fig.show()
    bg = SimpleImage('images/bg.png')  # 620 x 460
    bg.show()
    fig.make_as_big_as(bg)  # 620 x 460
    new_img = combine(fig, bg)
    new_img.show()


def combine(fig, bg):
    for x in range(fig.width):
        for y in range(fig.height):
            fig_p = fig.get_pixel(x, y)
            avg = (fig_p.red + fig_p.green + fig_p.blue) // 3
            total = fig_p.red + fig_p.green + fig_p.blue
            # green screen
            if fig_p.green > avg * THRESHOLD and total > BLACK:
                bg_p = bg.get_pixel(x, y)
                fig_p.red = bg_p.red
                fig_p.green = bg_p.green
                fig_p.blue = bg_p.blue
    return fig


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
