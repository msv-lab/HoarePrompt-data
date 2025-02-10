#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^5, and s and f are strings of length n consisting of '0' and '1' characters, representing the initial and desired states of the boxes, respectively. The sum of n over all test cases does not exceed 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        s = input()
        
        t = input()
        
        a = b = 0
        
        for i in range(n):
            a += s[i] > t[i]
            b += s[i] < t[i]
        
        print(max(a, b))
        
    #State: After all iterations of the loop, `a` will contain the total count of positions where the character in string `s` is greater than the corresponding character in string `t`; `b` will contain the total count of positions where the character in string `s` is less than the corresponding character in string `t`; `i` will be `n - 1` after the loop finishes; `t` will remain unchanged as it was an input and not modified by the loop.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer `n`, a string `s` of length `n` consisting of '0' and '1' characters, and another string `t` of the same length. For each test case, it counts the number of positions where the characters in `s` are greater than and less than the corresponding characters in `t`. It then prints the maximum of these two counts, which represents the minimum number of operations required to transform the initial state `s` into a state where each character matches the corresponding character in `t`.

