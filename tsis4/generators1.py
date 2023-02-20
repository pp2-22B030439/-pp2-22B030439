def gensquares(N):
    for i in range(N):
        yield i**2

for x in gensquares(10):
    print(x)