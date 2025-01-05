def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        memo[c] += 1
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
    print('Yes' if result else 'No')
func_1()