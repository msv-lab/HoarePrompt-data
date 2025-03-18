#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 2 ≤ n ≤ 50, and p is a list of n integers where each p_i is an integer such that 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        i = 0
        
        j = 0
        
        while i <= n - 1:
            p = l[i]
            q = l[p - 1]
            if q == i + 1:
                print(2)
                j = 1
                break
            i += 1
        
        if j == 0:
            print(3)
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 2 ≤ n ≤ 50, and after executing the loop, if there exists an index \(i\) such that \(l[i] = i+1\), the loop prints 2 and breaks, otherwise it prints 3.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \(n\) and a list \(p\) of \(n\) integers. For each test case, it checks if there exists an index \(i\) such that \(p[i] = i + 1\). If such an index is found, it prints 2 and breaks out of the loop. If no such index exists after checking all elements, it prints 3. The function does not return any value but outputs the result for each test case.

