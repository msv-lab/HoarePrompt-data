raw_input()
interesting = set(map(int, raw_input().split()))
boredom = 0
for x in range(1, 91):
  boredom += 1
  if x in interesting:
    boredom = 0
  elif boredom == 15:
    print(x)
    import sys; sys.exit()
print(90)
