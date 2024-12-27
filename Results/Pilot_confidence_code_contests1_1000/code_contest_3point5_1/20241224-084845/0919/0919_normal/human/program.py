import heapq
from sys import stdin, stdout


def __main__(n, k):
    servers = [0] * k
    times = []

    for i in range(n):
        s, m = [int(x) for x in stdin.readline().split()]
        time = max(servers[0], s)
        heapq.heapreplace(servers, time + m)
        times.append(time + m)

    stdout.write('\n'.join(str(time) for time in times) + '\n')

if __name__ == '__main__':
    n, k = map(int, stdin.readline().split())
    __main__(n, k)