def nnn(n):
    i=0
    for i in range(n):
        v= i**2
        yield v
    i+=1

n=int(input())
values=[]
for i in nnn(n):
    values.append(str(i))
print(values)