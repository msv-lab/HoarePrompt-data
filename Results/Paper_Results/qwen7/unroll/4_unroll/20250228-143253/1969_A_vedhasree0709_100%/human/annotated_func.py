#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 2 ≤ n ≤ 50, and p is a list of n integers where 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 2 ≤ n ≤ 50, and after executing the loop, if there exists an index `i` such that `l[i]` is equal to `i + 1`, the output will be `2` and the loop will break. Otherwise, the output will be `3`.
#Overall this is what the function does:The function processes a series of test cases, each defined by an integer \( t \) (number of test cases), an integer \( n \) (size of the permutation list), and a list \( p \) of length \( n \) containing distinct integers from 1 to \( n \) excluding the index itself. For each test case, it checks if there exists an index \( i \) such that \( p[i] \) equals \( i + 1 \). If such an index is found, it outputs 2; otherwise, it outputs 3. The function does not return any value but prints the result for each test case.

