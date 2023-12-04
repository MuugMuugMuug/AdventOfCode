
file_path = 'input.txt'

with open(file_path, 'r') as file:
    data = [line.rstrip('\n') for line in file.readlines()]


win_nums = [[int(num) for num in line.split(':')[1].split('|')[0].strip().split()]
    for line in data]

my_nums =  [[int(num) for num in line.split(':')[1].split('|')[1].strip().split()]
    for line in data]

# solve_a and solve_b
points = []
cards = [1] * len(my_nums)
for i, row in enumerate(my_nums):
    occ = 0
    for num in row:
        if num in win_nums[i]:
            occ += 1
            if i + occ < len(my_nums):
                cards[i+occ] += cards[i]
                
    points.append(0 if occ == 0  else 2**(occ-1))

# a
print(sum(points))
# b
print(sum(cards))
      

            