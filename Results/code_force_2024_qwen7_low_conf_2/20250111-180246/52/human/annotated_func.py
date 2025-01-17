#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n and m are integers such that 1 ≤ n ≤ m ≤ 2 ⋅ 10^5, and the sum of m over all test cases does not exceed 2 ⋅ 10^5. a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ 10^9 for all i.
def func():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        b = list(map(int, input().split()))
        
        a.sort()
        
        b.sort(reverse=True)
        
        diff = 0
        
        for i in range(n):
            diff += max(abs(a[i] - b[i]), abs(a[i - n] - b[i - n]))
        
        print(diff)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `i` is `n-1`, `diff` is the sum of the maximum of `abs(a[i] - b[i])` and `abs(a[i - n] - b[i - n])` for all `i` from `0` to `n-1`, `a` and `b` are lists of integers where `a` is sorted in ascending order and `b` is sorted in descending order, and `diff` is printed after all iterations of the loop.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads integers \( t \), \( n \), and \( m \), followed by two lists of integers \( a \) and \( b \). It then sorts \( a \) in ascending order and \( b \) in descending order. After sorting, it calculates the sum of the maximum absolute differences between corresponding elements of \( a \) and \( b \) (considering cyclic shifts if necessary) and prints the result. The function does not return any value.

