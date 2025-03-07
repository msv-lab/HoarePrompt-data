#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^5. For each test case, n and k are integers such that 1 <= n <= 26 and 1 <= k <= 26, and m is an integer such that 1 <= m <= 1000. The string s is of length m and consists only of the first k lowercase English alphabets. The sum of m and the sum of n over all test cases do not exceed 10^6.
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
        
    #State: - `t` is unchanged.
    #- `n` is unchanged.
    #- `k` is unchanged.
    #- `m` is unchanged.
    #- `s` is unchanged.
    #- `us` is unchanged.
    #- `win` is an empty set.
    #- `ans` is a list containing the last letter of each complete set of `k` unique letters found in `s`.
    #- `ps` is the count of such complete sets.
    #
    #Output State:
    if (ps >= n) :
        return print('YES')
        #The program returns print('YES')
    #State: `t` is unchanged. `n` is unchanged. `k` is unchanged. `m` is unchanged. `s` is unchanged. `us` is unchanged. `win` is an empty set. `ans` is a list containing the last letter of each complete set of `k` unique letters found in `s`. `ps` is the count of such complete sets, and `ps` is less than `n`.
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            return print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: t is unchanged. n is unchanged. k is unchanged. m is unchanged. s is unchanged. us is unchanged. win is an empty set. ans is a list containing the last letter of each complete set of k unique letters found in s. ps is the count of such complete sets, and ps is less than n. The program prints ''.join(ans) + x + 'a' * (n - len(ans) - 1) and terminates.
#Overall this is what the function does:The function `func_1` reads input values for the number of test cases `t`, and for each test case, it reads integers `n`, `k`, and `m`, and a string `s`. It then checks if the string `s` contains at least `n` complete sets of `k` unique letters. If it does, it prints 'YES'. If not, it prints 'NO' and attempts to construct and print a string of length `n` using the letters found in `s` and additional 'a' characters to meet the length requirement.

