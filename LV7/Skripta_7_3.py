import cv2
import numpy as np
from sklearn.externals import joblib
from sklearn.neural_network import MLPClassifier


# display
cv2.namedWindow("frame", cv2.WINDOW_NORMAL)   
cv2.namedWindow("edges", cv2.WINDOW_NORMAL)
font = cv2.FONT_HERSHEY_SIMPLEX

# TODO: ucitaj mrezu s diska


# algorithm params
pad = 15
size_th = 32
mnist_size = 28

# video processing
cp = cv2.VideoCapture(0)
kernel1 = np.ones((7,7), np.uint8)
kernel2 = np.ones((5,5), np.uint8)

# some vars
label = "unkown"

while True:
    
    ret, frame = cp.read(0)

    # frame preprocessing - getting edges
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
    v = np.median(gray_img)
    lower = int(max(0, (1.0 - 0.33) * v))
    upper = int(min(255, (1.0 + 0.33) * v))
    edge_img = cv2.Canny(gray_img, lower, upper)
    img_preprocessed = cv2.dilate(edge_img, kernel1, iterations=1)
    img_preprocessed = cv2.erode(img_preprocessed, kernel2, iterations=1)

    # get countours and bounding boxes (rects)
    _, contours, _ = cv2.findContours(img_preprocessed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    rects = [cv2.boundingRect(contour) for contour in contours]
    rects = [rect for rect in rects if rect[2] >= 3 and rect[3] >= 8]


    # loop over all rectangles (detections) and classify them
    for rect in rects:
        
        x, y, w, h = rect

        #crop rectangle from image        
        cropped_digit = img_preprocessed[y-pad:y+h+pad, x-pad:x+w+pad]
        cropped_digit = cropped_digit/255.0

        #filter small rectangles:
        if cropped_digit.shape[0] >= size_th and cropped_digit.shape[1] >= size_th:
            cropped_digit = cv2.resize(cropped_digit, (mnist_size, mnist_size))
        else:
            continue
        
        # start TODO: klasificiraj sliku (cropped_digit) s konvolucijskom neuronskom mrezom i zapisi predikciju u varijablu label (as string)


        # end of TODO

        # show rectangle and label on frame
        cv2.rectangle(frame, (x - pad, y - pad), (x + pad + w, y + pad + h), color = (255, 255, 0))

        cv2.putText(frame, label, (rect[0], rect[1]), font,
            fontScale = 0.5,
            color = (255, 0, 0),
            thickness =  1,
            lineType =  cv2.LINE_AA)


    # show results
    cv2.imshow("frame", frame)
    cv2.imshow("edges", img_preprocessed)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


