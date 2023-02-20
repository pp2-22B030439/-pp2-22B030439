def reverssss(n):
    i=0
    while i<=n:
        yield i
        i+=1

n=int(input())
values=[]
for i in reverssss(n):
    values.append(str(i))
print(values[::-1])



