# Importing all necessary libraries
import cv2
import os
import numpy as np
from typing import Tuple

# Read the video from specified path
cam = cv2.VideoCapture("J:\\goods_ai\\yolov5\\data\\videos\\4.mp4")

try:

    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

    if not os.path.exists('data\\frames'):
        os.makedirs('data\\frames')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

def resize_with_pad(image: np.array, 
                    new_shape: Tuple[int, int], 
                    padding_color: Tuple[int] = (0, 0, 0)) -> np.array:
    """Maintains aspect ratio and resizes with padding.
    Params:
        image: Image to be resized.
        new_shape: Expected (width, height) of new image.
        padding_color: Tuple in BGR of padding color
    Returns:
        image: Resized image with padding
    """
    original_shape = (image.shape[1], image.shape[0])
    ratio = float(max(new_shape))/max(original_shape)
    new_size = tuple([int(x*ratio) for x in original_shape])
    image = cv2.resize(image, new_size)
    delta_w = new_shape[0] - new_size[0]
    delta_h = new_shape[1] - new_size[1]
    top, bottom = delta_h//2, delta_h-(delta_h//2)
    left, right = delta_w//2, delta_w-(delta_w//2)
    image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=padding_color)
    return image

# frame
currentframe = 0

while (True):

    # reading from frame
    ret, frame = cam.read()

    if ret:
        # if video is still left continue creating images
        frame = resize_with_pad(frame, (672, 672))

        name = './data/frames/frame_' + str(currentframe) + '.jpg'
        print('Creating...' + name)
        # writing the extracted images
        cv2.imwrite(name, frame)

        '''
        # if video is still left continue creating images
        upframe = frame [0:720, 0:1280]
        name = './data/frames/frame_' + str(currentframe) + '_up.jpg'
        print('Creating...' + name)
        # writing the extracted images
        cv2.imwrite(name, upframe)

        bottomframe = frame [720:1440, 0:1280]
        name = './data/frames/frame_' + str(currentframe) + '_bottom.jpg'
        print('Creating...' + name)
        # writing the extracted images
        cv2.imwrite(name, bottomframe)
        '''

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
