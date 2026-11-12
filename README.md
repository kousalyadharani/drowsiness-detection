# Drowsiness Detection

Reconstructed from the portfolio description of Python/OpenCV/Dlib facial landmarks, eye-aspect-ratio detection, alerts, and a manuscript prepared for submission. It does not include the original paper, face images, Dlib model file, or a validated safety system.

## Run

`python3 drowsiness.py LANDMARKS.json --threshold 0.22 --sustained-seconds 1`

The JSON input is timestamped six-point eye landmarks for left and/or right eye. The program computes EAR and marks sustained low-EAR intervals. Landmark extraction from video is an optional adapter requiring OpenCV and Dlib; the included module focuses on the testable geometry and temporal rule. This prototype is not a medical or driver-safety device.

## Verify

`python3 -m unittest -v`
