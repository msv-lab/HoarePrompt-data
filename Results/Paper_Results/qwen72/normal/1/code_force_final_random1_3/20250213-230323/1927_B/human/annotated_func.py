#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 2·10^5, representing the length of the lost string. a is a list of n integers where 0 ≤ a_i < n, representing the trace of the string. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `i` is `t-1`, `l` is an input integer greater than 0, `array` is a list of integers derived from the last input, `alp` is a list containing the lowercase English alphabet letters from 'a' to 'z', `rev_array` is the reversed version of `array`, `ans` is a list of characters where each character corresponds to the count of the respective element in `rev_array` minus 1, mapped to the alphabet, `j` is `l`.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. Each test case consists of an integer `n` followed by a list of `n` integers. The function processes each test case to generate a string based on the counts of elements in the reversed list, mapping these counts to corresponding characters from the alphabet. After processing all test cases, the function prints the resulting strings for each test case. The final state of the program includes the processed test cases being outputted, with no modifications to the initial inputs or any other global state.

