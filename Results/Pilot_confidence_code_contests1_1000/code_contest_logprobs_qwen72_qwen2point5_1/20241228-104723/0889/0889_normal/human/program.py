n = int(raw_input())
bricks = raw_input().split()
bricks = [int(i) for i in bricks]
smash = 0
result = []
pos = 1
if 1 not in bricks:
  smash = -1
else:
  for i in range(1,n+1):
    if i >= len(bricks): break
    while bricks[i-1] != i:
      bricks.pop(i-1)
      smash = smash+1
print(smash)