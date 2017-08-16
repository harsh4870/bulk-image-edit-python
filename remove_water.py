import glob
from PIL import Image, ImageFilter

lists = glob.glob('wallarmy\*.jpg')
for x in lists:
	print x
	im = Image.open(x)
	w, h = im.size
	im.crop((11, 0, w-12, h-23)).resize((w, h)).save( x+'.nologo.jpg', 'JPEG' )
	print x + ' >> Modified'
	pass

