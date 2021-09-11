# Do lists lekar ek dictionary banaiye jisme pehli list ke elements keys ho aur dusri list ke elements 
# unn keys ki values ho.
# Example :-
# Input :-
# list1=["one","two","three","four","five"]
# Output :-
# {“one”:1,”two”:2,”three”:3,”four”:4,”five”:5}


# method1
list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,] 
data=dict(zip(list1,list2))
print(data)

# another method
list1=["one","two","three","four","five"]
list2=[1,2,3,4,5] 
listdic={}
for i in range(len(list1)):
    l=list1[i]
    for k in range(len(list2)):
        listdic[l]=list2[i]
        break#break is important here
print(listdic)

# another method
for i in range(len(list1)):
    key=list1[i]
    value=list2[i]
    listdic[key]=value
print(listdic)
