# Show Date and Time on Videos using OpenCV Python
import cv2
import datetime
cap=cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3,1280)
cap.set(4,720)
print(cap.get(3))
print(cap.get(4))


while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        text='Width :' + str(cap.get(3)) + ' Height :' + str(cap.get(4))
        date_obj=str(datetime.datetime.now())
        frame= cv2.putText(frame, date_obj, (10,50),font,1,(34,67,35),2,cv2.LINE_AA)
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('p'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()