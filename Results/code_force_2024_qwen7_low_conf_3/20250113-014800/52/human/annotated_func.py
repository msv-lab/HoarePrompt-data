#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100. For each test case, n and m are integers satisfying 1 ≤ n ≤ m ≤ 2⋅10^5, and the sum of all m values over all test cases does not exceed 2⋅10^5. a_i and b_i are lists of integers where 1 ≤ a_i, b_i ≤ 10^9 for all i.
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
        
    #State of the program after the  for loop has been executed: `t` is an integer between 1 and 100 inclusive, `n` is a positive integer, `m` is the integer obtained from the second input split, `a` is a list of integers sorted in ascending order, `b` is a list of integers sorted in descending order, `diff` is the final sum of `max(abs(a[i] - b[i]), abs(a[i - n] - b[i - n]))` for all valid `i` values from 0 to `n-1`, the value of `diff` is printed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads two integers \( n \) and \( m \), followed by two lists of integers \( a \) and \( b \). It sorts \( a \) in ascending order and \( b \) in descending order. Then, it calculates the sum of the maximum absolute differences between corresponding elements of \( a \) and \( b \), considering the circular nature of the lists (i.e., \( a[i - n] \) and \( b[i - n] \)). Finally, it prints the computed sum for each test case. The function handles up to 100 test cases, with each test case having \( n \) and \( m \) satisfying \( 1 \leq n \leq m \leq 2 \times 10^5 \) and the total sum of all \( m \) values not exceeding \( 2 \times 10^5 \). The function ensures that all test cases are processed correctly and the results are printed accordingly. Potential edge cases include scenarios where \( n \) or \( m \) are at their respective boundaries, and the function also correctly handles the circular reference for the lists when \( i \) reaches the end of the list.

