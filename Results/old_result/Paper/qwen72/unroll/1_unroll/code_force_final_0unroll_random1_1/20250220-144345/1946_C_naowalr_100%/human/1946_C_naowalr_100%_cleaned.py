threading.stack_size(1 << 26)
sys.setrecursionlimit(1 << 30)

def func_1():

    def solve():
        global numCuts
        (n, k) = list(map(int, sys.stdin.readline().split()))
        adj = [[] for i in range(n + 1)]
        for i in range(n - 1):
            (a, b) = list(map(int, sys.stdin.readline().split()))
            adj[a].append(b)
            adj[b].append(a)
        L = 1
        R = int(100000.0 + 1)
        numCuts = 0

        def dfs(a, p):
            global numCuts
            vertices = 1
            for b in adj[a]:
                if b != p:
                    vertices += dfs(b, a)
            if vertices >= x and a != p:
                numCuts += 1
                return 0
            return vertices
        while R - L > 1:
            x = (L + R) // 2
            numCuts = 0
            leftover = dfs(1, 1)
            if numCuts > k or (numCuts == k and leftover >= x):
                L = x
            else:
                R = x
        print(L)
    for _ in range(int(sys.stdin.readline())):
        solve()
main_thread = threading.Thread(target=boom)
main_thread.start()
main_thread.join()