while True:
  h, w = map(int, raw_input().split())
  if (h == 0 and w == 0):
    break
  for i in range(0,h):
    for j in range(0,w):
      if i == 0 or j == 0 or i == h-1 or j == w-1:
        print ("#")
      else: 
        print (".")
    print
  