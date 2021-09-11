# aapko ek dictionary di gai hai jisme aapko kuch key ki value print karani hai.

# Code ko debug karre do bug find karro.

# details={
#     "name":"Shanti",
#     "age":12,
#     "email":"shanti@navgurukul.org",
#     }

# print(details["name"])
# print(details["lastname"])
# print(details[age])#here quotation is missing 



#errors:
# in print(details["lastname"]), "lastname" key is a key that doesn't exist in the dictionary
# in print(details[age]), quotation is missing

#correct code:
details={
    "name":"Shanti",
    "age":12,
    "email":"shanti@navgurukul.org",
    }

print(details["name"])
print(details["age"])