#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 100), n and m are positive integers (1 ≤ n ≤ m ≤ 2 × 10^5), a_i is a list of n positive integers (1 ≤ a_i ≤ 10^9), and b_i is a list of m positive integers (1 ≤ b_i ≤ 10^9). The sum of m over all test cases does not exceed 2 × 10^5.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        c = list(map(int, input().split()))
        
        if len(set(a)) == 1 and len(set(c)) == 1 and a[0] == c[0]:
            print(0)
            continue
        
        a.sort()
        
        c.sort(reverse=True)
        
        if len(a) == 1:
            print(max(abs(a[0] - max(c)), abs(a[0] - min(c))))
            continue
        
        i, j, ans = 0, 1, 0
        
        for k in range(len(a)):
            t1 = abs(a[i] - c[i])
            t2 = abs(a[len(a) - j] - c[len(c) - j])
            if t2 > t1:
                j += 1
            else:
                i += 1
            ans += max(t1, t2)
        
        print(ans)
        
    #State: The loop has completed all iterations, and for each test case, `n` and `m` are assigned the integer values from the input, `a` is a sorted list of integers read from the input, `c` is a sorted list of integers read from the input in descending order, `ans` is the sum of the maximum absolute differences (`max(t1, t2)`) for each iteration, `i` is the number of iterations where `t2 <= t1`, `j` is 1 + the number of iterations where `t2 > t1`, and `k` is `len(a) - 1`. The loop has printed the value of `ans` for each test case.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads two positive integers `n` and `m`, followed by a list `a` of `n` positive integers and a list `c` of `m` positive integers. If all elements in `a` and `c` are the same and equal, it prints `0`. Otherwise, it sorts `a` in ascending order and `c` in descending order, then calculates the sum of the maximum absolute differences between corresponding elements from the sorted lists `a` and `c`. This sum is printed for each test case. The function does not return any value; it only prints the results.

