import cv2
import mediapipe as mp
import numpy as np


# Different mediapipe objects to show landmarks
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=False, min_detection_confidence=0.7)


cdict={'red':(0,0,255),
           'green':(0,255,0),
           'blue':(255,0,0),
           'yellow':(0,255,255),
           'magenta':(255,0,255),
           'cyan':(255,255,0),
           'black':(0,0,0)
           }   


canvas=np.empty((480,640,3),dtype='uint8')
canvas.fill(255)

cap=cv2.VideoCapture(0)

while True:
    color=input('Enter Color:\n')
    x1=0
    y1=0
    while True:
        canvas = cv2.circle(canvas, (x1,y1),6,(255,255,255),cv2.FILLED) 
        ret, frame = cap.read()
        frame=cv2.flip(frame,1)
        
        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, c = frame.shape
        
        results=hands.process(frame)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                break
            for id, lm in enumerate(hand_landmarks.landmark):
                if id == 8:
                    x2, y2 = int(lm.x * w), int(lm.y * h)
                    canvas = cv2.circle(canvas, (x2,y2),6,cdict[color],cv2.FILLED)
                    x1=x2
                    y1=y2

        cv2.imshow("Canvas", canvas)
                
        
        if cv2.waitKey(25) == ord('q'):
            break


    x1=0
    y1=0
    count=0

    while True:
        ret, frame=cap.read()
        frame=cv2.flip(frame,1)
        
        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, c = frame.shape
        results=hands.process(frame)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                break
            for id, lm in enumerate(hand_landmarks.landmark):
                if id == 8:
                    x2, y2 = int(lm.x * w), int(lm.y * h)                
                    canvas = cv2.circle(canvas, (x2,y2),6,cdict[color],cv2.FILLED) 
                    if(count==1 and (abs(x2-x1)>1 or abs(y2-y1)>1)):
                        cv2.line(canvas, (x1,y1), (x2,y2),cdict[color], 10)
                    x1=x2
                    y1=y2
                    count=1
    
        cv2.imshow("Canvas",canvas)
        
        if cv2.waitKey(25) == ord('c'):
            canvas.fill(255)
        if cv2.waitKey(25) == ord('q'):
            break
        
cap.release()
cv2.destroyAllWindows()