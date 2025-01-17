def func_1(n, V):
    V = [bin(i)[2:] for i in V]
    S = []
    for i in range(2 ** n):
        s = bin(i)[2:]
        if len(s) < n:
            s = '0' * (n - len(s)) + s
        valid = True
        for j in range(n):
            if s[j] == '1':
                sub_s = s[:j] + s[j + 1:]
                if not any((sub_s.count('1') == int(v, 2) for v in V)):
                    valid = False
                    break
        if valid:
            S.append(bin(int(s, 2) + 1)[2:])
    S.sort()
    print(len(S))
    for s in S:
        print(int(s, 2))
print('Test Case 1:')
func_1(3, [15] * 7)
print('\nTest Case 2:')
func_1(5, [63] * 16)