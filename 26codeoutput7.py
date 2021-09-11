# Niche diye gye code snippet ki output kya hogi?

rec = {
"Name" : "Python", 
"Age":"20",
"Addr" : "NJ", 
"Country" :"USA"
}
id1 = id(rec)
# Python id() function returns an identity of an object. 
# This is an integer which is guaranteed to be unique. 
# This function takes an argument an object and returns a unique integer number which represents identity. 
del rec#this deletes the dictionary rec

rec = {
    "Name" : "Python", 
    "Age":"20", 
    "Addr" : "NJ", 
    "Country" : "USA"
    }#this is the new rec
# now for id1 also rec is the new rec as rec and rec is same word
id2 = id(rec)#id2 is also the is of thw new rec
print(id1 == id2)#this will return an boolean#as id1 and id2 are same therefore it will return true