# Dog Hunger Detection Project  

This project uses **computer vision** with a **laptop camera** to detect when a dog is near its food bowl. If detected, the system sends a signal over **serial communication** to an **Arduino**, which triggers a buzzer.  

## Hardware  
- Arduino Mega  
- Buzzer  
- Laptop with Camera  

## Software  
- Python (OpenCV + TensorFlow for object detection)  
- Arduino IDE (for buzzer control)  
- Serial Communication (via `pyserial`)  

## How It Works  
1. The laptop's **camera** continuously monitors the food bowl.  
2. A **computer vision model** detects if the dog is near.  
3. If detected, a **signal is sent via serial** to the Arduino.  
4. The Arduino **activates a buzzer** to notify the owner.  

## Running the Project  
- Ensure Python and dependencies are installed (`pip install tensorflow opencv-python pyserial`).  
- Upload the Arduino code (`Project1AID.ino`).  
- Run `Officialp1pr.py` to start detection. 
