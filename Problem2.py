#Adam Pikielny
###Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

fiblist=[1,2]
for x in range(2,4000000):
    fiblist.append(fiblist[x-1]+fiblist[x-2])
sum=0
for x in fiblist:
    if x%2==0:
        sum+=x
print(sum)