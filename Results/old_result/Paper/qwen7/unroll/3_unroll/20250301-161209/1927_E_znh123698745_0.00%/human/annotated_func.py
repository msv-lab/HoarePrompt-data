#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n and k are integers such that 2 ≤ k ≤ n ≤ 2⋅10^5 and k is even; the sum of n for all test cases does not exceed 2⋅10^5.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        array = list(range(1, n + 1))
        
        answer = [1]
        
        a = [1, -1]
        
        for i in range(1, n):
            if (-1) ** i == -1:
                answer.append(array[a[-1]])
                a[-1] -= 1
            else:
                answer.append(array[a[0]])
                a[0] += 1
        
        print(*answer)
        
    #State: Output State: t test cases are processed, and for each test case, the output is a sequence of numbers printed based on the given rules. Specifically, for each test case with n elements and starting with 1, the output sequence alternates between moving forward and backward through the array, starting with the first element, then the last, then the second, and so on, until all elements are visited. The exact sequence depends on the values of n and k but follows the described pattern.
#Overall this is what the function does:The function processes a series of test cases, each containing two integers \( n \) and \( k \). For each test case, it generates and prints a sequence of numbers based on the following rules: starting with 1, it alternates between moving forward and backward through the array of numbers from 1 to \( n \), until all elements are visited. The exact sequence depends on the values of \( n \) and \( k \) but follows the described alternating pattern.

