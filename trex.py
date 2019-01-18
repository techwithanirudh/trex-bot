from PIL import ImageGrab, ImageOps
from numpy import array
from time import sleep
from pyautogui import keyDown, keyUp, click

# Position of the middle of the replay button.
replay_button = [480, 370]
# Position of dinosaurs right-top corner.
dinosaur = [221, 374]
# The size of the hitbox area in pixels.
hitbox_area = [60, 0, 100, 30]
# Distance of the hitbox away from the dinosaur.
hitbox_distance = 0

def jump():
    keyDown('space')
    sleep(0.05)
    keyUp('space')

def hitbox():
    area = (dinosaur[0] + hitbox_distance + hitbox_area[0],
            dinosaur[1] + hitbox_distance + hitbox_area[1],
            dinosaur[0] + hitbox_distance + hitbox_area[2],
            dinosaur[1] + hitbox_distance + hitbox_area[3])
    # Grab an image of the size of the area.
    image = ImageGrab.grab(area)
    # Grayscale the image.
    grayscale_image = ImageOps.grayscale(image)
    # Get each pixel color and put it in an array.
    image_colors = array(grayscale_image.getcolors())
    # Return the sum of the array.
    return image_colors.sum()

def end():
    end = (380, 130, 580, 160)
    # Grab an image of the size of the end area.
    image = ImageGrab.grab(end)
    # Grayscale the image.
    grayscale_image = ImageOps.grayscale(image)
    # Get each pixel color and put it in an array.
    image_colors = array(grayscale_image.getcolors())
    # Return the sum of the array.
    return image_colors.sum()

def main():
    click(replay_button)
    while True:
        """
        If the sum of the hitbox array changes, it means one of the pixels
        has changed its color (greyscale in our case), therefore something
        has entered the hitbox.
        """
        if(hitbox() != 1447):
            jump()
            sleep(0.1)
        """
        Same technique is applied to stop the loop. When the game is over,
        a text appears at the top of the game, but that area is empty when
        the game is running. So as soon as the text appears, the loop breaks.
        """
        if(end() != 6247):
            break

main()     