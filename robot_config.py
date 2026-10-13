import sys
filename=sys.argv[1]


with open(filename,"r") as f:
    content=f.read()

print(content)