import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from gamekeys import PressKey, W, A, S, D



def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked


def draw_lines(img, lines):
    for line in lines:
        coords = line[0]
        cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), [255, 255, 255], 3)



def main():


    while True:
        printscreen = np.array(ImageGrab.grab(bbox=(0, 20, 800, 620)))
        grayscale = cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(grayscale, threshold1=200, threshold2=300)

        vertices = np.array([[10, 500], [10, 300], [300, 200], [500, 200], [800, 300], [800, 500]], np.int32)

        r_of_int = roi(edges, [vertices])

        cv2.imshow('Edges', r_of_int)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()