num_string = raw_input()


num_hash = {'1': True, '9': True, '7': True, '4': True}

for s in num_string:
  if num_hash.has_key(s):
    del num_hash[s]

if len(num_hash) == 0:
  print("YES")
else:
  print("NO")