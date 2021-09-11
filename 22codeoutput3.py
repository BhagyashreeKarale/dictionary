# Niche diye gye code snippet ki output kya hoga?
fruit = {}

def addone(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1
        
addone('Apple')
addone('Banana')
addone('apple')
addone('Apple')

print (len(fruit))
print(fruit)



#output:
# fruit is a dictionary
# if the argument that we pass through function addone is ine of the keys that exist in the dictionary,
# then it will increase the value of the respective key by one
# else if the argument doesn't exist as a key in the dictionary it will assign value 1 to it 
# and add the key value pair to the dictionary.