def caculate_BMI(height,weight):
    BMI=weight/(height**2)
    if BMI<=18.5:
        print("您的BMI分类为:偏瘦")
    elif 18.5<=BMI<=25:
        print("您的BMI分类为:正常")
    elif 25<=BMI<=30:
        print("您的BMI分类为:偏胖")
    else:
        print("您的BMI分类为:肥胖")
    return BMI
result=caculate_BMI(1.8,100)
print(result)
