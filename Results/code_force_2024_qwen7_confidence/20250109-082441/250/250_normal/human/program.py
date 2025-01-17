import sys, threading
# from collections import defaultdict

input = lambda : sys.stdin.readline().strip()


def read_arr():
    return list(map(int, input().split()))
def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
def read_mult():
    return map(int, input().split())

def first_xor(n):
    if n % 4 == 0:
        return n
    if n % 4 == 1:
        return 1
    if n % 4 == 2:
        return n + 1
    return 0

def main():
    s = ""
    k = 0
    memo = {}
    def dp(ind, n):
        if n == 0:
            return ""
        # if 
        if (ind, n) in memo:
            return memo[(ind, n)]
        
        visited = {}
        for i in range(ind, len(s)):
            if len(visited) == k:
                break
            if ord(s[i]) - 97 < k and s[i] not in visited:
                visited[s[i]] = i

        if len(visited) < k:
            for i in range(26):
                ch = chr(i + 97)
                if ch not in visited:
                    return ch
        
        for ch in visited:
            pos = visited[ch]
            res = dp(pos + 1, n - 1)
            if res != "":
                return ch + res
        
        memo[(ind, n)] = ""
        return ""

    t = int(input())
    for _ in range(t):
        n,k,m = read_mult()
        s = input()
        
        ans = dp(0, n)
        if ans == "":
            print("YES")
        else:
            print("NO")
            print(ans)
        memo = {}


if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()