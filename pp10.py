a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]
d=[]
for i in a:
    if i in b and i not in c:
        c.append(i)
print(c)

d=[i for i in a if i in b]
print(list(dict.fromkeys(d)))
