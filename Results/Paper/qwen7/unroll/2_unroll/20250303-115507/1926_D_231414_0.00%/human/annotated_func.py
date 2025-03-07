#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and the list of integers a contains n non-negative integers where 0 ≤ a_j < 2^{31} for all 1 ≤ j ≤ n; the sum of all n over all test cases in a test does not exceed 2 \cdot 10^5.
def func():
    times = int(input())
    check = 2 ** 31 - 1
    for _ in range(times):
        n = int(input())
        
        data = list(map(int, input().split()))
        
        dic = dict()
        
        ans = n
        
        check = 2 ** 31 - 1
        
        for i in data:
            s = i ^ check
            if s in dic:
                dic[s] -= 1
                ans -= 1
                if dic[s] == 0:
                    del dic[s]
            elif i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
            print(ans)
        
    #State: Output State: `check` is 2147483647, `times` is 0.
    #
    #Explanation: The loop runs `times` number of times, and each iteration updates the `check` variable to `2 ** 31 - 1`, which is 2147483647. After all iterations, `times` will be reduced to 0 because it decreases by 1 in each iteration. The `check` variable remains unchanged as it is reset to 2147483647 at the start of each iteration.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer \( t \) (number of test cases), an integer \( n \) (size of the list), and a list of \( n \) non-negative integers. It then iterates through the list, using bitwise XOR operations to count unique elements. The function prints the count of unique elements for each test case. After processing all test cases, it outputs the final value of `check` (which is always set to \( 2^{31} - 1 \)) and `times` (which is reduced to 0 after all iterations).

