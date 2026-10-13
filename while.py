print("我是一个求平均值的计算器")
total=0
count=0
user_input=input("请输入数字,当输入q时程序终止：")
while user_input !="q":
  num=float(user_input)
  total +=num
  count+=1
  user_input=input("请输入数字,当输入q时程序终止：")
  if count==0:
    result=0
  else:
       result=total/count
print("平均值为：",str(result))



