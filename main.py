import tkinter
import face_recognition
import cv2
import time

def add():
    if (e1.get() == "koushal" and e2.get() == "emma2003"):
        r2 = tkinter.Tk()
        r2.title("login page")
        r2.geometry('400x200')
        tkinter.Label(r2, text="welcome koushal").grid(row=0)
        r2.mainloop()
    else:
        r3 = tkinter.Tk()
        r3.title("Error")
        r3.geometry('400x200')
        tkinter.Label(r3, text="something went wrong").grid(row=0)
        r3.mainloop()

def openwebcam():
    img1 = face_recognition.load_image_file('me4.jpeg')
    me1 = cv2.resize(img1, (0, 0), None, 0.1, 0.1)
    me1 = cv2.cvtColor(me1, cv2.COLOR_BGR2RGB)
    encode1 = face_recognition.face_encodings(me1)[0]

    cap = cv2.VideoCapture(0)
    while True:
        isTrue, frameS = cap.read()
        frameS = cv2.cvtColor(frameS, cv2.COLOR_BGR2RGB)
        frameEncode = face_recognition.face_encodings(frameS)[0]
        results = face_recognition.compare_faces([encode1], frameEncode)
        if (results[0]):
            r4 = tkinter.Tk()
            r4.title("Login page")
            r4.geometry('400x200')
            tkinter.Label(r4, text="welcome koushal").grid(row=0)
            r4.mainloop()
            break
        else:
            r5 = tkinter.Tk()
            r5.title("Error")
            tkinter.Label(r5, text="somethinh went wrong")
            r5.geometry('400x200')
            r5.mainloop()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


r = tkinter.Tk()
r.title("main window")
r.geometry('400x200')
but = tkinter.Label(r, text="Username: ").grid(row=0)
pas = tkinter.Label(r,text="password").grid(row=1)
e1 = tkinter.Entry(r)
e2 = tkinter.Entry(r)
e1.grid(row=0,column=2)
e2.grid(row=1,column=2)
sub = tkinter.Button(r,text="login", width=25, command=add)
sub.grid(row=2, column=3)
webcam = tkinter.Button(r, text="Or use web cam" ,width=30, command=openwebcam)
webcam.grid(row=3, column=3)

r.mainloop()
