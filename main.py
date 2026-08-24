from ultralytics import YOLO
import cv2 
import os
import time 
import easyocr

#Load YOLO model
base_model = YOLO("yolov8s.pt")
helmet_model = YOLO("helmet_best.pt")
plate_model =YOLO("number_plate_best.pt")

# For English langauge 
reader = easyocr.Reader(['en'])

#Traffic video
cap = cv2.VideoCapture("videos/traffic.mp4")
os.makedirs("Violations", exist_ok=True)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: 
        print("Error: video file is not detected")
        break

    #Detect vehicles
    base_results = base_model(frame,classes=[2,3])

    #Helmet detection
    helmet_results = helmet_model(frame,conf=0.5)

    #License plate Detection
    plate_results = plate_model(frame,conf=0.50)

    final_frame=frame.copy()

    if len(base_results) > 0:
        final_frame=base_results[0].plot(img=final_frame)
    if len(helmet_results) > 0:
        final_frame=helmet_results[0].plot(img=final_frame)

    #Number Plate detection and OCR Processing 
    if len(plate_results) > 0 and len(plate_results[0].boxes) > 0:
        for box in plate_results[0].boxes:

            #Find box possion for number plate
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])

            #Create box around number plate
            cv2.rectangle(final_frame, (x1, y1),(x2, y2), (0, 255, 0), 2)

            #Crop on number
            plate_crop = frame[y1:y2, x1:x2]

            if plate_crop.size > 0:
                #Reading number plate
                ocr_result = reader.readtext(plate_crop)
                label = f"Plate ({conf:.2f})"
                if len(ocr_result) > 0:
                    try:
                        #Output number plate text
                        plate_text = ocr_result[0][1]
                        label = f"{plate_text} ({conf:.2f})"
                    except Exception as e:
                        pass

                    #Display license plate number
            
                cv2.putText(final_frame, label, (x1, y1 -10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    #Show output
    cv2.imshow("ROADGUARDAI",final_frame)

    key=cv2.waitKey(1) & 0xFF

    if key == ord("s"):
        filename = f"Violations/violation_{int(time.time())}.jpg"
        cv2.imwrite(filename,final_frame)
        print("Evidence Saved:",filename)

    
    #Press Q to quit
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 
