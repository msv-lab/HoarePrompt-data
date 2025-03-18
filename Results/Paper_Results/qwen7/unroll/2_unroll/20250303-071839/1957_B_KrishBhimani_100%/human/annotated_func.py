#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n and k are positive integers such that 1 ≤ n ≤ 2 \cdot 10^5 and 1 ≤ k ≤ 10^9; the sum of all n over all test cases does not exceed 2 \cdot 10^5.
def func():
    for _ in range(int(input())):
        l1 = input().split()
        
        n, k = list(map(int, l1))
        
        if n == 1:
            print(k)
        else:
            arr = []
            k0 = k
            i = 0
            ans = []
            temp = 1
            while True:
                if temp * 2 < k:
                    temp *= 2
                    i += 1
                else:
                    break
            ans.append((1 << i) - 1)
            ans.append(k - sum(ans))
            ans += [0] * (n - len(ans))
            print(*ans)
        
    #State: Output State: t test cases are processed, and for each test case, two numbers are printed. The first number is a power of 2 (or 0 if n is 1), and the second number is the remaining value after subtracting the first number from k. If n is greater than 2, the remaining positions in the list are filled with 0.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads two integers \( n \) and \( k \). If \( n \) is 1, it prints \( k \). Otherwise, it calculates two numbers: a power of 2 (or 0 if \( n \) is 1) and the remaining value after subtracting this power of 2 from \( k \). It then fills the rest of the list with zeros up to length \( n \) and prints these values. The function implicitly takes the number of test cases \( t \) as input through user input, and outputs the results for each test case.

