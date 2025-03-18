#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n and k are integers where 1 ≤ n, k ≤ 2 · 10^5, representing the length of the array a and the number of operations, respectively. a is a list of n integers where -10^9 ≤ a_i ≤ 10^9, representing the array a. The sum of the values of n and k over all test cases does not exceed 2 · 10^5.
def func():
    t = int(input())
    for j in range(t):
        b = input().split()
        
        n = int(b[0])
        
        k = int(b[1])
        
        l = list(map(int, input().split()))
        
        suf = []
        
        suf.append(0)
        
        for i in range(n):
            suf.append(suf[i] + l[i])
        
        smin = [0]
        
        for i in range(n):
            if suf[i + 1] < smin[i]:
                smin.append(suf[i + 1])
            else:
                smin.append(smin[i])
        
        sm = -111
        
        for i in range(n + 1):
            if suf[i] - smin[i] > sm or sm == -111:
                sm = suf[i] - smin[i]
        
        sm = 2 ** k * sm - sm
        
        sm += suf[n]
        
        if sm < 0:
            a = abs(sm) // (10 ** 9 + 7)
            sm += (a + 1) * (10 ** 9 + 7)
        else:
            sm = sm % (10 ** 9 + 7)
        
        print(sm)
        
    #State: After the loop executes all iterations, `j` is equal to `t`, `b` is the last list of strings obtained from the user input split by whitespace, `n` is the integer value of the first element in the last `b`, `k` is the integer value of the second element in the last `b`, `l` is the last list of integers obtained from the user input split by whitespace, `suf` is a list containing `n + 1` elements starting with 0 and followed by the cumulative sums of the elements in the last `l`, `i` is `n`, `smin` is a list of length `n + 1` where each element is the minimum cumulative sum up to that index in the last `suf`, and `sm` is the final computed value after applying the given operations, which is printed out. All other variables remain unchanged as they were before the loop started.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. Each test case consists of two integers `n` and `k`, and a list of `n` integers `a`. The function computes a specific value `sm` for each test case based on the cumulative sums of the elements in `a` and the operations defined by `k`. The final value of `sm` is adjusted to ensure it is non-negative and then printed modulo \(10^9 + 7\). The function does not return any value; instead, it prints the result for each test case. After processing all test cases, the function terminates.

