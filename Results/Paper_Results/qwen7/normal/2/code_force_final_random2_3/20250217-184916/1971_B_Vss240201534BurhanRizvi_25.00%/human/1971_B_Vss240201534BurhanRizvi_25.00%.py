import random
for _ in range(int(input())):
  s=input()
  s2=''.join(random.sample(s,len(s)))
  if s!=s2:
    print('Yes')
    print(s2)
  else:
    print('No')