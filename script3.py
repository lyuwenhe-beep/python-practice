temp_list=[]
while True:
  try:
    temp = float(input("enter current temperature,( the code proceed expect entering 0):"))
  except ValueError:
         print("please enter number!")
         continue
  if temp==0:
      break
  temp_list.append(temp)
if len(temp_list)>0:
     total=sum(temp_list)
     count=len(temp_list)
     result=total/count
     print("currently average temperature is :",result)
     print("Maximum temperature is :",max(temp_list))
     print("Minimum temperature is :",min(temp_list))
     if result>=30:
        print("current temperature is already high!")
else:
  print("No temperature data entered")
file = open("temp.txt","w")
file.write(f"the maximum temperature is {max(temp_list)},\n"
              f"the minimum temperature is {min(temp_list)},\n"
                  f"the average temperature is {result}")
file.close()

file = open("temp.txt","r")
file_content=file.read()
print(file_content)