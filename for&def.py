dic_gpa={"小明":3.81,"小李":3.24,"小云":3.3,"小刘":3.5}
for name,gpa in dic_gpa.items():
    print(f"{name}同学你好，你的绩点为:{gpa}")



def sphere_volume(radius):
    volumn=4/3*3.14*radius**3
    print(f"该球体体积为:{volumn}")
    return volumn
sphere_volume(3)
sphere_volume(5)
sphere_volume(2)