import numpy as np
import os
import cv2

def main():

    cap = cv2.VideoCapture('test.avi')
    
    success, image = cap.read()
    
    if success:
        cv2.imwrite("ff.jpg", image)
    
    image = cv2.imread('ff.jpg', 0)
    success = 1

    N = 20
    R = 20
    hashMin = 2
    phi = 16

    samples = initializeBackgroud(image, N)
    
    height, width = firstFrame.shape

    for i in range (0, 20):
        s = "outputInitialBackground/" + str(i) + ".jpg"
        cv2.imwrite(s, samples[1 : width - 1, 1 : height - 1, i])
        
    while success: 
        success, frame = cap.read()
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        segMap, samples = vibe_detection(gray, samples, hashMin, N, R, phi)
        cv2.imshow('segMap', segMap)
        
        t = "op" + str(count) + ".jpg"
        t = "output/" + t;
        cv2.imwrite(t, segMap)
        
        count = count + 1;
        
        if cv2.waitKey(1) and 0xff == ord('q'):
            break
    
    cv2.destroyAllWindows()

def vibe_detection(frame, samples, hashMin, N, R, phi):
    
    height, width = frame.shape
    
    segMap = np.zeros((height, width)).astype(np.uint8)
    
    for i in range (height):
        for j in range (width):
            count, index, dist = 0, 0, 0
            
            while count < hashMin and index < N:
                dist = np.abs(frame[i, j] - samples[i, j, index])
                
                if dist < R:
                    count += 1
                index += 1
                
            if count >= hashMin:
                r = np.random.randint(0, phi - 1)
                
                if r == 0:
                    r = np.random.randint(0, phi - 1)
                    samples[i, j, r] = frame[i, j]
                r = np.random.randint(0, phi - 1)
                
                if r == 0:
                    x, y = 0, 0
                    while(x == 0 and y == 0):
                        x = np.random.randint(-1, 1)
                        y = np.random.randint(-1, 1)
                    r = np.random.randint(0, phi - 1)
                    
                    random_i = i + x
                    random_j = j + y
                    
                    samples[random_i, random_j, r] = frame[i, j]
            else:
                segMap[i, j] = 255
                
    return segMap, samples

def initializeBackgroud(firstFrame, N):
    
    paddedImage = np.pad(firstFrame, 1, 'symmetric')
    
    height, width = paddedImage.shape
    
    samples = np.zeros((height, width, N))
    
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            for k in range(N):
                x, y = 0, 0
                
                while(x == 0 and y == 0):
                    x = np.random.randint(-1, 1)
                    y = np.random.randint(-1, 1)
                
                random_i = i + x
                random_j = j + y
                
                samples[i, j, k] = paddedImage[random_i, random_j]
    
    samples = samples[1:height-1, 1:width-1]
    
    return samples

if __name__ == "__main__":
    main()
