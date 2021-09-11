dict={"name":"Raju","marks":56}
ui=input("Enter any word:\n")
#method1
if ui in dict:
    print("Exist")
else:
    print("Doesn't exist")
#method2
if ui in dict.keys():
    print("Exists")
else:
    print("Doesn't exist")