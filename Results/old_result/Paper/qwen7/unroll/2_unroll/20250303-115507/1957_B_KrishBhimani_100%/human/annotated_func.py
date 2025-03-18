#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of two integers n and k such that 1 ≤ n ≤ 2 \cdot 10^5 and 1 ≤ k ≤ 10^9, and the sum of all n values across all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: Output State: t test cases are processed, each test case outputs two integers separated by a space. For each test case, if n is 1, the output is k itself. Otherwise, the output is a list where the first number is (2^i) - 1, the second number is k minus the first number, and it is padded with zeros to make the total length equal to n.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \( n \) and \( k \). For each test case, if \( n \) is 1, it outputs \( k \) itself. Otherwise, it calculates two integers: \( (2^i) - 1 \) and \( k - ((2^i) - 1) \), where \( i \) is determined such that \( 2^i \) is just greater than or equal to \( k \). It then pads the result with zeros to ensure the output list has a length of \( n \). The function outputs these results for each test case, separated by a space.

