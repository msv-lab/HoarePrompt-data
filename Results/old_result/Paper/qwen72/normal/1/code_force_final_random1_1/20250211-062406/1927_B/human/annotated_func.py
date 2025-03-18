#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case consists of an integer n (1 ≤ n ≤ 2 · 10^5) and a list of n integers a_1, a_2, ..., a_n (0 ≤ a_i < n), representing the trace of the string. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 2 · 10^5, `a` is a list of n integers where 0 ≤ a_i < n, `l` is an integer greater than or equal to 0, `array` is a list of integers read from the input, `alp` is a list containing the lowercase English alphabet letters from 'a' to 'z', `rev_array` is the reversed version of `array`, `ans` is a list containing `l` elements, each element being the character from `alp` indexed by the count of `rev_array[j]` in `rev_array[j:]` minus 1, `i` is `t`, `j` is `l-1`.
#Overall this is what the function does:The function `func` processes a series of test cases. It reads the number of test cases `t` from the input, and for each test case, it reads an integer `n` and a list of `n` integers. It then constructs a string based on the reversed list of integers and the English alphabet, printing the resulting string for each test case. The function does not return any value; instead, it prints the results directly. After processing all test cases, the function completes its execution.

