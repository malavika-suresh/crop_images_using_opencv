import cv2

#reading image
image = cv2.imread(r"img.jpg")

#converting to gray scale
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#applying canny edge detection
edged = cv2.Canny(image, 10, 250)


#finding contours
cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
idx = 0
for c in cnts:
	x,y,w,h = cv2.boundingRect(c)
	if w>50 and h>50:
		idx+=1
		new_img=image[y:y+h,x:x+w]
		#cropping images
		cv2.imwrite(r"cropped img\cropped"+str(idx) + '.png', new_img)
cv2.imwrite(r"cropped img\original.png", image)

print('Objects Cropped Successfully!')
