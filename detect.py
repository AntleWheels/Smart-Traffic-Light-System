import cv2
import imutils 
car_cascade = cv2.CascadeClassifier('cars.xml')# Loading the cascade
# initializing the camera
cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)
cam3 = cv2.VideoCapture(2)
cam4 = cv2.VideoCapture(3)
while True:
    #Read from the camera at North
    _,img =cam1.read() #reading the frame from the camera and storeas img
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Convert the image to grayscale
    img = imutils.resize(img,width=1000) #resize the image 
    cars = car_cascade.detectMultiScale(gray,1.1,1) #detecting the cars
    for (x,y,w,h) in cars: # we are iterating over the cars
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) #drawing a rectangle around the cars


    #Read from the camera at South
    _,img1 =cam2.read()
    gray1 =cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    img1 = imutils.resize(img1,width=1000)
    cars1 = car_cascade.detectMultiScale(gray1,1.1,1)
    for(x,y,w,h) in cars1:
        cv2.rectangle(img1,(x,y),(x+w,y+h),(0,0,255),2)

    #Read from the camera at East
    _,img2 =cam3.read()
    gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    img2 = imutils.resize(img2,width=1000)
    cars2 =car_cascade.detectMultiScale(gray2,1.1,1)
    for (x,y,w,h) in cars2:
        cv2.rectangle(img2,(x,y)(x+w,y+h),(0,0,255),2)

    #Read from the camera at West
    _,img3 =cam4.read()
    gray3 = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
    img3 = imutils.resize(img3,width=1000)
    cars3 = car_cascade.detectMultiScale(gray3,1.1,1)
    for (x,y,w,h) in cars3:
        cv2.rectangle(img3,(x,y),(x+w,y+h),(0,0,255),2)

    #Displaying the frames
    cv2.imshow("North",img)
    cv2.imshow("South",img1)
    cv2.imshow("East",img2)
    cv2.imshow("West",img3)
    
    #counting the cars
    b_north= str(len(cars)) 
    b_south= str(len(cars1))
    b_east= str(len(cars2))
    b_west= str(len(cars3))

    #converting the string to integer 
    north =int(b_north)
    south =int(b_south)
    east =int(b_east)
    west =int(b_west)
    print("_____________________________________________________")
    print("Total number of cars near the Junction :",(north+south+east+west))
    cars_count =[north,south,east,west]
    sorting =sorted(cars_count)
    print(f"Please give the 'Green' signal at {sorting[-1]} direction {"For 120 seconds" if sorting[-1] >=120 else "For 30 seconds"}")
    print(f"Please give the 'Yellow' signal at {sorting[-2]} direction")
    print(f"Please give the 'Red' signal at {sorting[-3]} direction")
    print(f"Please give the 'Red' signal at {sorting[-4]} direction")
    if cv2.waitKey(33) ==27:
        break
cam1.release()
cam2.release()
cam3.release()
cam4.release()
cv2.destroyAllWindows()
