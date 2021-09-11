# Ek dictionary ki value ke sabhi items ko count kijiye jo ki ek list me hai.

# Input :-

dict =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
# Output :-

# total count:5


dict =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
count=0
for val1 in dict.values():
    if type(val1) == dict:#if the value is dictionary
        for val2 in val1.values():
            count=count+1
    elif type(val1) == list:#if the value is list.i.e in this case
        for i in val1:#if the value is single data
            count=count+1
    else:
        count=count+1
print(count,"values present in total")