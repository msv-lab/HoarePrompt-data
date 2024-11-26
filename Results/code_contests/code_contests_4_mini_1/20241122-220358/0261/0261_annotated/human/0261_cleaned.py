alphabet = raw_input()
data = alphabet.split()
data = [int(i) for i in data]
data.sort()
if data[0] + data[3] == data[1] + data[2] or data[0] + data[1] + data[2] == data[3]:
    print('YES')
else:
    print('NO')