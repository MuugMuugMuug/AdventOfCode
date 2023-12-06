file_path = 'input.txt'

with open(file_path, 'r') as file:
    data = [line.rstrip('\n') for line in file.readlines()]


def is_symbol_adjacent(row, col, matrix=data):
  row_nums = [x for x in [row-1, row, row+1] if x >= 0 and x < len(matrix)]
  col_nums = [x for x in [col-1, col, col+1] if x >= 0 and x < len(matrix[0])]

  for row in row_nums:
    for col in col_nums:
      char = matrix[row][col]
      if not char.isdigit() and char != '.':
        return 1
  return 0

def get_adjacent_cors(row, col, matrix=data):
  row_nums = [x for x in [row-1, row, row+1] if x >= 0 and x < len(matrix)]
  col_nums = [x for x in [col-1, col, col+1] if x >= 0 and x < len(matrix[0])]

  return row_nums, col_nums
 
# solve a
numbers = []
for i, row in enumerate(data):
  digits = []
  is_valid = []
  for j, char in enumerate(row):
    if char.isdigit():
      digits.append(char)
      is_valid.append(is_symbol_adjacent(i,j))
    else:
      if digits and sum(is_valid) > 0:
        numbers.append(int("".join(digits)))
      digits = []
      is_valid = []
  if digits:
    if digits and sum(is_valid) > 0:
      numbers.append(int("".join(digits)))
    digits = []
    is_valid = []

print(sum(numbers))

# solve b
numbers = []
for i, row in enumerate(data):
  digits = []
  row_cors = []
  col_cors = []
  for j, char in enumerate(row):
    if char.isdigit():
      digits.append(char)
      cors = get_adjacent_cors(i, j)
      row_cors = row_cors + cors[0]
      col_cors = col_cors + cors[1]
    else:
      if row_cors:
        numbers.append({
          'value': int("".join(digits)),
          'adjacent_rows': set(row_cors),
          'adjacent_cols': set(col_cors),
          })
        digits = []
        row_cors = []
        col_cors = []
  if row_cors:
    numbers.append({
        'value': int("".join(digits)),
        'adjacent_rows': set(row_cors),
        'adjacent_cols': set(col_cors),
        })
    digits = []
    row_cors = []
    col_cors = []

gear_ratios = []
for i, row in enumerate(data):
  for j, char in enumerate(row):
    if char == '*':
      gear_adjacent = []
      for number in numbers:
        if i in number['adjacent_rows'] and j in number['adjacent_cols']:
          gear_adjacent.append(number['value'])
      if len(gear_adjacent) == 2:
        gear_ratios.append(gear_adjacent[0] * gear_adjacent[1])

print(sum(gear_ratios))


        
            
  
