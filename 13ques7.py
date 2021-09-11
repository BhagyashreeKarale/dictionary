# Ek list lijiye aur uske andar dictionaries me keys and values likhiye jaisa ki niche dikhaya gaya hai 
# (Sample Data) aur uske baad saare unique values ko ek list me print karaye.

# Example :-

# Input :-
data=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]
unilist=[]
for i in data:
    for values in i.values():
        if values not in unilist:
            unilist.append(values)
print(unilist)
