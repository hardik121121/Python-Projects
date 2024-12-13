import numpy as np
import cv2
import imutils
import datetime

# Load the pre-trained cascade classifier
gun_cascade = cv2.CascadeClassifier('cascade.xml')

# Check if the cascade file is loaded properly
if gun_cascade.empty():
    print("Error loading cascade file")
    exit()

# Initialize camera (0 is the default camera)
camera = cv2.VideoCapture(0)

# Initialize variables
firstFrame = None
gun_exist = False

while True:
    ret, frame = camera.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Resize the frame to improve performance
    frame = imutils.resize(frame, width=500)

    # Convert the frame to grayscale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect guns in the frame
    guns = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))

    # If guns are detected, set gun_exist to True
    if len(guns) > 0:
        gun_exist = True

    # Draw rectangles around detected guns
    for (x, y, w, h) in guns:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the current frame
    cv2.imshow("Security Feed", frame)

    # Wait for the 'q' key to exit the loop
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# After the loop finishes, print the detection result
if gun_exist:
    print("Guns Detected!")
else:
    print("No Guns were detected")

# Release the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
