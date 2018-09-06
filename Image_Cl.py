# Color IMG Generator
# Released under MIT license
#
# bytebitter [at] gmail [dot] com

from PIL import Image
from PIL import ImageDraw

class COLOR(object):
	def __init__(self, name):
		self.name = name
		self.hex = "#000000"
		self.sz = 100

	def set_hex(self, hex):
		self.hex = hex

	def get_img_off(self, bdr):
		print(self.name)
		bd = int(bdr)
		img = Image.new("RGB", (self.sz, self.sz), "black")
		draw = ImageDraw.Draw(img)
		for i in range(0, bd, 1):
			draw.rectangle([(0+i,0+i),(self.sz-i,self.sz-i)], fill=None, outline=self.hex)
		return(img)
	
	def get_img_on(self):
		img = Image.new("RGB", (self.sz,self.sz), color=self.hex) 
		return(img)

