class student:
    def __init__(self,student_name,student_ID):
        self.name=student_name
        self.grades={"语文":0,"数学":0,"英语":0}
        self.ID=student_ID
    def set_grade(self,course,grade):
        self.grades[course]=grade
student1=student("小明","123456")
student1.set_grade("数学",100)
print(student1.name)
print(student1.grades)
