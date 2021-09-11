# User se 10 students ke naam aur marks lekar unhe ek dictionary me store karaye.
name=[]
marks=[]
for counter in range (10):
    namei=input("Enter your name:\n")
    name.append(namei)
    marksi=int(input("Enter your marks:\n"))
    marks.append(marksi)
# students=dict(zip(name,marks))
# print(students)
#without using function
students={}
for i in range(len(name)):
    n=name[i]
    m=marks[i]
    students[n]=m
print(students)