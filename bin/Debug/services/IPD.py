import cv2

def main():
    faces=cv2.CascadeClassifier("services\\face.xml")

    eyes=cv2.CascadeClassifier("services\\eye.xml")

    capture=cv2.VideoCapture(0)
    is_al = False

    while True:
        ret,frame=capture.read()

        gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        face=faces.detectMultiScale(gray_frame,1.3,5)

        for (x,y,w,h) in face:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), thickness=4)

            gray_face=gray_frame[y:y+h,x:x+w]

            color_face=frame[y:y+h, x:x+w]
            eye=eyes.detectMultiScale(gray_face, 1.5, 5)
            for (a,b,c,d) in eye:
                cv2.rectangle(color_face, (a,b), (a+c, b+d), (0,255,0), thickness=4)
            dis = 0
            if len(eye) >= 2:
                eye1_x, eye1_y, eye1_w, eye1_h = eye[0]
                eye2_x, eye2_y, eye2_w, eye2_h = eye[1]
                dis = abs(eye2_x + eye2_w // 2 - (eye1_x + eye1_w // 2))
            if dis > 20:
                is_al = True
                f = open("services\\ipd.txt", "w")
                f.write(str(dis))
                f.close()
                print("значение записано в ipd.txt")
                exit()


        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) == 13 and not is_al:
            break

    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()