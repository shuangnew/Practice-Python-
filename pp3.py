a=[1,2,3,4,5,6,7,8,234,4576,234]
b=[]
c=input('Enter a number to compare:')
for i in a:
    if i<=int(c):
        b.append(i)
print ('Here are the numbers that smaller than'+ c)
print (b) 


print ('Here are the numbers that smaller than'+ c)
print ([i for i in a if i<=int(c)])