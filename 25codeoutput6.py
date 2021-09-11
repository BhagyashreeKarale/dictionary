# Niche diye gye code snippet ki output kya hoga?

box = {}
jars = {}
crates = {}
box['biscuit'] = 1
box['cake'] = 3
jars['jam'] = 4
crates['box'] = box
crates['jars'] = jars
print (len(crates[box]))#we're trying to use a dict as a key to another dict. That does not work because the keys have to be hashable. As a general rule, only immutable objects (strings, integers, floats, frozensets, tuples of immutables) are hashable (though exceptions are possible). So this does not work:(




#output:
#this will throw an TypeError which says unhashable type: 'dict'
#Let us first understand what is hashable and unhasable. 
# In simple terms, we term the items whose values cannot be changed as hashable 
# and the objects whose values can be changed as unhashable.
# For example in Python, all immutable objects can be termed as hashable 
# while as mutable objects can be termed as unhashable. 
# Let us take an example where we can get such error and why we get it.
# For example when you use a list as a key in the dictionary 
# It cannot be done and we will get an error ’TypeError: unhashable type’.
# This is because lists can't be hashed and we are trying to use a list as an hash argument. 
# This means that when you try to hash an unhashable object it will result in this error. 
# The standard way to solve this issue is to cast a list to a tuple.
# And as tuples are immutable and thus hashable, it can work .