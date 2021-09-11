# Ek code likhiye jo dictionary ki 3 highest value print karaye.

# Input :-

my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20 }
# Output :-

# [58,56,100]


my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
val_list=[]
flist=[]
for values in my_dict.values():
    val_list.append(values)
for i in range(1,4):#its important to mention the starting point here.
    for k in range(len(val_list)-i):
        if val_list[k]>val_list[k+1]:
            temp=val_list[k]
            val_list[k]=val_list[k+1]
            val_list[k+1]=temp
    flist.append(val_list[k+1])
print(flist)
