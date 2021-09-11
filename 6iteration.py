# Iteration
# Iterate through all keys:-
states_capitals = {
  'Gujarat' : 'Gandhinagar',
  'Maharashtra' : 'Mumbai',
  'Rajasthan' : 'Jaipur',
  'Bihar' : 'Patna'
  }
for state in states_capitals:
      print(state)
 
# Output:- Gujarat Maharashtra Rajasthan Bihar

# Iterate through all values:-
# Example :-

states_capitals = {
    'Gujarat' : 'Gandhinagar',
    'Maharashtra' : 'Mumbai',
    'Rajasthan' : 'Jaipur',
    'Bihar' : 'Patna'
    }
    
for state in states_capitals:
    print(states_capitals[state])
 
# Output :-  Gandhinagar         Mumbai         Jaipur         Patna

# Example :-

details ={
    "name":  "Bijender",
    "age":  17,
    "class":  "10th"
    }
for x in details.values():
    print(x)
 
# Output: 

# 17 Bijender 10th 

# Example  :-

# dictionary se keys and values ek sath kaise print karte hai.

movie ={
    "name":  "Puli",
    "hero":  "Vijay",
    "rating":  7.5
    }
for x,y in movie.items():
    print(x,y)
 
# Output :-

('rating', 7.5) ('hero', 'Vijay') ('name', 'Puli') 

# Dictionary length
# Dictionary length hum dictionary mai kitne items hai yai count karne ke liye karte hai.

# Example:- 

meal ={
    "monday":  "Chole chawal",
    "sunday":  "Fried rice",
    "wednesday":  "dosa"
    }
print(len(meal))
 
# Output :- 3