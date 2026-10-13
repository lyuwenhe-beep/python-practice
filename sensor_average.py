import sys
filename = sys.argv[1]

reading1 = float(input("Enter the reading 1: "))
reading2 = float(input("Enter the reading 2: "))
reading3 = float(input("Enter the reading 3: "))

total = reading1 + reading2 + reading3
average = total/3

with open(filename,"w") as f:
    f.write(f"Reading 1: {average}\n")
    f.write(f"Reading 2: {average}\n")
    f.write(f"Reading 3: {average}\n")
    f.write(f"total reading: {total}\n")
    f.write(f"Average reading: {average}\n")

with open(filename,"r") as g:
    content = g.read()
    print(content)

