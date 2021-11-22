import cv2

vidcap = cv2.VideoCapture("11.mp4")

count=0
while(vidcap.isOpened()):
    ret, image= vidcap.read()
    
    if not ret:
        break
    if(int(vidcap.get(1))%4==0):
        print("프레임숫자 : "+str(int(vidcap.get(1))))
        cv2.imwrite(f"./fram{count}.png",image)
        count +=1
    

vidcap.release()