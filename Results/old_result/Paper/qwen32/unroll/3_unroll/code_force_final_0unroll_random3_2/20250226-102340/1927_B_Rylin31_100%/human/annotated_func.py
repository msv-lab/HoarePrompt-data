#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each of the t test cases, n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where 0 <= a_i < n. The sum of n over all test cases does not exceed 2 * 10^5. It is guaranteed that for each test case, there exists a suitable string s consisting of lowercase Latin letters a-z that corresponds to the given trace a.
def func():
    for i in range(int(input())):
        l = int(input())
        
        s = [(0) for i in range(l)]
        
        array = list(map(int, input().split()))
        
        ans = ''
        
        for j in array:
            ans += chr(s[j] + 97)
            s[j] += 1
        
        print(ans)
        
    #State: A sequence of strings, each corresponding to the output of each test case, constructed by mapping each value in `array` to a character based on the current value in `s` and then incrementing that value in `s`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it constructs and outputs a string `s` of lowercase Latin letters, where each character in `s` is determined by the values in `a` and the current state of a frequency counter `s`.

