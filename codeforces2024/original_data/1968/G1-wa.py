import sys
    
def int_input():
    return int(sys.stdin.readline().strip())

def string():
    return sys.stdin.readline().strip()

def map_int():
    return map(int, sys.stdin.readline().strip().split())

def list_int_input():
    return list(map(int, sys.stdin.readline().strip().split()))

def list_string_input():
    return list(sys.stdin.readline().strip().split())

def LPS_preprocess(pattern):
    n = len(pattern)
    lps = [0]*n
    j = 0
    i = 1
    while i < n:
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j-1]
    return lps

def count_substring(text,pattern):
    if len(pattern) == 0:
        return 0

    n = len(text)
    m = len(pattern)
    lps = LPS_preprocess(pattern)
    count = 0
    i = 0
    j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j-1]

        if j == m:
            count += 1
            j = 0

    return count

def solve():
    n,l,r = map_int()
    s = input()

    k = l

    left = 0
    right = n
    best = 0
    while left <= right:
        mid = left + (right - left) // 2

        if count_substring(s,s[:mid]) >= k:
            best = mid
            left = mid + 1
        else:
            right = mid - 1

    return best

if __name__ == '__main__':
    test_cases = int_input()
    for _ in range(test_cases):
        print(solve())