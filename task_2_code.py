import cv2

  
# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('WhatsApp Video 2023-03-24 at 01.54.21.mp4')
  
# Check if camera opened successfully
if (cap.isOpened()== False):
    print("Error opening video file")
i=0
# Read until video is completed
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        
        if i%4==0:
            cv2.imshow('Frame', frame)
            cv2.waitKey(1)
    
        else:
            cv2.waitKey(1)
            pass
    if 0xFF == ord('q'):
        break
    i=i+1
cap.release()
# Press Q on keyboard to exit


