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
        
    #State: - `t` is still an integer such that 1 <= t <= 10^5.
    #- `n` is still an integer such that 1 <= n <= 26.
    #- `k` is still an integer such that 1 <= k <= 26.
    #- `m` is still an integer such that 1 <= m <= 1000.
    #- `s` is the same input string.
    #- `us` is still a set containing the first `k` lowercase letters of the English alphabet.
    #- `win` is an empty set.
    #- `ans` is a list containing the last characters of each sequence of `k` distinct characters from `us` found in `s`.
    #- `ps` is the count of such sequences of `k` distinct characters.
    #
    #Output State:
    if (ps >= n) :
        return print('YES')
        #The program returns 'YES'
    #State: `t` is still an integer such that 1 <= t <= 10^5. `n` is still an integer such that 1 <= n <= 26. `k` is still an integer such that 1 <= k <= 26. `m` is still an integer such that 1 <= m <= 1000. `s` is the same input string. `us` is still a set containing the first `k` lowercase letters of the English alphabet. `win` is an empty set. `ans` is a list containing the last characters of each sequence of `k` distinct characters from `us` found in `s`. `ps` is the count of such sequences of `k` distinct characters. Additionally, `ps` is less than `n`.
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: 
#Overall this is what the function does:The function reads input values for `n`, `k`, and `m`, followed by a string `s`. It then checks if there are at least `n` sequences of `k` distinct characters from the first `k` lowercase English alphabets in the string `s`. If such sequences exist, it prints 'YES'. Otherwise, it prints 'NO' and constructs a string based on the characters found and prints it.

