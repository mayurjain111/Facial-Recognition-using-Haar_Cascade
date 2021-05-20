import cv2
import os

cam = cv2.VideoCapture(0)
face_id = input('\n enter user id end press <return> ==>  ')

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "{}.jpg".format(img_counter+1)
        cv2.imwrite("dataset/User."+str(face_id)+'.'+ str(img_name),frame)
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
