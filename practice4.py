import sys
filename=sys.argv[1]


#.strip()去除空格符号 eg：在f.read().strip()

with open(filename,"a") as g:
    line1=input("enter the line")
    line2=input("enter the line")
    line3=input("enter the line")

    g.write(line1+"\n")
    g.write(line2+"\n")
    g.write(line3+"\n")
print("Three lines saved to",filename)