import cv2
from cvzone.HandTrackingModule import HandDetector
import keyboard
import time

# Initialize camera and hand detector
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.7, maxHands=2)
cap.set(2,400)
cap.set(3,200)

prev_action = None
last_press_time = time.time()

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)

        # Define gestures
        if fingers == [1, 1, 1, 1, 1]:  # All fingers up -> Accelerate
            action = "accelerate"
        elif fingers == [0, 0, 0, 0, 0]:  # Fist -> Brake
            action = "brake"
        else:
            action = "none"

        # Avoid repeating key presses
        if action != prev_action or (time.time() - last_press_time > 0.5):
            if action == "accelerate":
                keyboard.press('right')
                keyboard.release('left')
                print("Accelerating...")
            elif action == "brake":
                keyboard.press('left')
                keyboard.release('right')
                print("Braking...")
            else:
                keyboard.release('left')
                keyboard.release('right')
                print("Neutral...")

            prev_action = action
            last_press_time = time.time()

    else:
        # No hands detected — stop keys
        keyboard.release('left')
        keyboard.release('right')
        prev_action = "none"

    # Show webcam feed
    cv2.imshow("Hand Control", img)
    if cv2.waitKey(1) == ord('g'):
        break

cap.release()
cv2.destroyAllWindows()
