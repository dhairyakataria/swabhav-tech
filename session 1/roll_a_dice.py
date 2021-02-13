import random

arr = [0,0,0,0,0,0]
for _ in range(100):
  x = random.randint(1,6)
  arr[x-1] += 1

for i in range(6):
  print('for ', i+1,"= ", arr[i])