#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, n and m are integers for each test case such that 1 ≤ n ≤ m ≤ 2 · 10^5, a_i is a list of n integers where 1 ≤ a_i ≤ 10^9, and b_i is a list of m integers where 1 ≤ b_i ≤ 10^9. The sum of m over all test cases does not exceed 2 · 10^5.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 100, n and m are integers for each test case such that 1 ≤ n ≤ m ≤ 2 · 10^5, a_i is a list of n integers where 1 ≤ a_i ≤ 10^9, and b_i is a list of m integers where 1 ≤ b_i ≤ 10^9. The sum of m over all test cases does not exceed 2 · 10^5. The loop has processed all test cases and printed the required output for each test case. The lists a and c are sorted (a in ascending order and c in descending order) for each test case, and the indices i and j are updated accordingly during the loop execution. The variable ans is the accumulated maximum absolute difference for each test case and is reset to 0 for the next test case.
#Overall this is what the function does:The function processes multiple test cases, each containing two lists of integers `a` and `c` with lengths `n` and `m` respectively. For each test case, it calculates and prints the minimum number of operations required to make all elements in `a` equal by either increasing or decreasing elements in `a` using elements from `c`. If all elements in `a` and `c` are already equal, it prints `0`. The function does not return any value but prints the result for each test case. After processing all test cases, the function concludes.

