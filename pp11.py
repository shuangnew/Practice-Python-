test=int(input('Please enter your number'))

b=test-1
a=list(range(2,b))
c=[]
for number in a:
      if test % number==0:
          c.append(a)
      else:
          pass

if len(c)>0:
    print('This is not a prime number')
else: 
    print('This is a prime number')
    


     