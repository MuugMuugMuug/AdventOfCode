from functools import reduce
from math import ceil, floor

with open('input.txt', 'r') as file:
  data = [line.rstrip('\n') for line in file.readlines()]

times = [int(x) for x in data[0].split(':')[1].split()]
distances = [int(x) for x in data[1].split(':')[1].split()]

# solve a
ww =[]
for ii, time in enumerate(times):
  wins = 0
  for v in range(time+1):
    dist = v * (time - v)
    if dist > distances[ii]:
      wins += 1
  ww.append(wins)

print(reduce(lambda x, y: x * y, ww))

# solve b
time = int("".join([x for x in data[0] if x.isdigit()]))
distance = int("".join([x for x in data[1] if x.isdigit()]))

wins = 0
for v in range(time+1):
  dist = v * (time - v)
  if dist > distance:
    wins += 1

print(wins)

# more elegant
# quadratic eqation -x**2 + b * x + c
# c is -1 * distance to beat, b is length of the race, x is how long you press the button
# discriminant = b**2 - 4 * a * c
d = time**2 - 4 * distance
x1 = (-1*time + d**0.5) / -2
x2 = (-1*time - d**0.5) / -2
wins = floor(x2) - ceil(x1) + 1
print(wins)
