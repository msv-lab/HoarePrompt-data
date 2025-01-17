#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100. For each test case, n and m are integers satisfying 1 ≤ n ≤ m ≤ 2 × 10^5, and the sum of m over all test cases does not exceed 2 × 10^5. a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ 10^9 for all i.
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
        
    #State of the program after the  for loop has been executed: `t` is the number of test cases, `diff` is the sum of the maximum absolute differences for all pairs `(a[i], b[i])` for all valid `i` in the range from 0 to `n-1`, `a` is a sorted list of integers, `b` is a sorted list of integers in descending order, and `diff` is printed after processing all test cases.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads integers \(n\) and \(m\), followed by two lists of integers \(a_i\) and \(b_i\). It then sorts list \(a\) in ascending order and list \(b\) in descending order. For each pair \((a[i], b[i])\) within the range of \(n\), it calculates the maximum absolute difference and accumulates these values into a variable `diff`. After processing all test cases, it prints the accumulated value of `diff` for each test case. The function handles the input constraints for \(t\), \(n\), \(m\), \(a_i\), and \(b_i\) as specified, ensuring that the sum of \(m\) over all test cases does not exceed \(2 \times 10^5\).

