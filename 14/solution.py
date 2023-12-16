import numpy as np

with open('input.txt', 'r') as file:
  data = np.array([list(line.rstrip('\n')) for line in file.readlines()])

for ii in range(data.shape[1]):
  col = data[:,ii]
  num_rocks = 0
  stop_pos = -1
  for jj,c in enumerate(col):
    if c == '#':
      stop_pos = jj
      num_rocks = 0
    elif c == 'O':
      col[jj] = '.'
      col[stop_pos + num_rocks + 1] = 'O'
      num_rocks += 1

acc = 0
num_rows = data.shape[0]
for ii in range(num_rows):
  acc += list(data[ii,:]).count('O') * (num_rows - ii)

print(acc)

for ii in range(10**9):
  if ii % 10**7 == 0:
    print(ii / 10**6)
  data = data.transpose()




