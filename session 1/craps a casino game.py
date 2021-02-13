from random import randint

point = 0
while True:
  total_sum = randint(1,6) + randint(1,6)
  if ((total_sum == 7) or (total_sum == 11)) and  point==0:
    print('You Win ')
    break
  elif ((total_sum == 2) or (total_sum == 3) or (total_sum == 12)) and point==0:
    print('craps')
    break
  elif point==0:
    point = total_sum
  elif point == total_sum:
    print('You Win ')
    break
  elif total_sum==7:
    print('craps')
    break
  else:
    continue