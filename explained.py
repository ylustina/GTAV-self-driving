import cv2
import numpy as np
from PIL import ImageGrab

# put in comments to transfer to a jupyter notebook later

def roi(img, vertices):
    # creates a blank mask
    mask = np.zeros_like(img)

    # uses defined vertices to fill in the polygon
    cv2.fillPoly(mask, vertices, 255)

    # returns an image where mask pixels are nonzero
    masked = cv2.bitwise_and(img, mask)

    return masked


def draw_lines(img, lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), [255, 255, 255], 3)
    # TODO look up try excepts
    except:
        pass


def img_ops(image):

    # original unprocessed image
    original_img = image

    # converts the original image to grayscale
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    processed_img = cv2.GaussianBlur(processed_img, (3, 3), 0)

    vertices = np.array([[10, 500], [10, 300], [300, 200], [500, 200], [800, 300], [800, 500]], np.int32)
    processed_img = roi(processed_img, [vertices])

    lines = cv2.HoughLinesP(processed_img, 1, np.pi / 180, 180, np.array([]), 100, 5)
    draw_lines(processed_img, lines)

    return processed_img, original_img


def main():
    while True:
        screen = np.array(ImageGrab.grab(bbox=(0, 20, 800, 620)))

        new_screen, original_img = img_ops(screen)

        cv2.imshow('img_ops', new_screen)
        cv2.imshow('original_img', cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB))

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


# if you're not running this file directly, don't run this code
# TODO look up side effects

if __name__ == "__main__":
    main()
