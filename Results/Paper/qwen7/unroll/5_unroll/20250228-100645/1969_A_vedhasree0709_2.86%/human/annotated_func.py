#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 2 ≤ n ≤ 50, and p is a list of n integers where 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        i = 0
        
        j = 0
        
        while i <= n - 1:
            if l[i] == i + 2 and l[i + 1] == i + 1:
                print(2)
                j = 1
                break
            i += 1
        
        if j == 0:
            print(3)
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 2 ≤ n ≤ 50, and after executing the loop, the output consists of either '2' or '3' printed for each test case based on the conditions inside the loop. If there exists an index `i` where `l[i] == i + 2` and `l[i + 1] == i + 1`, then '2' is printed; otherwise, '3' is printed.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer \( n \) and a list \( l \) of length \( n \). For each test case, it checks if there exists an index \( i \) such that \( l[i] = i + 2 \) and \( l[i + 1] = i + 1 \). If such an index exists, it prints '2'; otherwise, it prints '3'. The function does not return any value but prints the result for each test case.

