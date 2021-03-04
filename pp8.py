while True:
     ply1=input('Player one enter your choice:')
     ply2=input('Player two enter your choice:')
     lst=['rock','paper', ' sissors']
     if list.index(ply1)==list.index(ply2):
         print('Its a draw')
     elif ply1=='rock' and ply2=='paper':
         print('player one is the winner')
     elif ply1=='rock' and ply2=='sissors':
         print('player two is the winner')
     elif ply1=='paper' and ply2=='sissors':
         print('player one is the winner')
     elif ply1=='paper'and ply2=='rock':
         print('player two is the winner')
     elif ply1=='sissors'and ply2=='paper':
         print('player two is the winner')
     else ply1=='sissors' and ply2=='rock':
         print('player one is the winner')
    Quit=input('Would you like to play again? or type quit to quit')
    if Quit==quit
       break
    else:
        pass

