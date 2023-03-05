color = input()
a = input()
with open(a, "w") as myfile:
        for c in color:
                myfile.write("%s" % c)

content = open(a)
print(content.read())
