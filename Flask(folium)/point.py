import cv2

def onMouse(event, x, y, flags, param) :
    if event == cv2.EVENT_LBUTTONDOWN :
        print('point : ', x, y)
    elif event == cv2.EVENT_LBUTTONUP :
        print('point : ', x, y)
    elif event == cv2.EVENT_MOUSEMOVE:
        print('point2 : ', x, y)
        if flags & cv2.EVENT_FLAG_LBUTTON :
            cv2.circle(img, (x,y), 5, (0,0,255), -1)
            cv2.imshow('image', img)

img = cv2.imread('5flow.jpg')
cv2.imshow('image', img)
cv2.setMouseCallback('image', onMouse)
cv2.waitKey()