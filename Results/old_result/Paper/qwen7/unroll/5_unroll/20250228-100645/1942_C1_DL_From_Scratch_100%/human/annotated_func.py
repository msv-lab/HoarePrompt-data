#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are positive integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2 ⋅ 10^5), and y = 0. The input also includes x distinct integers from 1 to n representing the vertices Bessie has chosen, and the sum of x over all test cases does not exceed 2 ⋅ 10^5.
def func():
    T = int(input())
    for _ in range(T):
        n, x, y = map(int, input().split())
        
        list0 = list(map(int, input().split()))
        
        list0 = sorted(list0)
        
        count = 0
        
        for i in range(x - 1):
            num = list0[i + 1] - list0[i] - 1
            if num == 1:
                count += 1
        
        num = list0[0] + n - list0[-1] - 1
        
        if num == 1:
            count += 1
        
        print(count + x - 2)
        
    #State: Output State: T is an integer between 1 and 10^4 inclusive. For each value of T, there are T iterations of the loop. In each iteration, n, x, y are integers, and list0 is a sorted list of integers. After processing each iteration, count is an integer representing the number of gaps of size 1 found in the list0, adjusted by the conditions involving x and y. The final output of each iteration is printed, and the sum of all these outputs forms the final state.
#Overall this is what the function does:The function processes a series of test cases, where for each test case, it reads values for n, x, and y, along with x distinct integers from 1 to n. It then calculates the number of gaps of size 1 between consecutive integers in the list, adjusts this count based on the value of x, and prints the result for each test case. The final output is the sum of these results for all test cases.

