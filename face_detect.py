import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True)

# Drawing utils
mp_drawing = mp.solutions.drawing_utils
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

# Function to calculate Euclidean distance
def euclidean(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

# Eye aspect ratio (EAR)
def calculate_ear(landmarks, eye_indices):
    left = euclidean(landmarks[eye_indices[1]], landmarks[eye_indices[5]])
    right = euclidean(landmarks[eye_indices[2]], landmarks[eye_indices[4]])
    top = (left + right) / 2
    bottom = euclidean(landmarks[eye_indices[0]], landmarks[eye_indices[3]])
    ear = top / bottom
    return ear

# Mouth aspect ratio (MAR)
def calculate_mar(landmarks, mouth_indices):
    top = euclidean(landmarks[mouth_indices[0]], landmarks[mouth_indices[1]])
    bottom = euclidean(landmarks[mouth_indices[2]], landmarks[mouth_indices[3]])
    mar = top / bottom
    return mar

# Eye and mouth landmark indices
LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]
MOUTH = [13, 14, 78, 308]

# EAR & MAR thresholds
EAR_THRESH = 0.21
MAR_THRESH = 0.5

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Draw face mesh
            mp_drawing.draw_landmarks(
                image=frame,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_CONTOURS,
                landmark_drawing_spec=drawing_spec,
                connection_drawing_spec=drawing_spec)

            landmarks = []
            for lm in face_landmarks.landmark:
                landmarks.append((int(lm.x * w), int(lm.y * h)))

            # Calculate EAR for both eyes
            left_ear = calculate_ear(landmarks, LEFT_EYE)
            right_ear = calculate_ear(landmarks, RIGHT_EYE)
            avg_ear = (left_ear + right_ear) / 2

            # Calculate MAR for mouth
            mar = calculate_mar(landmarks, MOUTH)

            # Blinking detection
            if avg_ear < EAR_THRESH:
                cv2.putText(frame, "Eyes are blinking", (30, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

            # Mouth open detection
            if mar > MAR_THRESH:
                cv2.putText(frame, "Mouth is open", (30, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    cv2.imshow('MediaPipe Face Mesh', frame)
    if cv2.waitKey(5) & 0xFF == ord('g'):
        break

cap.release()
cv2.destroyAllWindows()
