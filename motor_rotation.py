import sys
filename=sys.argv[1]
speed=float(input("Enter the speed in RPM:"))
time=float(input("Enter the time in minutes:"))

total_rotations = speed*time

with open(filename,"w") as f:
    f.write(f"Motor Speed: {speed} RPM\n")
    f.write(f"Motor Time: {time} minutes\n")
    f.write(f"Total Rotations: {total_rotations}")

with open(filename,"r") as g:
    content = g.read()
    print(content)