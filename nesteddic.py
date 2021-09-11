a=[1,4,5,65,3,6,46,45,]
b={}
for i in a[::-1]:
    b={i:b}
print(b)