def nnn(n):
    i=0
    while i<=n:
        if i%3==0 or i%4==0:
            yield i
        i+=1

n=int(input())
values=[]
for i in nnn(n):
    values.append(str(i))
print(values)