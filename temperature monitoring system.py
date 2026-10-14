def check_temperature(temp):
    if temp >=35:
        return "High"
    elif temp <=0:
        return "Low"
    else:
        return "Normal"

temp_list=[]
while True:
  temp = input("enter current temperature,( the code proceed expect entering q):")
  if temp=="q":
      break
  try:
      temp = float(temp)
      temp_list.append(temp)
  except ValueError:
         print("please enter a valid number!")
         continue

if len(temp_list)>0 :
     total=sum(temp_list)
     count=len(temp_list)
     result=total/count
     print("currently average temperature is :",result)
     print("Maximum temperature is :",max(temp_list))
     print("Minimum temperature is :",min(temp_list))
     print("The number of collections is :",len(temp_list))

     high_alarm=[]
     low_alarm=[]
     for tempi in temp_list:
       outcome=check_temperature(tempi)

       if outcome == "High":
        print(tempi, ": the temperature is already high!")
        high_alarm.append(tempi)
        print(f"there are {len(high_alarm)} high temperatures")

       elif outcome == "Normal":
        print(tempi, ": the temperature is normal")

       else:
        print(tempi, ": the temperature is already low!")
        low_alarm.append(tempi)
        print(f"there are {len(low_alarm)} low temperatures")

     count=len(low_alarm)+len(high_alarm)
     print(f"the total number of abnormal temperatures is {count}")

     file = open("temp.txt", "a+")
     file.write(f"\ntemp_list : {temp_list}\n"
         f"the maximum temperature is {max(temp_list)},\n"
                       f"the minimum temperature is {min(temp_list)},\n"
                       f"the average temperature is {result}")
     file.seek(0)

     content=file.read()
     print(content)
     file.close()

else:
  print("No temperature data entered")



