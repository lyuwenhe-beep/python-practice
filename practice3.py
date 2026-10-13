import sys
script,width,height,depth = sys.argv
width = int(width)
height = int(height)
depth = int(depth)

Volume= width*height*depth
print("the volume is :",Volume)