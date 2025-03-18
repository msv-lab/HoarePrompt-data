t = int(input())
 
 
 
def solve(s):
    n = len(s)
    A = [] 
    idx_A = []
    for i in range(0, n):
        if s[i] == '>':
            if (len(idx_A) == 0):
                A.append(0)
            else:
                x = A[len(A) - 1] + (i - idx_A[len(idx_A) - 1]) * len(idx_A)
                A.append(x)
            idx_A.append(i)
    B = []
    idx_B = []
    for j in range(0, n):
        i = n - 1 - j
        if s[i] == '<':
            if (len(idx_B) == 0):
                B.append(0)
            else:
                x = B[len(B) - 1] + (idx_B[len(B) - 1] - i) * len(idx_B)
                B.append(x)
            idx_B.append(i)
    l = 0
    r = len(B)
 
 
    for i in range(0, n):
        if (s[i] == '>'):
            if l < r:
                a = A[l]
                x = r - (l + 2)
                b = B[r - 1]
                if x >= 0:
                    b = b - B[x]
                    b = b - (idx_B[x] - idx_B[r - 1]) * (x + 1)
                b = b + (idx_B[r - 1] - i) * (l + 1)
                print(a * 2 + b * 2 + i + 1, end = " ")
            else:
                if (r == 0):
                    print(n - i, end = " ")
                else:
                    a = B[r - 1] + (idx_B[r - 1] - i) * r
                    b = A[l - 1]
                    if l - r > 0:
                        b = b - A[l - r - 1]
                        b = b - (idx_A[l - 1] - idx_A[l - r - 1]) * (l - r)
                    b = b + (i - idx_A[l - 1]) * r
                    print(a * 2 + b * 2 + (n - i), end = " ")
            l += 1
        else:
            r -= 1
            if (l <= r):
                if (l == 0):
                    print(i + 1, end = " ")
                else:
                    a = A[l - 1]
                    a = a + (i - idx_A[l - 1]) * l
                    b = B[r]
                    if r - l >= 0:
                        b = b - B[r - l]
                        b = b - (idx_B[r - l] - i) * (r - l)
                    b = b + (idx_B[r] - i) * l
                    print(a * 2 + b * 2 + i + 1, end = " ")
            else:
                if (r == 0):
                    print((n - i) + (i - idx_A[l - 1]) * 2, end = " ")
                else:
                    a = B[r]
                    b = A[l - 1]
                    if l - r - 1 > 0:
                        b = b - A[l - r - 2]
                        b = b - (idx_A[l - 1] - idx_A[l - r - 2]) * (l - r - 1)
                    b = b + (i - idx_A[l - 1]) * (r + 1)
                    print(a * 2 + b * 2 + (n - i), end = " ")
 
 
for i in range(0, t):
    n = int(input())
    s = input()
    solve(s)
    print()