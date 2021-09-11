# aapko ek dictionary di gai hai jisme aapko sare key ka sum karna hai.

# Apko iss code mai dedugging karni or pata karna hai ki aap output 14 kese la sakte ho.

dict1={1:2,2:3,3:4,4:5}
sum=0
for i in dict1.values():    
    sum=sum+1
print(sum)



#error:
#here we want sum of the values of the keys in the dictionary
#but the code add 1 for each count of values
#there are 4 values so each time by adding 4 we got 4
#but we want the sum of the values not the sum of the no. of values
#to det the sum of the values we have to replace 1 in sum=sum+i with i


#correct code:
dict1={1:2,2:3,3:4,4:5}
sum=0
for i in dict1.values():    
    sum=sum+i
print(sum)