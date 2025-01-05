a = raw_input()
for i in a:
    if i in ['H', 'Q', '9']:
        print('YES')
        a = 'tstr123'
        break
if a != 'tstr123':
    print('NO')