#State of the program right berfore the function call: The function `func` is expected to process multiple test cases. Each test case includes an integer `n` (1 ≤ n ≤ 2·10^5) representing the length of the lost string, and a list of integers `a` of length `n` where each element `a_i` (0 ≤ a_i < n) represents the trace of the string. The sum of `n` over all test cases does not exceed 2·10^5. It is guaranteed that for each trace, there exists at least one valid string `s` consisting of lowercase Latin letters a-z.
def func():
    for i in range(int(input())):
        l = int(input())
        
        array = list(map(int, input().split()))
        
        alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        rev_array = array[::-1]
        
        ans = []
        
        for j in range(l):
            ans.append(alp[rev_array[j:].count(rev_array[j]) - 1])
        
        print(''.join(map(str, ans)))
        
    #State: The loop processes all test cases, and for each test case, it prints a string `s` of length `n` consisting of lowercase Latin letters a-z, which is derived from the trace `a`. The state of the variables `i`, `l`, `array`, `alp`, `rev_array`, and `ans` are reset for each iteration of the loop, and the final output is the concatenation of all the printed strings, one for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases. Each test case includes an integer `n` and a list of integers `a`. For each test case, the function prints a string `s` of length `n` consisting of lowercase Latin letters a-z, derived from the trace provided in `a`. The function does not return any value; it only prints the results. After processing all test cases, the function concludes, and the state of the program is reset for the next function call.

