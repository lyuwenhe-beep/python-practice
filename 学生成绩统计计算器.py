scores_list=[]
while True:
     try:
         score = float(input("enter a score:"))
         if score ==0:
             break
         elif score < 60:
             print("fail!")
         elif score >=60:
             print("pass!")
         elif score >=90:
             print("excellent!")
     except ValueError:
         print("please enter a number")
         break
     scores_list.append(score)
print(scores_list)
pass_count=0
fail_count=0
for score in scores_list:
    if score >= 60:
        pass_count+=1
    else:
        fail_count+=1
print(f"there are {pass_count} pass")
print(f"there are {fail_count} fail")
average_score = sum(scores_list)/len(scores_list)
print(f"average score is {average_score}")