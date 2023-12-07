with open('input.txt', 'r') as file:
  data = [line.rstrip('\n') for line in file.readlines()]

hands = [{
    'cards': x.split()[0],
    'value':int(x.split()[1])
  } for x in data ]

deck = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
labels = [[5], [1,4] ,[2,3], [1,1,3], [1,2,2], [1,1,1,2], [1,1,1,1,1]]
labels = labels[::-1]
rankings = [[], [], [], [], [], [], []]

# solve a
for hand in hands:
  label = []
  for card in deck:
    occ = hand['cards'].count(card)
    if occ > 0:
      label.append(occ)
  for ii, l in enumerate(labels):
    if sorted(label) == l:
      found_index = False
      jj = 0
      while not found_index and jj < len(rankings[ii]):
        r = rankings[ii][jj]['cards']
        for kk, c in enumerate(hand['cards']):
          if deck.index(c) < deck.index(r[kk]):
            found_index = True
            break
          if deck.index(c) > deck.index(r[kk]):
            break
        if found_index:
          break
        jj += 1      
      rankings[ii].insert(jj, hand)
      break

aa = [h['value'] for ii, l in enumerate(rankings) for h in l]
scores = []
for ii, a in enumerate(aa):
  scores.append((ii+1) * a) 
print(sum(scores))

# solve b
deck = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
rankings = [[], [], [], [], [], [], []]

for hand in hands:
  label = []
  jokers = hand['cards'].count('J')
  for card in deck[1:]:
    occ = hand['cards'].count(card)
    if occ > 0:
      label.append(occ)
  label = sorted(label)
  if label:
    label[-1] = label[-1] + jokers
  else:
    label = [5]
  for ii, l in enumerate(labels):
    if sorted(label) == l:
      found_index = False
      jj = 0
      while not found_index and jj < len(rankings[ii]):
        r = rankings[ii][jj]['cards']
        for kk, c in enumerate(hand['cards']):
          if deck.index(c) < deck.index(r[kk]):
            found_index = True
            break
          if deck.index(c) > deck.index(r[kk]):
            break
        if found_index:
          break
        jj += 1      
      rankings[ii].insert(jj, hand)
      break

aa = [h['value'] for ii, l in enumerate(rankings) for h in l]
scores = []
for ii, a in enumerate(aa):
  scores.append((ii+1) * a) 
print(sum(scores))
