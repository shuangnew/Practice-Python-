def foo(a):
    b=a.split()
    return b[::-1]

a=input('please ennter your sentance here:')
c=foo(a)
print(c)