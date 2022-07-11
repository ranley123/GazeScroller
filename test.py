from re import I
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
import cv2
from gaze_tracking import GazeTracking
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
# Set the layout for interface
driver.set_window_size(1000, 1000)
# Get the sample website to be scrolled
driver.get("https://medium.com/analytics-vidhya/machine-learning-algorithms-b8e182cbdf94")
# Scroll to the height of the whole webpage
js="window.scrollTo(0,40)" 
# # Execute the scroll order by webdriver
# driver.execute_script(js) 

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
i = 0

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    # if gaze.is_blinking():
    #     text = "Blinking"
    if gaze.is_up():
        text = "Looking up"
    elif gaze.is_bottom():
        text = "Looking bottom"
        i += 1
        driver.execute_script("window.scrollTo(0, {offset}*{times});".format(offset=30, times=i))  
        # print("scroll to {offset}*{times});".format(offset=30, times=i))

    elif gaze.is_center():
        text = "Looking center"

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break
   
webcam.release()
cv2.destroyAllWindows()