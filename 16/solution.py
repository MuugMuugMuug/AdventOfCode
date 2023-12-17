import math
import sys

sys.setrecursionlimit(10**9)

with open('test.txt', 'r') as file:
  data = [line.rstrip('\n') for line in file.readlines()]

num_rows = len(data[0])
num_cols = len(data)

def rotate_point(point, angle_degrees):
  angle_radians = math.radians(angle_degrees)
  
  rotation_matrix = [
      [math.cos(angle_radians), -math.sin(angle_radians)],
      [math.sin(angle_radians), math.cos(angle_radians)]
  ]

  rotated_x = rotation_matrix[0][0] * point[0] + rotation_matrix[0][1] * point[1]
  rotated_y = rotation_matrix[1][0] * point[0] + rotation_matrix[1][1] * point[1]

  return [round(rotated_x), round(rotated_y)]


def is_over_edge(pos, num_rows=num_rows, num_cols=num_cols):
  return pos[0] >= num_cols or pos[1] >= num_rows or pos[0] < 0 or pos[1] < 0

def is_in_loop(head, beams):
  return head in beams

def get_new_directions(dir, pos, data=data):
  char = data[pos[0]][pos[1]]
  if char == '.':
    return [dir]
  if char == '-':
    return [[0,1], [0,-1]] if dir[1] == 0 else [dir]
  if char == '|':
    return [[1,0], [-1,0]] if dir[0] == 0 else [dir]
  if char == '\\':
    return [rotate_point(dir,-90)] if dir[0] == 0 else [rotate_point(dir,90)]
  if char == '/':
    return [rotate_point(dir,90)] if dir[0] == 0 else [rotate_point(dir,-90)]

def get_step(pos, dir):
  return [[pos[0] + dir[0], pos[1] + dir[1]], dir]

def get_next_steps(pos, new_dirs, beams):
  return [get_step(pos,d) for d in new_dirs if not is_over_edge(get_step(pos, d)[0]) and not is_in_loop(get_step(pos,d),beams)]
  
def trace_beam(queue, beams=[]):
  if len(queue) == 0:
    return beams
  
  pos = queue[0][0]
  dir = queue[0][1]
  beams.append(queue[0])

  new_dirs = get_new_directions(dir, pos)
  next_steps = get_next_steps(pos, new_dirs, beams)
    
  if len(next_steps) == 0:
    return trace_beam(queue[1:], beams)
  
  next_step = next_steps[0] 
  new_queue = queue + next_steps[1:]

  return trace_beam(new_queue[1:] +[next_step], beams)
  
def get_unique_locs(beams):
  return set([tuple(x[0]) for x in beams])

# solve a
queue = [[[0,0],[0,1]]] # [location, direction]
num_locs = len(get_unique_locs(trace_beam(queue, [])))
print(num_locs)

# solve b
qs = []
num_locs_list = []
for ii in range(num_cols):
  qs.append([[[ii,0],[0,1]]])
  qs.append([[[ii,num_rows-1],[0,-1]]])
for jj in range(num_rows):
  qs.append([[[0,jj],[1,0]]])
  qs.append([[[num_cols-1,jj],[-1,0]]])

num_locs = 0
index = -1
for ii, q in enumerate(qs):
  nl = len(get_unique_locs(trace_beam(q, [])))
  if nl > num_locs:
    num_locs = nl
    index = ii

print(num_locs)
print(qs[index])