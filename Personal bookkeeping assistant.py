def caculate_expense(expense):
    if len(expense)==0:
        return 0

    total=sum(expense)
    count=len(expense)
    average=total/count
    maximum=max(expense)
    minimum=min(expense)

    return average,maximum,minimum,total,count
expense_list=[]
while True:
    try:
        money=int(input("enter expense"))
    except ValueError:
           print("please enter number")
           continue
    if money == 0:
       break
    expense_list.append(money)

result=caculate_expense(expense_list)
if result is None:
    print("please enter number")
else:
    average, maximum, minimum, total, count=result
    print("the average expense is",average)
    print("the maximum expense is",maximum)
    print("the minimum expense is",minimum)
    print("the total expense is",total)
    print("the count is",count)
