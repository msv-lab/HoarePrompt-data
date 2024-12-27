from sys import stdin, stdout
from itertools import repeat
def main():
    n = int(stdin.readline())
    a = map(int, stdin.readline().split())
    m = int(stdin.readline())
    q = map(int, stdin.read().split(), repeat(10, 2 * m))
    q[1] = (q[1] - q[0]) / 2
    for i in xrange(1, m):
        q[i*2+1] = (q[i*2+1] - q[i*2]) / 2 + q[i*2-2]
    ans = [('odd','even')[q[i*2+1]%2] for i in xrange(m)]
    stdout.write('\n'.join(ans))
main()
