#!/usr/bin/env python3

import itertools as it
from PIL import Image
from pathlib import Path

#CONFIG#
canvas_size = (2000,2000)
image_dir = "images"
########

#
# make sure PIL (pillow) package is installed
# place all the images in image_dir formatted as [name].[posX].[posY].png
# example file: myname.400.234.png
# they will be applied in alphabetical order
#

def getCoords(filename):
	nameparts = filename.split(".")
	return (int(nameparts[1]),int(nameparts[2]))

base = Image.new("RGBA",canvas_size,(0,0,0,0))
files = Path(image_dir).glob('*')
for file in sorted(files):
	image = Image.open(file)
	base.paste(image,getCoords(file.name))
	print("pasting",file)

base.save("template.png","png")
