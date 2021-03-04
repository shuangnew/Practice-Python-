num=input('Please enter a number')
dev=input('What number would you like to divide?')
if int(num)%int(dev)==0:
    print (num +' can be dividd by '+ dev)
elif int(num)%2 ==0:
    print(num + ' is an even number'
    +' and cannot be dividd by '+ dev)
else:
    print(num +' is an odd number'
    +' and cannot be dividd by '+ dev)