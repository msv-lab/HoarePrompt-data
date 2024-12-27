import sys

inp = [int(i.split(' ')[0]) for i in sys.stdin.read().strip().splitlines()[1:]]

res = 0
for i in range(len(inp) - 1):
    if inp[i] > inp[i+1]:
        res += 1
sys.stdout.write(str(res))
