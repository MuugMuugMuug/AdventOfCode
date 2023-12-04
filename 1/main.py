file_path = 'data.txt'

with open(file_path, 'r') as file:
    data = [line.strip() for line in file]

array = [line for line in data]

def words_to_numbers(text):
    word_to_number = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    for number in word_to_number:
         text = text.replace(number, word_to_number[number])

    return text

# a
values = []
for row in array:
      for value in row:
           if value.isdigit():
                first_digit = value
                break
      for value in reversed(row):
           if value.isdigit():
                last_digit = value
                break
      values.append(int(first_digit+last_digit))

print(sum(values))

# b
values = []
first_digit = None
last_digit = None
for row in array:
  for ii, c in enumerate(row):
    if not first_digit:
      substr = words_to_numbers(row[0:ii+1])
      for value in substr:
        if value.isdigit():
          first_digit = value
          break
    if not last_digit:
      substr = words_to_numbers(row[::-1][0:ii+1][::-1])
      for value in substr:
        if value.isdigit():
            last_digit = value
            break   
    if first_digit and last_digit:
        break       

  values.append(int(first_digit+last_digit))
  first_digit = None
  last_digit = None

print(sum(values))