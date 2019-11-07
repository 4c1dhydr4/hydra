from datetime import datetime

def crop_center(img,cropx,cropy):
	y,x, z = img.shape
	startx = x//2-(cropx//2)
	starty = y//2-(cropy//2)    
	return img[starty:starty+cropy,startx:startx+cropx]

def timestamp():
	now = datetime.now()
	return '{}/{}/{} {}:{}'.format(now.day, now.month, now.year, now.hour, now.minute)