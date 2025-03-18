s = input()
while '00' in s:
    s = s.replace('00', '0')
while '11' in s:
    s = s.replace('11', '1')
if s == '1' or s == '':
    print('no')
else:
    print('yes')
