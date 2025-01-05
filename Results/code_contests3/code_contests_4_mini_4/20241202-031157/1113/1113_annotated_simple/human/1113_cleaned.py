sys.stdout = io.BytesIO()
atexit.register(lambda : os.write(1, sys.stdout.getvalue()))
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
write = sys.stdout.write
maxint = float('inf')
res = []
T = int(input())
for t in range(T):
    for i in range(9):
        row = input().strip()
        nRow = ''
        for i in row:
            if i == '9':
                nRow += '1'
            else:
                nRow += i
        res.append(nRow)
write('\n'.join(res))