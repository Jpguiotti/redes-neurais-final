import cv2
# importando mediapipe
import mediapipe as mp

#capturar a camêra 
cap = cv2.VideoCapture(1)

#desenhar os pontos

mp_drawing = mp.solutions.drawing_utils

# coletar solucao do face mesh 

mp_face_mesh = mp.solutions.face_mesh


# enquanto a camera estiver aberta 
with mp_face_mesh.FaceMesh(min_detection_confidence=0.5,min_tracking_confidence=0.5)
while cap.isOpened():
    # sucesso é booleana-0 e 1 
    sucesso,frame = cap.read()
    if not sucesso:
        print('ignorando o fram vazio da camera')
        continue
    cv2.imshow('Camera',frame)
    
    if cv2.waitKey(10) & 0xFF == ord('c'):
        break
#fecha a captura
cap.release()
cv2.destroyAllWindows()    