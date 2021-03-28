import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img=cv2.imread('image/sample3.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

height,width,_ = img.shape

boxes = pytesseract.image_to_boxes(img)

for b in boxes.splitlines():
    b = b.split(' ')
    x,y,w,h = int(b[1]),int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img,(x,height-y),(w,height-h),(0,0,200),3)
    cv2.putText(img,b[0],(x,height-y+40),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)

cv2.imshow('window',img)
cv2.waitKey(0)