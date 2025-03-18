#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, f, a, and b are integers such that 1 ≤ n ≤ 2 ⋅ 10^5, 1 ≤ f, a, b ≤ 10^9. The list m contains n integers such that 1 ≤ m_i ≤ 10^9 and m_i < m_{i+1}.
def func():
    test_cases = int(input())
    for i in range(test_cases):
        feat = [int(i) for i in input().split(' ')]
        
        n = feat[0]
        
        f = feat[1]
        
        a = feat[2]
        
        b = feat[-1]
        
        arr = [int(i) for i in input().split(' ')]
        
        array2 = []
        
        for i in range(0, n):
            if i == 0:
                if arr[0] < b / a:
                    array2.append(arr[0] * a)
            elif arr[i] - arr[i - 1] < b / a:
                array2.append((arr[i] - arr[i - 1]) * a)
        
        if sum(array2) + (n - len(array2)) * b < f:
            print('Yes')
        else:
            print('No')
        
    #State: Output State: The program will execute `test_cases` number of iterations based on the input provided in each iteration. For each iteration, it will process two lines of input: the first line contains integers `n`, `f`, `a`, `b`, and additional elements for the list `m`, and the second line contains `n` integers representing the list `arr`. The program then checks if the sum of certain transformed elements in `arr` plus a base value is less than `f`. If true, it prints 'Yes', otherwise 'No'. After all iterations, the output state consists of `test_cases` lines, each containing either 'Yes' or 'No' based on the condition evaluated in each iteration.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads integers n, f, a, and b, followed by a list of n integers. It then checks if the sum of certain transformed elements in the list plus a base value is less than f. If the condition is met, it prints 'Yes'; otherwise, it prints 'No'. The function outputs 'Yes' or 'No' for each test case based on the evaluation of the condition.

