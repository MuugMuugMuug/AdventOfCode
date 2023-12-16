with open('input.txt', 'r') as file:
  data = [line.rstrip('\n') for line in file.readlines()]

init_seq = data[0].split(',')

def get_hash(s, current_hash=0):
  new_hash = ((current_hash + ord(s[0])) * 17) % 256
  if len(s) == 1:
    return new_hash
  return get_hash(s[1:], new_hash)

# solve a
hashes = []
for seq in init_seq:
  hashes.append(get_hash(seq))

print(sum(hashes))

# solve b
boxes = [[] for x in range(256)]

def find_label(label, box):
  for ii, seq in enumerate(box):
    l = read_seq(seq)
    if label == l[0]:
      return ii
  return -1

def read_seq(seq):
  if '=' in seq:
    label, num = seq.split('=')
    return label, num, True
  return seq.split('-')[0], -1, False
  

for seq in init_seq:
  label, num, contains_eq = read_seq(seq)
  b_num = get_hash(label)
  index = find_label(label, boxes[b_num])
  if contains_eq:
    if index >= 0:
      boxes[b_num][index] = seq
    else: 
      boxes[b_num].append(seq)
  elif index >= 0:
    del boxes[b_num][index]

fp = []
for ii, b in enumerate(boxes):
  for jj, l in enumerate(b):
    fp.append((ii+1) * (jj+1) * int(l.split('=')[1]))

print(sum(fp))