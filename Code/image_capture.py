import cv2
import time
start_time=time.time()
cam=cv2.VideoCapture(0)

cv2.namedWindow("Capture Image")
img_counter=1
while True:

    ret,frame=cam.read()
    # cv2.imshow("Capture Image",frame)
    if not ret:
        break
    # k=cv2.waitKey(1)
    # if k%256 ==27:
    #     print ("Escape pressed ..")
    #     break

    curr_time=int(time.time())
    time_elasped=curr_time-int(start_time)
    if(time_elasped==5):
        break

    img_name = "{}.png".format(img_counter)
    cv2.imwrite('images/'+img_name, frame)
    print("{} written!".format(img_name))
    img_counter += 1
    time.sleep(0.005)
cam.release()

cv2.destroyAllWindows()
