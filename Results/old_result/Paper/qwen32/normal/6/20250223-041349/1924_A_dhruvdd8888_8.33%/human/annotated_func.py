#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^5, for each test case, n and k are integers such that 1 <= n <= 26 and 1 <= k <= 26, m is an integer such that 1 <= m <= 1000, and s is a string of length m comprising only of the first k lowercase English alphabets. The sum of m and the sum of n over all test cases do not exceed 10^6.
def func_1():
    n, k, m = tuple(map(int, input().split()))
    s = input()
    us = set(chr(i + 97) for i in range(k))
    win = set()
    ans = []
    ps = 0
    for i in s:
        if i in us:
            win.add(i)
            if len(win) == k:
                ans.append(i)
                ps += 1
                win.clear()
        
    #State: `win` is a set containing fewer than `k` unique characters or is empty, `ans` is a list of characters that were the last character in each complete set of `k` unique characters found in `s`, and `ps` is the count of such complete sets.
    if (ps >= n) :
        return print('YES')
        #The program returns print('YES')
    #State: `win` is a set containing fewer than `k` unique characters or is empty, `ans` is a list of characters that were the last character in each complete set of `k` unique characters found in `s`, `ps` is the count of such complete sets, and `ps` is less than `n`
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: `win` contains all elements from `us` that were not in `win` initially, `ans` and `ps` remain unchanged, `us` remains unchanged.
#Overall this is what the function does:The function reads input values for `n`, `k`, `m`, and a string `s`, then checks if there are at least `n` occurrences of a complete set of `k` unique characters in `s`. If so, it prints 'YES'. Otherwise, it prints 'NO' and constructs a string based on the characters found and prints it.

