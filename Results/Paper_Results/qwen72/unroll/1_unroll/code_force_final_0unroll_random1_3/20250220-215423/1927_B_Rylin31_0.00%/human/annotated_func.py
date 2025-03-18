#State of the program right berfore the function call: The function should take two parameters: an integer t (1 \le t \le 10^4) representing the number of test cases, and a list of lists, where each inner list contains the trace of a string s of length n (1 \le n \le 2 \cdot 10^5), with each trace element a_i (0 \le a_i < n) being a non-negative integer. The sum of n over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: The function will print the transformed string for each test case, and the variables `i`, `l`, `array`, `alp`, `rev_array`, and `ans` will be reset for each iteration of the outer loop. After all iterations, the final state of these variables will be their initial state for the last test case, with `i` being equal to `t` (the number of test cases).
#Overall this is what the function does:The function `func` reads input from the user to process multiple test cases. For each test case, it reads an integer `l` and a list of integers `array`. It then generates a string `ans` by mapping each element in `array` to a corresponding character from a predefined alphabet list `alp`, based on the count of that element in the reversed `array`. The function prints the generated string for each test case. After processing all test cases, the function does not return any value, but the variables `i`, `l`, `array`, `alp`, `rev_array`, and `ans` are reset for each test case, and `i` will be equal to `t` (the number of test cases) at the end.

