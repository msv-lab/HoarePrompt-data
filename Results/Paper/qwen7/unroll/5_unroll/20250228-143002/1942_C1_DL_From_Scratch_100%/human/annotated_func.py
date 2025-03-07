#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and y = 0. The sum of x over all test cases does not exceed 2⋅10^5. The input consists of t test cases, where for each test case, the first line contains n, x, and y, followed by a second line containing x distinct integers from 1 to n representing the chosen vertices.
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
        
    #State: Output State: The value of `count` for each test case, which represents the number of gaps of size 1 between consecutive elements in the sorted list, plus `x - 2`.
#Overall this is what the function does:The function processes up to 10,000 test cases. For each test case, it reads three integers \( n \), \( x \), and \( y \), and a list of \( x \) distinct integers from 1 to \( n \). It then calculates the number of gaps of size 1 between consecutive elements in the sorted list of integers and adds \( x - 2 \) to this count. Finally, it prints the result for each test case.

