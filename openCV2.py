import cv2

# Capture live stream from your default camera
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while(True):
    ret,frame=cap.read()
    if(ret==True):
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)
    # Convert frame to grey

        grey= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame_window',grey)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()