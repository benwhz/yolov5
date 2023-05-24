# Importing all necessary libraries
import cv2
import os

# Read the video from specified path
cam = cv2.VideoCapture("J:\\goods_ai\\yolov5\\data\\videos\\3.mp4")

try:

    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

    if not os.path.exists('data\\frames'):
        os.makedirs('data\\frames')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 0

while (True):

    # reading from frame
    ret, frame = cam.read()

    if ret:
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

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
