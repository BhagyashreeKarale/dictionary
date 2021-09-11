# Ek program likhiye jo ki nested dictionary me se first key or value ko remove kare.
# Input :-

Dic= {1: 'NAVGURUKUL',2: 'IN',  3:{    'A' : 'WELCOME','B' : 'To','C' : 'DHARAMSALA'}}
# Output :-
# Dic= {1: 'NAVGURUKUL',2: 'IN',  3:{ 'B' : 'To','C' : 'DHARAMSALA'}}


Dic= {1: 'NAVGURUKUL',2: 'IN',  3:{    'A' : 'WELCOME','B' : 'To','C' : 'DHARAMSALA'}}
for key1 in Dic.keys():
    if type(Dic[key1])==dict:#dont forget type
        for key2 in Dic[key1].keys():#this is similar to list
            del Dic[key1][key2]
            break
print(Dic)
