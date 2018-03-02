import time

import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab

from gamekeys import PressKey, W, A, S, D


def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)

    return masked


def main():
    """


    :return:
    """

    while True:
        printscreen = np.array(ImageGrab.grab(bbox=(0, 20, 800, 620)))  # captures screen
        grayscale = cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY)  # screen is grayscale
        edges = cv2.Canny(grayscale, threshold1=200, threshold2=300)  # creates Canny edges

        vertices = np.array([[10, 500], [10, 300], [300, 200], [500, 200], [800, 300], [800, 500]], np.int32)
        r_of_int = roi(edges, [vertices])  # region of interest

        cv2.imshow('Edges', r_of_int)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    main()
