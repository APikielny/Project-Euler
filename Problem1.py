#Adam Pikielny
newlist=[]
for x in range(0,1000):
    if x%5==0 and x%3==0:
        newlist.append(x)
    elif x%5==0:
        newlist.append(x)
    elif x%3==0:
        newlist.append(x)
print(sum(newlist))
