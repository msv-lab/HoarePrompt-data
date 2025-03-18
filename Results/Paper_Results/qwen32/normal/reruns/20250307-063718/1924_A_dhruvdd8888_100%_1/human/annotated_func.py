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
        
    #State: t is an integer such that 1 <= t <= 10^5; n is an integer such that 1 <= n <= 26; k is an integer such that 1 <= k <= 26; m is an integer such that 1 <= m <= 1000; s is the input string; us is a set containing the first k lowercase letters of the alphabet; win is an empty set; ans is a list containing the last character of each set of k consecutive characters from s that are all in us; ps is the number of times a complete set of k characters from us was found in s.
    if (ps >= n) :
        return print('YES')
        #The program returns print('YES')
    #State: t is an integer such that 1 <= t <= 10^5; n is an integer such that 1 <= n <= 26; k is an integer such that 1 <= k <= 26; m is an integer such that 1 <= m <= 1000; s is the input string; us is a set containing the first k lowercase letters of the alphabet; win is an empty set; ans is a list containing the last character of each set of k consecutive characters from s that are all in us; ps is a list containing the number of times a complete set of k characters from us was found in s, and ps is less than n
    print('NO')
    #This is printed: NO
    for i in us:
        if i not in win:
            return print(''.join(ans) + i + 'a' * (n - len(ans) - 1))
        
    #State: - The output string will be the concatenation of the elements in `ans`, the first character `i` in `us`, and a string of 'a' characters such that the total length of the output string is `n`.
    #
    #Given the above understanding, the output state after the loop executes all its iterations is:
    #
    #Output State:
#Overall this is what the function does:The function `func_1` processes multiple test cases, each defined by integers `n`, `k`, and `m`, and a string `s`. It checks if there are at least `n` occurrences of sets of `k` consecutive characters in `s` that are all within the first `k` lowercase English alphabets. If such occurrences are found, it prints 'YES'. Otherwise, it constructs and prints a string of length `n` by appending characters from the sets found, a character from the set of the first `k` alphabets that was not in any set, and padding with 'a' characters if necessary.

