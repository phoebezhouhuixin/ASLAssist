import cv2

def main():
    count =7
    cap=cv2.VideoCapture(0)
    while True:
        if cap.isOpened():
            ret, frame = cap.read()
        else:
            ret = False

        cv2.imshow("1",frame)

        if cv2.waitKey(1) & 0xff ==ord("c"):
            img2 = frame
            cv2.imwrite("images/image_"+str(count)+".jpg",img2)
            count+=1
            cv2.imshow(str(count+1),img2)
        elif cv2.waitKey(1) & 0xff ==ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

main()
