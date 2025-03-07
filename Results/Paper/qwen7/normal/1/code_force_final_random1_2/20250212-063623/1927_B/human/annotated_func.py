#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and the trace is a list of n integers a_1, a_2, ..., a_n where 0 ≤ a_i < n.
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
        
    #State: Output State: After the loop executes all its iterations, `i` will be equal to the number of test cases provided by `int(input())`, `j` will be equal to `l` for each test case, `ans` will be a list of characters from the `alp` list. For each index `j` from 0 to `l-1` for all test cases, the character added to `ans` is the one whose index in `alp` is equal to the number of times `rev_array[j]` appears in the substring of `rev_array` starting from `j` to the end of `rev_array`, minus 1. `array` will be a list of integers obtained by splitting the input and converting each element to an integer for each test case, and `rev_array` will be the reversed version of `array` for each test case.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `t` indicating the number of test cases, an integer `n`, and a list of `n` integers `trace`. It then reverses the list of integers and constructs a new list `ans` by mapping each integer in the reversed list to a corresponding character from a predefined alphabet list `alp`. Finally, it prints the characters in `ans` concatenated together as a string. The function does not return any value but modifies and prints the output based on the input provided.

