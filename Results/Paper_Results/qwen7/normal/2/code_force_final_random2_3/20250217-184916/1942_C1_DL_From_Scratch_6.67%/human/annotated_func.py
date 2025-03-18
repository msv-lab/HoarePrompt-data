#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and y = 0. Additionally, the sum of x over all test cases does not exceed 2⋅10^5. The first line of each test case contains three integers n, x, and y. The second line of each test case contains x distinct integers from 1 to n, representing the vertices Bessie has chosen.
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
        
        num = n - list0[-1]
        
        if num == 1:
            count += 1
        
        print(count + x - 2)
        
    #State: All test cases have been processed, `T` is 0, `i` is `x - 1`, `count` is the total number of times `num` equals 1 during the loop's execution for all test cases plus the number of test cases (`T`), `num` is `n - list0[-1]` for the last test case, and `list0` is sorted for each test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of three integers \( n \), \( x \), and \( y \), followed by \( x \) distinct integers from 1 to \( n \). It calculates the number of gaps of size 1 between consecutive integers in the list and adds the number of such gaps to the count of test cases minus one. Finally, it prints the result for each test case.

