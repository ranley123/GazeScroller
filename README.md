# Gaze Scroller

![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)


This is a Python (2 and 3) library that provides a **Gaze-Tracking Scroller** based on deep learning models. It is based on [GazeTracking](https://github.com/antoinelame/GazeTracking) repository by identifying real-time position of the pupils and the gaze direction. Apart from that, this project implements a scroller function helping to scroll every document-like pages!

## Installation

Clone this project:

```shell
git clone https://github.com/ranley123/GazeScroller.git
```

### For Pip install
Install these dependencies (NumPy, OpenCV, Dlib):

```shell
pip install -r requirements.txt
```

### For Anaconda install
Install these dependencies (NumPy, OpenCV, Dlib):

```shell
conda env create --file environment.yml
#After creating environment, activate it
conda activate GazeTracking
```


### Verify Installation

Run the demo:

```shell
python test.py
```

## Simple Demo

```python
import cv2
from gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

while True:
    _, frame = webcam.read()
    gaze.refresh(frame)

    new_frame = gaze.annotated_frame()
    text = ""

    if gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"

    cv2.putText(new_frame, text, (60, 60), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, 0), 2)
    cv2.imshow("Demo", new_frame)

    if cv2.waitKey(1) == 27:
        break
```


## Licensing

This project is released by Antoine Lamé under the terms of the MIT Open Source License. View LICENSE for more information.
