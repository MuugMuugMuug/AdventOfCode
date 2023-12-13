import numpy as np
from math import ceil

with open('input.txt', 'r') as file:
  data = [line.rstrip('\n') for line in file.readlines()]

patterns = [[]]
for row in data:
  if not row:
    patterns[-1] = np.array(patterns[-1])
    patterns.append([])
    continue
  patterns[-1].append(list(row))
patterns[-1] = np.array(patterns[-1])

def expected_amount(n, l):
  return min(ceil(n/2), l - ceil(n/2))

def get_reflection(p):
  r = 0
  num_cols = p.shape[1]
  matching = []
  for ii in range(num_cols):
    col_1 = p[:,ii]
    for jj in range(ii+1,num_cols):
      col_2 = p[:, jj]
      if np.array_equal(col_1, col_2):
        matching.append(ii + jj)
  for m in set(matching):
    if expected_amount(m, num_cols) == matching.count(m):
      r = ceil(m/2)
  return r

acc = 0
for p in patterns:
   acc += get_reflection(p) # columns
   acc += 100 * get_reflection(np.transpose(p)) # rows

print(acc)