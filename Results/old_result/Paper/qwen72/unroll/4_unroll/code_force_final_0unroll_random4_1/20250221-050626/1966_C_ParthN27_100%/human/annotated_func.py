#State of the program right berfore the function call: The function should take two parameters: an integer t representing the number of test cases, and a list of lists, where each inner list represents a test case and contains n integers a_1, a_2, ..., a_n, with 1 ≤ t ≤ 10^4 and 1 ≤ n ≤ 2·10^5. Each integer a_i in the inner list is a positive integer such that 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2·10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        s = set()
        
        for i in range(n):
            s.add(arr[i])
        
        s = list(s)
        
        s.sort()
        
        s = [0] + s
        
        ans = 1
        
        n = len(s)
        
        if n == 2:
            print('Alice')
        else:
            for i in range(1, n - 1):
                if s[i] - s[i - 1] > 1:
                    break
                else:
                    ans ^= 1
            if ans:
                print('Alice')
            else:
                print('Bob')
        
    #State: The loop iterates through each test case, processes the list of integers, and prints 'Alice' or 'Bob' based on the conditions specified in the loop. After all iterations, the variables `t` and the list of lists remain unchanged, while the variables `n`, `arr`, `s`, and `ans` are reset to their initial states or modified as part of the loop's processing for each test case.
#Overall this is what the function does:The function reads an integer `t` from input, representing the number of test cases, and then processes each test case. For each test case, it reads an integer `n` and a list of `n` positive integers from input. It then determines and prints 'Alice' or 'Bob' based on the unique sorted values of the integers. If the list of unique values contains exactly two elements, 'Alice' is printed. Otherwise, it checks if the difference between consecutive elements is at most 1, and prints 'Alice' or 'Bob' based on the final value of a variable `ans` after processing. The function does not return any value. After processing all test cases, the input variables `t` and the list of lists remain unchanged, while other variables (`n`, `arr`, `s`, `ans`) are reset for each test case.

