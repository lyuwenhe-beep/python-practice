import sys
filename = sys.argv[1]

robot_name=float(input("enter robot name: "))
starting_bp=float(input("enter starting battery percentage: "))
battery_up=float(input("enter battery used percentage: "))

remaining_battery = starting_bp - battery_up

with open(filename,"w") as f:
    f.write(f"Robot name: {robot_name}\n")
    f.write(f"Starting battery percentage: {starting_bp}\n")
    f.write(f"Battery used percentage: {battery_up}\n")
    f.write(f"Remaining battery percentage: {remaining_battery}\n")
with open(filename,"r") as g:
    content = g.read()
    print(content)