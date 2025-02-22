import os
import cv2
import numpy as np
import tensorflow as tf
import serial
import time
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import DepthwiseConv2D

# Disable OneDNN optimizations
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

# Prevent scientific notation
np.set_printoptions(suppress=True)

# Handle custom DepthwiseConv2D layer
class CustomDepthwiseConv2D(DepthwiseConv2D):
    def __init__(self, *args, **kwargs):
        kwargs.pop("groups", None)
        super().__init__(*args, **kwargs)

# Loadig the keras model from files
model_path = "C:/Users/toddk/Downloads/converted_keras/keras_Model.h5"  
model = load_model(model_path, compile=False, custom_objects={"DepthwiseConv2D": CustomDepthwiseConv2D})

# Loading class labels from files
labels_path = "C:/Users/toddk/Downloads/converted_keras/labels.txt"
with open(labels_path, "r") as f:
    class_names = [line.strip() for line in f.readlines()] 

# Initialize webcam
camera = cv2.VideoCapture(0)

#serial communication with Arduino
arduino = serial.Serial('COM3', 9600)
time.sleep(2) 

while True:
    ret, frame = camera.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Resize image to model's input size
    resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)

    # Prepare image for model
    image_array = np.asarray(resized_frame, dtype=np.float32).reshape(1, 224, 224, 3)
    image_array = (image_array / 127.5) - 1  # Normalize

    # Make prediction
    prediction = model.predict(image_array)
    index = np.argmax(prediction)
    class_name = class_names[index]  # Get class label
    confidence_score = round(prediction[0][index] * 100, 2)  # Better rounding

    # Display prediction
    print(f"Class: {class_name} | Confidence: {confidence_score}%")

    # Debugging print to check the class detected
    print(f"Detected class: {class_name}")

    # Check if the detected class corresponds to 'hungry' (adjust based on your class names)
    if class_name.lower() == "1 hungry":  
        print("Sending '1' to Arduino")  # Debugging print
        arduino.write(b'1')  # Trigger buzzer
    else:
        print("Sending '0' to Arduino")  # Debugging print
        arduino.write(b'0')  # Stop buzzer

    # Display the frame
    cv2.putText(frame, f"{class_name} {confidence_score}%", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow("Webcam Image", frame)

    # Press ESC to exit
    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()
arduino.close()  # Close the serial connection
