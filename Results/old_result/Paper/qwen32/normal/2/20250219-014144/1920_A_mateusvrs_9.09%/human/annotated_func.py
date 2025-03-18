#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100. Each of the following n lines contains two integers a and x where a ∈ {1, 2, 3} and 1 ≤ x ≤ 10^9. There is at least one constraint of type 1 and at least one constraint of type 2. All pairs (a, x) are distinct.
def func():
    t = int(input())
    r = []
    for _ in range(t):
        n = int(input())
        
        cx = set()
        
        ax = int(1000000000.0 + 7)
        
        bx = -1
        
        for _ in range(n):
            a, x = map(int, input().split())
            if a == 1:
                bx = max(x, bx)
            elif a == 2:
                ax = min(x, ax)
            else:
                cx.add(x)
        
        if bx >= ax:
            r.append(0)
        else:
            tmp = 0
            for i in cx:
                if i >= bx and i <= ax:
                    tmp += 1
            r.append(ax - bx + 1 - tmp)
        
    #State: t is 0; n is 0; cx is a set of unique x values from the last test case where a was 3; ax is the minimum x value from the last test case where a was 2; bx is the maximum x value from the last test case where a was 1; r is a list containing the results from all t test cases.
    print(*r, sep='\n')
    #This is printed: (nothing is printed)
#Overall this is what the function does:The function processes multiple test cases, each consisting of several constraints defined by pairs of integers `(a, x)`. It calculates and outputs a result for each test case based on the given constraints. Specifically, for each test case, it determines the number of integers within a certain range that are not explicitly listed as constraints of type 3, given the maximum constraint of type 1 and the minimum constraint of type 2.

