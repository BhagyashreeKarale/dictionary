# Ek program likhiye jo ki dictionaries ki values ka sum print kare.
my_dict = {'data1':100,
        'data2': -54,
        'data3': 247} 
sum=0
for values in my_dict:
    sum=sum+my_dict[values]
print(sum)
#another method
my_dict = {'data1':100,
        'data2': -54,
        'data3': 247} 
sum=0
for values in my_dict.values():
    sum=sum+values
print(sum)