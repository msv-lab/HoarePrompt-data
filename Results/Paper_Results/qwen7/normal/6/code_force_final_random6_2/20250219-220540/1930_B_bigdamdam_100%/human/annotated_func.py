#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 3 ≤ n ≤ 10^5. Additionally, the sum of all n values across all test cases does not exceed 10^5.
def func():
    for i in range(int(input())):
        n = [int(i) for i in input().split()][0]
        
        p = [0] * n
        
        ind = n
        
        for i in range(0, n, 2):
            p[i] = ind
            ind -= 2
        
        ind = 1 + n % 2
        
        for i in range(1, n, 2):
            p[i] = ind
            ind += 2
        
        print(*p)
        
    #State: `ind` is `n + 1`; `i` is `n - 1`; `p` is a list where every even index is filled with the value `1 + 2 * ((index - 1) // 2)` and every odd index is filled with the value `1 + 2 * ((index) // 2)` if `index` is less than `n` and `0` otherwise.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \). It constructs a list \( p \) of length \( n \), where every even index is filled with the value \( 1 + 2 \times \left(\frac{\text{index} - 1}{2}\right) \) and every odd index is filled with the value \( 1 + 2 \times \left(\frac{\text{index}}{2}\right) \) if the index is less than \( n \) and 0 otherwise. After processing all test cases, it prints the list \( p \) for each test case.

