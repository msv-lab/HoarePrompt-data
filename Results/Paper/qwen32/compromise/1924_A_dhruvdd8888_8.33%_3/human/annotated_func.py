#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^5. For each test case, n and k are integers such that 1 <= n <= 26 and 1 <= k <= 26. m is an integer such that 1 <= m <= 1000. s is a string of length m consisting only of the first k lowercase English alphabets. The sum of m and the sum of n over all test cases do not exceed 10^6.
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
        
    #State: t is an integer such that 1 <= t <= 10^5; n, k, and m are integers read from the input, where 1 <= n <= 26, 1 <= k <= 26, and 1 <= m <= 1000; s is the newly input string of length m consisting only of the first k lowercase English alphabets; us is a set containing the first k lowercase English alphabets; win is an empty set; ans is a list containing the characters that completed sets of k unique characters found in s; ps is an integer representing the number of complete sets of k unique characters found in s.
    if (ps >= n) :
        return print('YES')
        #The program returns 'YES'
    #State: t is an integer such that 1 <= t <= 10^5; n, k, and m are integers read from the input, where 1 <= n <= 26, 1 <= k <= 26, and 1 <= m <= 1000; s is the newly input string of length m consisting only of the first k lowercase English alphabets; us is a set containing the first k lowercase English alphabets; win is an empty set; ans is a list containing the characters that completed sets of k unique characters found in s; ps is a integer representing the number of complete sets of k unique characters found in s; and ps is less than n
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: - The loop will print a string for each character in `us` that is not in `win`. Since `win` is initially empty, it will print a string for each character in `us`.
    #   - Each printed string will be of the form `i` followed by `n - 1` 'a's.
    #
    #Since `us` contains the first `k` lowercase English alphabets, the loop will print `k` strings, each starting with a different character from `us` followed by `n - 1` 'a's.
    #
    #Output State:
#Overall this is what the function does:The function `func_1` reads multiple test cases, each defined by integers `n`, `k`, and `m`, and a string `s`. For each test case, it checks if the string `s` contains at least `n` disjoint sets of `k` unique characters from the first `k` lowercase English alphabets. If such sets are found, it prints 'YES'. If not, it prints 'NO' and then prints additional strings based on the characters not found in the sets.

