#Mohit Tamang 1001552822
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
from scipy import ndimage

#processes the given image through a lowpass & a highpass filter
def image_processing(image_filename):
    img = mpimg.imread(image_filename) #reads image into img array
    #original image
    plt.imshow(img,cmap='gray')
    plt.title("original image of %s"% (image_filename,))
    plt.show()

    #LOW_PASS_FILTER
    lowpass_filter = np.full(10,0.1) # lowpass filter of 10 point moving average
    mylist = []

    #passing the image through low-pass filter 
    for row in img:
        y = np.convolve(row,lowpass_filter)#applying filter to each row of original image
        mylist.append(y)
  
    plt.imshow(mylist,cmap='gray')
    plt.title("blurred image of %s"% (image_filename,))
    plt.show()

    #HIGH_PASS_FILTER
    highpass_filter = np.array([1,-1]) # highpass filter 
    new_list = []
    #passing the image through highpass filter 
    for row in img:
        x = np.convolve(row,highpass_filter)#applying filter to each row of original image
        new_list.append(x)

    plt.imshow(new_list,cmap='gray')
    plt.title("edge detected image of %s"% (image_filename,))
    plt.show()  
 
image_processing('boat.512.tiff')
image_processing('clock-5.1.12.tiff')
image_processing('man-5.3.01.tiff')
image_processing('tank-7.1.07.tiff')


#Removing noises from darinGrayNoise.jpg
noisyimage = mpimg.imread('darinGrayNoise.jpg')
plt.imshow(noisyimage,cmap='gray')
plt.title('Noisy image of professor Brezeale')
plt.show()
lowpass_filter = np.full(10,0.1) # lowpass filter of 10 point moving average
highpass_filter = np.array([1,-1]) # highpass filter 
new_img_data = []



#applying scipy's ndimage.median_filter on the noisyimage
new_image = ndimage.median_filter(noisyimage,5)
plt.imshow(new_image,cmap='gray')
plt.title('Professor Brezeale after applying median filter')
plt.show()

#applying high-pass filter on the original image
for row in new_image:
    z = np.convolve(row,highpass_filter)
    new_img_data.append(z)
    
plt.imshow(new_img_data,cmap='gray')
plt.title('Professor Brezeale after applying highpass filter')
plt.show()

#applying scipy's ndimage.median_filter on the noisyimage
new_image = ndimage.median_filter(new_img_data,5)
plt.imshow(new_image,cmap='gray')
plt.title('Professor Brezeale after applying median filter')
plt.show()