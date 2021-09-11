# "MISSISSIPPI" iss word me har letter ki occurrency count karke ek dictionary me store karaye. 
# Jisme letter dictionary ki keys aur occurrency Uss dictionary ki values hongi.
data="MISSISSIPPI"
data=list(data)
unilist=[]
fdic={}
for i in data:
    if i not in unilist:
        unilist.append(i)
        count=0
        for k in range(len(data)):
            if data[k]==i:
                count=count+1
        fdic[i]=count
print(fdic)
# we can do this by creating two list of i and count each and then using zip function too.