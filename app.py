import cv2
image = cv2.imread('bibi.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier('haarcascade_fron_face.xml')
try:
    if face_cascade.empty():
        raise IOError('Error: Failed to load cascade classifier')
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Faces', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except IOError as e:
    print(str(e))

except Exception as e:
    print(str(e))
