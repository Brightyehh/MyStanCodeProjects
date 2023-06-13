"""
File: stanCodoshop.py
Name: 
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    # color_dis = ((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)**0.5
    return ((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)**0.5


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    # n = 0
    # red_amount = 0
    # green_amount = 0
    # blue_amount = 0
    # for pixel in pixels:
    #     red_amount += pixel.red
    #     green_amount += pixel.green
    #     blue_amount += pixel.blue
    #     n += 1
    # rgb_avg_lst = [red_amount//n, green_amount//n, blue_amount//n]
    # return rgb_avg_lst
    return [
        sum(map(lambda pixel: pixel.red, pixels)) // len(pixels),
        sum(map(lambda pixel: pixel.green, pixels)) // len(pixels),
        sum(map(lambda pixel: pixel.blue, pixels)) // len(pixels)]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    # avg_lst = get_average(pixels)  # ex. [avg_red, avg_green, avg_blue]
    # min_dist = float('inf')
    # best_pixel = (0, 0, 0)  # initial value for best pixel
    # for pixel in pixels:
    #     pixel_dist = get_pixel_dist(pixel, avg_lst[0], avg_lst[1], avg_lst[2])
    #     if pixel_dist < min_dist:
    #         min_dist = pixel_dist
    #         best_pixel = pixel
    # return best_pixel
    return min(list((get_pixel_dist(pixel, get_average(pixels)[0], get_average(pixels)[1], get_average(pixels)[2]),
                     pixel) for pixel in pixels), key=lambda t: t[0])[1]


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.


    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    # print(best1.red, best1.green, best1.blue)
    for x in range(width):
        for y in range(height):
            pixel_lst = []
            for image in images:
                pixel = image.get_pixel(x, y)
                pixel_lst.append(pixel)
            pixel_best = get_best_pixel(pixel_lst)
            result.get_pixel(x, y).red = pixel_best.red
            result.get_pixel(x, y).green = pixel_best.green
            result.get_pixel(x, y).blue = pixel_best.blue
    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
