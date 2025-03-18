#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100. For each test case, n and m are integers satisfying 1 ≤ n ≤ m ≤ 2 ⋅ 10^5, and the sum of m over all test cases does not exceed 2 ⋅ 10^5. a_i and b_i are integers where 1 ≤ a_i, b_i ≤ 10^9.
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
        
    #State: Output State: The output state will consist of a series of integers, each representing the result of the operations performed within the loop for each test case. These integers are calculated based on the sorting and comparison operations between lists `a` and `c` for each test case. Specifically, the output for each test case will either be 0 (if certain conditions are met), or the sum of maximum absolute differences calculated during the sorting and comparison process.
#Overall this is what the function does:The function processes multiple test cases, each containing integers n and m, along with two lists a and c. For each test case, it first checks if both lists contain identical elements. If so, it prints 0 and moves to the next test case. Otherwise, it sorts list a in ascending order and list c in descending order. Then, it calculates the sum of the maximum absolute differences between corresponding elements of the sorted lists a and c. Finally, it prints the calculated sum for each test case.

