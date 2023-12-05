with open('input.txt', 'r') as file:
  data = [line.rstrip('\n') for line in file.readlines()]

seeds = [int(num) for num in data[0].split(':')[1].strip().split()]
maps = []
for line in data[2:]:
  if line and not line[0].isdigit():
    maps.append([])
  if line and line[0].isdigit():
    maps[-1].append([int(num) for num in line.strip().split()])

def mapping(x, rows):
  for r in rows:
    if x >= r[1] and x <= r[1] + r[2] -1:
      return x - r[1] + r[0]
  else:
    return x

# solve a
mapped_seeds = []
for seed in seeds:
  for m in maps:
    seed = mapping(seed, m)
  mapped_seeds.append(seed)

print(min(mapped_seeds))

# solve b
queue = []
for ii, c in enumerate(seeds[0:int(len(seeds)/2)]):
  queue.append([seeds[ii*2], seeds[ii*2+1]])

mapped_seeds = []
for m in maps:
  ii = 0
  mapped = []
  while ii < len(queue) and ii < 20:
    c = queue[ii]
    sr_max = c[0] + c[1] - 1
    is_mapped = False
    for l in m:
      mp_max = l[1] + l[2] - 1
      if sr_max >= l[1] and c[0] <= mp_max:
        is_mapped = True
        start = max([c[0],l[1]])
        rng = min([sr_max, mp_max]) - start + 1
        mapped.append([start +l[0] - l[1], rng])
        if c[0] < l[1]: 
          queue.append([c[0], l[1] - c[0]])
        if sr_max > mp_max:
          queue.append([mp_max + 1, sr_max - mp_max])
        break
    if not is_mapped:
      mapped.append(c)
    ii += 1
  queue = mapped

print(min([x[0] for x in mapped]))

