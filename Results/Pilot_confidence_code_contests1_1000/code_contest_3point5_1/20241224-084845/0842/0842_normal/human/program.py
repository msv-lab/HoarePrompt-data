s = str(raw_input())
no_flag = False
for i in range(len(s)):
  if i%2 == 0:
    if s[i] == 'L':
      print('No')
      no_flag = True
      break
  else:
    if s[i] == 'R':
      print('No')
      no_flag = True
      break
if no_flag == False:
  print('Yes')