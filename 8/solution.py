with open('input.txt', 'r') as file:
  data = [line.rstrip('\n') for line in file.readlines()]

lr_map = {
  'L': 0,
  'R': 1,
}

# solve a
lr = [lr_map[x] for x in data[0]]

network = {x.split('=')[0].strip(): x.split('=')[1].replace(')', "").replace('(', "").strip().split(', ') for x in data[2:]}

cur = 'AAA'
steps = 0
while cur != 'ZZZ':
  lr_index = lr[steps % len(lr)]
  cur = network[cur][lr_index]
  steps += 1

print(steps)

## solve b
import math

def find_lcm_of_list(numbers):
    lcm = 1
    for num in numbers:
        lcm = lcm * num // math.gcd(lcm, num)
    return lcm


lr = [lr_map[x] for x in data[0]]


network = {x.split('=')[0].strip(): x.split('=')[1].replace(')', "").replace('(', "").strip().split(', ') for x in data[2:]}
keys = [key for key in network if key[2] == 'A']

s = []
exit_found = False



for ii, key in enumerate(keys):
  steps = 0
  found_exit = False
  while not found_exit:
    lr_index = lr[steps % len(lr)]
    key = network[key][lr_index]
    steps += 1
    if key[2] == 'Z':
      s.append(steps)
      found_exit = True

  

print(find_lcm_of_list(s))
