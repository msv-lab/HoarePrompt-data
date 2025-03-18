#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100. For each test case, n and m are positive integers such that 1 ≤ n ≤ m ≤ 2 ⋅ 10^5, and the sum of m over all test cases does not exceed 2 ⋅ 10^5. a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ 10^9 for all i.
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
        
    #State: Output State: The output state will consist of a series of integers printed as the result of the loop's execution for each test case. Each integer represents the calculated value of `ans` for that specific test case based on the given conditions and operations within the loop. The values of `ans` are determined by sorting lists `a` and `c`, comparing elements from opposite ends of these sorted lists, and summing up the maximum absolute differences until all elements are processed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads two lists of integers, `a` and `c`. If both lists contain identical unique elements, it prints 0 and continues to the next test case. Otherwise, it sorts `a` in ascending order and `c` in descending order. It then iterates through the elements of both lists, calculating the maximum absolute difference between corresponding elements from the two lists, and accumulates these differences. Finally, it prints the total accumulated value for each test case.

