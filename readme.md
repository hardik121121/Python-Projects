# 🔫 Gun Detection using OpenCV and Haar Cascade

This project is a **Gun Detection** system that uses OpenCV and a pre-trained Haar Cascade Classifier to detect guns in real-time from a webcam feed. When a gun is detected, it will draw bounding boxes around the detected objects and print a message confirming the detection.

## 🛠️ Technologies Used

- **Python** 🐍
- **OpenCV** 📷
- **Haar Cascade Classifier** 🔍

## 🚀 Features

- ✅ **Real-Time Gun Detection:** Detects guns in real-time from the webcam feed.
- ✅ **Bounding Boxes:** Draws bounding boxes around detected guns.
- ✅ **Detection Feedback:** Prints a message indicating whether a gun is detected or not after the webcam feed is closed.
- ✅ **Easy to Use:** Just run the script and press 'q' to stop detection.

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/gun-detection.git
   cd gun-detection
   ```

2. Install the required libraries:

   ```bash
   pip install opencv-python imutils
   ```

3. Make sure you have the Haar Cascade XML file for gun detection (`cascade.xml`). You can use your own or find pre-trained classifiers for gun detection online.

## 🧑‍💻 How to Run

1. Run the script:

   ```bash
   python gun_detection.py
   ```

2. The camera feed will start automatically. If a gun is detected, bounding boxes will be drawn around the detected guns.

3. Press **`q`** to stop the camera feed and see if a gun was detected or not in the final output.

## 📸 Demo


### Gun Detection Result:
![Gun Detected](https://github.com/hardik121121/Weapon_Detection_Using_Open_Cv/blob/main/assets/Model_check.png?raw=true)




## 🤖 How It Works

1. **Camera Feed**: The webcam is initialized using OpenCV, and frames are captured in real-time.
2. **Pre-processing**: Each frame is converted to grayscale to speed up the detection process.
3. **Gun Detection**: The Haar Cascade Classifier is used to detect guns in each frame. If any guns are detected, bounding boxes are drawn around them.
4. **Final Output**: After closing the webcam feed, a message is displayed to indicate whether a gun was detected or not.

## 🔧 Troubleshooting

- If you get an error about the cascade file, ensure that the `cascade.xml` file is in the correct directory.
- Make sure the webcam is working and not being used by other applications.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

🚀 **Feel free to contribute!** If you have ideas or improvements, feel free to open an issue or submit a pull request.
