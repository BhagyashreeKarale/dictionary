# Q-6. Niche diye gye code snippet ki output kya hogi?

my_dict = {}
my_dict[(1,2,4)] = 8
my_dict[(4,2,1)] = 10
my_dict[(1,2)] = 12

sum = 0
for k in my_dict:
    sum += my_dict[k]

print (sum)
print(my_dict)

#here the sum will be 30 as in loop we are calculating sum of value of each key in the dictionary
#we have 3 keys in the dictionary and their values as 8,10,12 respectively
#therefore the sum is 30
# and the dictionary is:my_dict={(1,2,4) = 8,(4,2,1) = 10,(1,2) = 12}