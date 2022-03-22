import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui

def screen_record():
    frame = 1062
    time.sleep(3)
    print("Starting...")
    while(True):
        # Check if no more pages left
        fullscreen = np.array(ImageGrab.grab())
        # print(fullscreen[1381, 2142][0] == 247)
        if fullscreen[1381, 2142][0] == 247:
            print('Last page found!')
            break

        load = np.array(ImageGrab.grab(bbox=(1000,300,1300,420)))

        # Check page load
        reloads = 0
        while np.mean(load) == 255 and reloads < 5:
            print("Waiting...")
            load = np.array(ImageGrab.grab(bbox=(1000,300,1300,420)))
            reloads += 1
            time.sleep(2)

        # Get page
        print(f'Capturing frame {frame}...')
        page = np.array(ImageGrab.grab(bbox=(707,152,1620,1326)))

        frame_name = str(frame).rjust(4, '0')
        cv2.imwrite(f'images/{frame_name}.png', cv2.cvtColor(page, cv2.COLOR_BGR2RGB))
        # cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        frame += 1

        # Reload page every 100 frames to remove out of memory errors
        if frame % 100 == 0:
            print("Reloading...")
            pyautogui.click(172, 30)
            time.sleep(15)

        pyautogui.click(2176, 1403)
        time.sleep(2)

screen_record()
