# Niche diye gye code snippet ki output kya hogi?

a = {'a':1,'b':2,'c':3}

print (a['a','b'])
# Options :- 
# A. Key Error

# B. [1,2]

# C. {‘a’:1,’b’:2}

# D. (1,2)

#output:
# not it will throw an key error as we are tring to access values of two keys 
# at a time in a way which isn't allowed.
# we can access value of only one key using the syntax dictionaryname[keyname]