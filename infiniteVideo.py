import cv2

while (True):
    # Displays the window infinitely
    key = cv2.waitKey(0)

    # Shuts down the display window and terminates
    # the Python process when a specific key is
    # pressed on the window.
    # 27 is the esc key
    # 113 is the letter 'q'
    if key == 27 or key == 113:
        break