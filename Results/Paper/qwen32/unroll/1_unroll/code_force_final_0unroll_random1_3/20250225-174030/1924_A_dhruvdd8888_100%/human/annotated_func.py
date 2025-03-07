#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^5. For each test case, n and k are integers such that 1 <= n <= 26 and 1 <= k <= 26, and m is an integer such that 1 <= m <= 1000. The string s is of length m and contains only the first k lowercase English alphabets. The sum of m and the sum of n over all test cases do not exceed 10^6.
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
        
    #State: 
    if (ps >= n) :
        return print('YES')
        #The program returns None after printing 'YES'
    #State: `ps` is less than `n`
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            return print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: the printed string formed by joining `ans`, the first element `i` from `us` not in `win`, and 'a' characters to reach length `n`.
#Overall this is what the function does:The function `func_1` reads input values `n`, `k`, `m`, and a string `s`. It checks if the string `s` contains at least `n` distinct sequences of all `k` specified lowercase English alphabets. If it does, it prints 'YES'. If not, it prints 'NO' and then constructs and prints a string of length `n` that includes all `k` alphabets if possible, padding with 'a' if necessary.

