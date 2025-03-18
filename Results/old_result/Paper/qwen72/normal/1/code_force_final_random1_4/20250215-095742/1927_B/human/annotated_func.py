#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case consists of an integer n where 1 ≤ n ≤ 2·10^5, and a list of n integers a_1, a_2, ..., a_n where 0 ≤ a_i < n, representing the trace of the string. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `i` is `t-1`, `l` is an input integer, `array` is a list of integers provided by the user input, `alp` is a list containing the lowercase English alphabet letters from 'a' to 'z', `rev_array` is the reversed version of `array`, `ans` is a list containing the letters corresponding to the counts of each element in `rev_array` starting from index `j` (which ranges from 0 to `l-1`) in the `alp` list, `j` is `l`.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and a list of `n` integers. It then computes a string based on the counts of elements in the reversed list and maps these counts to corresponding letters from the alphabet. The function prints the resulting string for each test case. After processing all test cases, the function completes without returning any value. The final state includes the printed results for each test case, and the input variables are no longer needed.

