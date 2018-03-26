import cv2
import numpy as np
from PIL import ImageGrab


def draw_lines(img, lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), [255, 255, 255], 3)
    # TODO look up try excepts
    except:
        pass


def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)

    return masked


def process_img(original_image):
    # TODO look up docstrings PEP 257

    """
    Note:

    :param original_image:
    :return:

    """
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    processed_img = cv2.GaussianBlur(processed_img, (5, 5), 0)

    vertices = np.array([[10, 500], [10, 300], [300, 200], [500, 200], [800, 300], [800, 500]], np.int32)
    processed_img = roi(processed_img, [vertices])

    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180, 20, 15)
    draw_lines(processed_img, lines)

    return processed_img


def main():
    while True:
        screen = np.array(ImageGrab.grab(bbox=(0, 20, 800, 620)))
        new_screen = process_img(screen)

        cv2.imshow('window', new_screen)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


# if you're not running this file directly, don't run this code
# TODO look up side effects
if __name__ == "__main__":
    main()
