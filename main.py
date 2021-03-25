#!/bin/python3
from random import randint

player= input('rock(r),paper(p),scissors(s)')

if player=='r':
  print('O','vs', end = ' ')
  
elif player=='p':
   print('---','vs', end = ' ')

else:
  print('>8','vs', end = ' ')

  
chosen= randint(1,3)


if chosen == 1:
  computer = "r"
  print('O')
  
elif chosen == 2:
  computer= 'p'
  print('---')
else:
  computer='s'
  print('>8')
  



if player==computer:
  print('draw')
  
elif player=='r' and computer=='s':
  print('Player wins')

elif player=='p' and computer =='r':
  print('Player wins')

elif player=='s' and computer=='p':
  print('Player wins')
  
else:
  print('Computer wins')
 
