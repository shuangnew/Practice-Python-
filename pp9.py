import random
a=random.randint(0,9)
guess=0
count=0

while guess !=a and guess !='exit':
    guess=int(input('Please enter you guess:'))
    if guess==a:
         print('You got it!')
         print('You took only ' + str(count) +' tries')
    elif guess<a: 
        print('Your guess is a bit low')
        count=count+1
    else:
         print('Your guess is a bit high')
         count=count+1
    if guess=='exit':
        break
