def foo(lst):
    b=[]
    for a in lst:
        if a not in b:
            b.append(a)
        else:
            pass
    return b

lst=[1,2,34,5,6,6,6,78,8]
print (foo(lst))
   

