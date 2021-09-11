# Question 1
# Ek program likhiye jisse ki niche di hui dictionaries ek hi dictionary me aa jaaye jaise ki niche 
# Expected result me diya gaya hain or jisski bhi keys same hai unki values add ho jai.
# Example :-

# Input :-

dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic4={}
# Output :-

# {1: 10, 2: 60, 3: 30,  5: 50, 6: 60}

dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic4={}
#method1
dic1.update((dic2.update(dic3)))
dic2.update(dic3)
print(dic2)
#method2
dicts = {}
dicts.update(dic1)
dicts.update(dic2)
dicts.update(dic3) 
print(dicts)
#method3 (using for loop)
for i in (dic1,dic2,dic3):
    dic4.update(i)
print(dic4)

