import random

ran_num = random.randint(0,100)

count = 0
while True:
  count += 1
  ur_choise = int(input('Your guess:- '))
  if(ur_choise == ran_num):
    print('Your guess ', ur_choise)
    print('You guessed it in ', count)
    break
  elif(ur_choise<ran_num):
    print("Too Low")
  else:
    print('Too high')