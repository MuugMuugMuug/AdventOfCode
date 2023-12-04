from functools import reduce

def import_games_from_file(file_path, colors):
  with open(file_path, 'r') as file:
      data = [line.rstrip('\n') for line in file.readlines()]

  games = {}
  for i, line in enumerate(data):
      game_number = "".join([char for char in line.split(':')[0] if char.isdigit()])
      games[game_number] = []
      draws = line.split(':')[1].split(';')
      for draw in draws:
        games[game_number].append([])
        items = draw.split(',')
        draw_dict = {}
        for item in items:
           for color in colors:
              if color in item:
                number = int("".join([char for char in item if char.isdigit()]))
                draw_dict[color] = number
        games[game_number][-1] = draw_dict


  return games

max_cubes = {
   'red': 12,
   'green': 13,
   'blue': 14,
}

file_path = 'input.txt'
games = import_games_from_file(file_path, list(max_cubes.keys()))

def solve_a(games):
  possible_games = []
  for number, game in games.items():
    possible = True
    for k, v in max_cubes.items():

      if max([draw[k] for draw in game if k in draw]) > v:
        possible = False
    if possible:
      possible_games.append(int(number))

  print(sum(possible_games))

solve_a(games)

def solve_b(games):
  powers = []
  for number, game in games.items():
    min_cubes = []
    for k, v in max_cubes.items():
      
      min_cubes.append(max([draw[k] for draw in game if k in draw])) 
    powers.append(reduce(lambda x, y: x * y, min_cubes))

  print(sum(powers))
  return powers

powers = solve_b(games)