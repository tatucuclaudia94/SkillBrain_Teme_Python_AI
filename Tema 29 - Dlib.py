import cv2
import csv
import datetime


# incarcare model detectie fata

face_cascade = cv2.CascadeClassifier(
cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


# pornire camera

cap = cv2.VideoCapture(0)


# fisier CSV pentru landmarks

landmark_file = open("landmarks.csv","w",newline="")
landmark_writer = csv.writer(landmark_file)

landmark_writer.writerow(["x","y","w","h"])


# fisier CSV pentru prezenta

attendance_file = open("prezenta.csv","w",newline="")
attendance_writer = csv.writer(attendance_file)

attendance_writer.writerow(["nume","data","ora"])


while True:

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.3,5)


    for (x,y,w,h) in faces:

        # desenare fata

        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        # salvare coordonate fata

        landmark_writer.writerow([x,y,w,h])

        # salvare prezenta

        now = datetime.datetime.now()

        attendance_writer.writerow(
        ["Claudia", now.date(), now.time()]
        )

        # mesaj sistem pornit

        cv2.putText(
        frame,
        "Face detected - Access granted",
        (30,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
        )


    cv2.imshow("Face System", frame)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()

landmark_file.close()

attendance_file.close()

cv2.destroyAllWindows()

