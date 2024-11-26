gets = lambda r=sys.stdin.readline: r().strip()
S = gets()
N = int(S[:-1])
C = ord(S[-1]) - ord('a')
M = N - 1 & 3
if M in (1, 2):
    N -= M
    M ^= 3
    N += M
print((N - 1) // 2 * 7 + (N - 1) // 4 * 2 + (6 - C))