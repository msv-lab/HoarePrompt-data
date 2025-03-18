#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are positive integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and y = 0. The input also includes a list of x distinct integers from 1 to n representing the vertices Bessie has chosen, and the sum of x over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: The value of `count` for each test case, which is calculated based on the conditions provided in the loop. Specifically, `count` is incremented for each gap of exactly 1 between consecutive elements in the sorted list, and additionally once for the gap between the first element and 1, and between `n` and the last element of the list, if these gaps are exactly 1. The final result for each test case is printed as `count + x - 2`.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it calculates a specific value based on a given list of integers. It sorts the list and counts the number of gaps of exactly 1 between consecutive elements, and additionally counts one more gap if the gap between the smallest element in the list and 1, or between the largest element and n, is exactly 1. Finally, it prints the result for each test case, which is the count plus \(x - 2\), where \(x\) is the number of elements in the list.

