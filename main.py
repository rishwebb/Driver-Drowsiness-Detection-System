import cv2
import dlib
import imutils
from scipy.spatial import distance as dist
from imutils import face_utils
import pygame
import time

# Initialize Pygame mixer
pygame.mixer.init()
alert_sound = pygame.mixer.Sound("assets/alert.mp3")
wakeup_sound = pygame.mixer.Sound("assets/wake_up.mp3")

# Set volume
alert_sound.set_volume(1.0)
wakeup_sound.set_volume(1.0)

def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

# Constants
EAR_THRESHOLD = 0.25  # Restored to original sensitivity
EAR_CONSEC_FRAMES = 15 
COUNTER = 0

# Audio State Management
AUDIO_STATE = 0  # 0: Idle, 1: Playing Alert, 2: Pause, 3: Playing Wakeup, 4: Loop Alert
pause_start_time = 0

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret: break
    
    frame = cv2.flip(frame, 1)
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Optimized detection for Linux (up-sample 0 for speed)
    rects = detector(gray, 0)

    # Detection Logic
    eyes_closed = False
    if len(rects) > 0:
        for rect in rects:
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)
            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            ear = (eye_aspect_ratio(leftEye) + eye_aspect_ratio(rightEye)) / 2.0
            
            if ear < EAR_THRESHOLD:
                eyes_closed = True
    else:
        # If face is lost while previously closed, keep counting
        if COUNTER > 0:
            eyes_closed = True

    if eyes_closed:
        COUNTER += 1
        if COUNTER >= EAR_CONSEC_FRAMES:
            cv2.putText(frame, "!!! DROWSINESS DETECTED !!!", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            
            # --- Sequential Audio State Machine ---
            if AUDIO_STATE == 0: # Start with Alert
                alert_sound.play()
                AUDIO_STATE = 1
            
            elif AUDIO_STATE == 1: # Wait for Alert to finish
                if not pygame.mixer.get_busy():
                    pause_start_time = time.time()
                    AUDIO_STATE = 2
            
            elif AUDIO_STATE == 2: # 1 Second Pause
                if time.time() - pause_start_time >= 1.0:
                    wakeup_sound.play()
                    AUDIO_STATE = 3
            
            elif AUDIO_STATE == 3: # Wait for Wakeup to finish
                if not pygame.mixer.get_busy():
                    AUDIO_STATE = 4
            
            elif AUDIO_STATE == 4: # Loop Alert until eyes open
                if not pygame.mixer.get_busy():
                    alert_sound.play()
    else:
        # Reset everything if eyes open
        if COUNTER > 0:
            pygame.mixer.stop()
        COUNTER = 0
        AUDIO_STATE = 0

    cv2.imshow("Drowsiness Guard", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()