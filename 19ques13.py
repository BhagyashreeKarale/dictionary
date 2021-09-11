# Ek program likho jo ki dictionaries ki values ko sort(ascending or descending) kar de.

# Input :-

{'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# Expected result in Ascending Order:

{'param':20,'anjili':30,'bijender':45,'roshini':50,'deepak':60}
# Expected result in Descending Order:

{'deepak':60,'roshini':50,'bijender':45,'anjili':30,'param':20}




data={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
vallist=[]
for i in data.values():
    vallist.append(i)
for i in range(len(vallist)):
    for j in range (len(vallist)-i-1):
        if vallist[j]>vallist[j+1]:#for descending order just change the sign from > to < 
            temp=vallist[j]
            vallist[j]=vallist[j+1]
            vallist[j+1]=temp#now vallist is ascending order of values

ndic={}#we'll create a new list here
for v in vallist:
    for s in data.keys():
        if data[s]==v:
            ndic[s]=v
print(ndic)

