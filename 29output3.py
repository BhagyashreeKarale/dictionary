# Niche ek program hai jisme keys 1 se lekar 15 ke beech main hai aur values keys ka square hai jaise ki.

# Output kuch esha hona chahiye :-

# ab aapko is program ko theek karna hai.

c=dict()
for i in range(1,16):
    c=i*i
print(c) 

#errors:
# here c=dict() is incorrect method of taking an empty dictionary,
# we shall take empty dictionary c as c={}
# c = i*i will give us the number multiplied to itself
# but we want square
# so we will use exponent symbol and power will be 2 as we want square
# also instead of c we will take another variable as we have alrready taken empty dictionary named c
# therefore square=i**2
# we have to add this to the dictionary we are going to print at last
# for that we will code c[i]=square
# and at last printing the dictionary

c={}
for i in range(1,16):
    square=i**2
    c[i]=square
print(c) 