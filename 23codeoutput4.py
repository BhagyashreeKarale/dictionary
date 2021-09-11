# Niche diye gye code snippet ki output kya hoga?
Student = {}
Age = {}
Details = {}
Student['name'] = "bikki"
Age['student_age'] = 14
Details['Student'] = Student#student={name:bikki}
Details['Age'] = Age#age={'student_age':24}

print (len(Details["Student"])) 


#here we have only one pair in Details["Student"] as it consists of dictionary student 
# which has one key value pair .i.e 'name':"bikki"