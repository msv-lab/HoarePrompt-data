#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and 0 ≤ y ≤ n - x. Additionally, the sum of x over all test cases does not exceed 2⋅10^5, and the input consists of t test cases, where each test case is defined by three integers n, x, and y followed by x distinct integers from 1 to n representing the chosen vertices.
def func():
    tt = int(input())
    for ii in range(tt):
        n, x, y = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        ans = x + y - 2
        
        tmp = []
        
        for i in range(1, len(a)):
            if a[i] - a[i - 1] == 2:
                ans += 1
            elif (a[i] - a[i - 1]) % 2 == 0:
                tmp.append((a[i] - a[i - 1]) // 2)
        
        if a[0] + n - a[len(a) - 1] == 2:
            ans += 1
        elif (a[0] + n - a[len(a) - 1]) % 2 == 0:
            tmp.append((a[0] + n - a[len(a) - 1]) // 2)
        
        tmp.sort()
        
        for i in tmp:
            if y >= i - 1:
                ans += i
                y -= i - 1
            else:
                break
        
        ans += y
        
        print(min(ans, n - 2))
        
    #State: Output State: The output state will be the minimum value between `ans`, which is calculated based on the given logic within the loop for each test case, and `n - 2`. For each test case, the variable `ans` is updated based on the differences between consecutive elements in the sorted list `a`, and additional adjustments are made using the variables `x` and `y`. Finally, the minimum value between `ans` and `n - 2` is printed for each test case.
#Overall this is what the function does:The function processes a series of test cases, each consisting of integers n, x, and y, along with x distinct integers from 1 to n. It calculates a value `ans` based on the differences between consecutive elements in the sorted list of chosen vertices and adjusts `ans` using the values of x and y. Finally, it prints the minimum value between `ans` and `n - 2` for each test case.

