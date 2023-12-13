from itertools import combinations

with open('test.txt', 'r') as file:
  data = [line.rstrip('\n') for line in file.readlines()]

def get_combinations_indices(arr, r):
    return combinations(arr, r)


def insert_at_indices(input_string, indices, replacement_char='#'):
    result_list = list(input_string)

    for index in indices:
        if 0 <= index < len(result_list):
            result_list[index] = replacement_char

    return ''.join(result_list)

def count_joining_chars(input_string, ch='#'):
    counts = []
    current_count = 0

    for char in input_string:
        if char == ch:
            current_count += 1
        elif current_count > 0:
            counts.append(current_count)
            current_count = 0

    if current_count > 0:
        counts.append(current_count)

    return counts

strings = [x.split()[0] for x in data]
pattern = [[int(y) for y in x.split()[1].split(',')] for x in data]

# solve a
combs = []
for ii,s in enumerate(strings):
  pat = pattern[ii]
  num_damaged =s.count('#')
  num_total = sum(pat)
  indices = [index for index, c in enumerate(s) if c == '?']
  options = get_combinations_indices(indices, num_total - num_damaged)
  c = 0
  for o in options:
     if count_joining_chars(insert_at_indices(s, o)) == pat:
         c += 1
  combs.append(c)
     
print(sum(combs))

# solve b
strings_b = []
for s in strings:
  s_b = s
  for ii in range(4):
    s_b = s_b + '?' + s
  strings_b.append(s_b)

combs = []
for ii,s in enumerate(strings_b):
  print(ii)
  pat = pattern[ii] * 5
  num_damaged =s.count('#')
  num_total = sum(pat)
  indices = [index for index, c in enumerate(s) if c == '?']
  options = get_combinations_indices(indices, num_total - num_damaged)
  c = 0
  for o in options:
     if count_joining_chars(insert_at_indices(s, o)) == pat:
         c += 1
  combs.append(c)

print(sum(combs))