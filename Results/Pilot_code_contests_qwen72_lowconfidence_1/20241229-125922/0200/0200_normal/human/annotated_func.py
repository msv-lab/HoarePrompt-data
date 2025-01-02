#State of the program right berfore the function call: n is an integer where 1 ≤ n ≤ 200000, and a is a list of n integers where 1 ≤ ai ≤ 10^9.
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    sm = 0
    m = dict()
    ans = 0
    for i in range(n - 1, -1, -1):
        cnt = 0
        
        diff = 0
        
        if a[i] in m:
            cnt += m[a[i]]
            diff += a[i] * m[a[i]]
        
        if a[i] + 1 in m:
            cnt += m[a[i] + 1]
            diff += (a[i] + 1) * m[a[i] + 1]
        
        if a[i] - 1 in m:
            cnt += m[a[i] - 1]
            diff += (a[i] - 1) * m[a[i] - 1]
        
        ans += sm - diff - a[i] * (n - i - 1 - cnt)
        
        sm += a[i]
        
        if a[i] in m:
            m[a[i]] += 1
        else:
            m[a[i]] = 1
        
    #State of the program after the  for loop has been executed: `n` is an input integer where 1 ≤ n ≤ 200000, `a` is a list of `n` integers where 1 ≤ ai ≤ 10^9, `sm` is the sum of all elements in `a`, `m` is a dictionary where each key is an element from `a` and the value is the count of occurrences of that element in `a`, `ans` is the result of the computation based on the loop logic, and `i` is -1.
    print(ans)
#Overall this is what the function does:The function `func` reads an integer `n` and a list `a` of `n` integers from the standard input. It then processes the list `a` to compute a specific value `ans`. This value is calculated by iterating over the list in reverse order, keeping track of the sum of elements seen so far (`sm`), and using a dictionary `m` to count occurrences of each element and its neighbors (element ± 1). The final computed value `ans` is printed to the standard output. The function does not return any value; it only prints the result. The state after the function execution is: `n` remains unchanged, `a` remains unchanged, `sm` is the sum of all elements in `a`, `m` contains the counts of each element in `a`, and `ans` is the computed result.

