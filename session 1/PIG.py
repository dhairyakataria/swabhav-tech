from random import randint

total_score = 0
Turn = 0
while total_score<20:
  Turn += 1
  print('\nTURN ', Turn)
  score = 0
  while input('Role or Hold? (r/h)') != 'h': 
    dice = randint(1,6)
    print('Die ', dice)
    if dice == 1:
      print('Turn over.')
      score = 0
      break
    score += dice
  print('Score for turn = ', score)
  
  total_score += score
  if total_score>=20:
    print('You  Win!!!')
    print('You finished in ', Turn, 'turns!')
    break
