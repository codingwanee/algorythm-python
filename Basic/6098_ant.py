game = [list(map(int, input().split())) for _ in range(10)]
a, b = 1, 1

while (game[a][b] == 0):
  game[a][b] = 9
  if game[a][b+1] == 0 or game[a][b+1] == 2:
    b += 1
  else:
    a += 1
if(game[a][b] == 2):
  game[a][b] = 9
for i in game:
  print (' '.join(repr(j) for j in i))