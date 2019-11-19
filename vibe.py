
import numpy as np
import os
import cv2

def initializeBackgroud(firstFrame, N):
           
    paddedImage = np.pad(firstFrame, 1, 'symmetric')
    
    height = paddedImage.shape[0]
    width = paddedImage.shape[1]
    
    samples = np.zeros((height,width,N))
    
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
                
    samples = samples[1 : height - 1, 1 : width - 1]
    
    return samples
    
vid = cv2.VideoCapture('test.avi')

success, firstFrame = vid.read()

if success:
    cv2.imwrite("ff.jpg", firstFrame)

firstFrame = cv2.imread('ff.jpg', 0)
success = 1

N = 20
R = 20
hashMin = 2
phi = 16

samples = initializeBackgroud(firstFrame, N)

height = firstFrame.shape[0]
width = firstFrame.shape[1]

for i in range (0, 20):
    s = "/home/yashk2000/imgProc/vibe/output/" + str(i) + ".jpg"
    cv2.imwrite(s, samples[1 : width - 1, 1 : height - 1, i])
    cv2.imshow("image", samples[1 : width - 1, 1 : height - 1, i])
    cv2.waitKey(0)
    
cv2.destroyAllWindows()
