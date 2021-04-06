import matplotlib.pyplot as plt
import numpy as np



img = skimage.io.imread('tiger.png', as_gray=True)

h=img.shape[0]
w=img.shape[1]
 
matrix=np.ones((h,w))*100
img1 = img+matrix
for i in range (0,w):
    for j in range(0,h):
        if img1[j][i] > 255:
            img1[j][i]=255

h,w=img.shape
img90=np.zeros((w,h))
imgr=np.zeros((h,w))


for j in range(0,h):
    img90[:,h-j-1]=img[j,:]

for j in range(0,w):
    imgr[:,j]=img1[:,w-j-1]

imgcut=img1[::10,::10]





plt.figure(1)
plt.imshow(imgcut, cmap='gray', vmin=0, vmax=255)

plt.show()
#:j
#[:,1] stupac
#[1,:] redak