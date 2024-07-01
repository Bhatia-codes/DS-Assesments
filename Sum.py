def lily(n):
    sum=0
    for i in range(len(n)):
        sum=sum+n[i]
    return sum

x=[1,2,3,4,5]
print(lily(x))