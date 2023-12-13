import math

with open('input.txt', 'r') as file:
  data = [line.rstrip('\n') for line in file.readlines()]

max_row = len(data) 
max_col= len(data[0])

for ii, r in enumerate(data):
  for jj, c in enumerate(r):
    if c == 'S':
      routes = [[[ii,jj]]]

pipes ={
  '|': [[1,0], [-1, 0]],
  '-': [[0,1], [0, -1]],
  'L': [[1,0], [0,-1]],
  'J': [[1,0], [0,1]],
  '7': [[-1,0], [0,1]],
  'F': [[-1,0], [0,-1]],
  'S': [[1,0], [-1, 0],[0,1], [0, -1]],
  '.': []
}

def get_adjacent_cors(cors, max_row=max_row, max_col=max_col):
  adjacent_cors = [[cors[0]+1, cors[1]], [cors[0]-1, cors[1]], [cors[0], cors[1]+1], [cors[0], cors[1]-1]]
  return [ac for ac in adjacent_cors if ac[0] < max_row and ac[0] >= 0 and ac[1] < max_col and ac[1] >= 0]


is_loop_completed = False
while not is_loop_completed:
  new_routes = []
  for route in routes:
    cors = route[-1]
    current_pipe = data[cors[0]][cors[1]]
    acs = [ac for ac in get_adjacent_cors(cors)]
    for ac in acs:
      row = ac[0]
      col = ac[1]
      new_pipe = data[row][col]
      if ac not in route or (new_pipe == 'S' and len(route) > 2):
        new_diff = [ac[ii] - c for ii,c in enumerate(cors)]
        cur_diff = [c - ac[ii] for ii,c in enumerate(cors)]
        if new_diff in pipes[new_pipe] and cur_diff in pipes[current_pipe]:
          new_routes.append(route + [ac])
          if new_pipe == 'S':
            is_loop_completed = True
  if new_routes:
    routes = new_routes
    if len(routes[0]) > 19600:
      is_loop_completed = True
  else:
    is_loop_completed = True

print(math.ceil(len(new_routes[0][1:])/2))

# solve b
enclosed = []
for ii,row in enumerate(data):
  for jj,tile in enumerate(row):
    if [ii,jj] not in routes[0]:
        enclosed.append([ii,jj])


e = []
o = []
for jj, c in enumerate(enclosed):
  print(jj)
  is_inside_loop = True
  is_filled = False
  if c in e or c in o:
    continue
  new = [c[:]]
  acc = [c[:]]
  while not is_filled:
    foo = []
    for n in new:
      adjacent = get_adjacent_cors(n)
      if len(adjacent) < 4: # not within the loop
        is_inside_loop = False
      b = [a for a in adjacent if a not in acc and a not in routes[0]]
      foo = foo + b
      acc = acc + b
    if not b:
      is_filled = True
    new = foo
  if is_filled and is_inside_loop:
    acc = [a for a in acc if a not in e]
    e = e + acc
  else:
    acc = [a for a in acc if a not in o]
    o = o + acc
  

print(len(e))