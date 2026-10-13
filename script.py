temp_list=[]
while True:
    try:
        temp = input("enter temperature")
    except ValueError:
        print("please enter temperature")
        continue
    if temp =="0":
        break
    temp_list.append(float(temp))

def temp_caculate(temp_list):
    if len(temp_list)==0:
        print("please enter temperature")
        return None
    total=sum(temp_list)
    count=len(temp_list)
    average_temp=total/count
    return average_temp
print(temp_caculate(temp_list))