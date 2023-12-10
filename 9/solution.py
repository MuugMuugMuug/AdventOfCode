from functools import reduce

with open('input.txt', 'r') as file:
  data = [line.rstrip('\n') for line in file.readlines()]

histories = [[int(x) for x in row.split()] for row in data]


# solve a and b
next_values = []
prev_values = []

def get_diffs(l):
  return [l[ii+1] - c for ii,c in enumerate(l[0:-1])]

for hist in histories:
  diffs = [hist]
  finished = False
  while not finished:
    diffs.append(get_diffs(diffs[-1]))
    if len(set(diffs[-1])) == 1:
      finished = True
  prev_values.append(reduce(lambda x, y: y - x, [diff[0] for diff in diffs][::-1]))
  next_values.append(sum([diff[-1] for diff in diffs]))

print(sum(next_values))
print(sum(prev_values))

