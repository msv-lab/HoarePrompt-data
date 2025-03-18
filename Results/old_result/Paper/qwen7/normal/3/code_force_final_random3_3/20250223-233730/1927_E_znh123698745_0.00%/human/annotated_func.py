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
        
    #State: Output State: After the loop executes all iterations, `answer` will be a list containing all integers from 1 to `n-1`. The exact sequence of these integers depends on the parity of `n-1` and whether `(-1) ** i` evaluates to -1 or 1 for each iteration. If `n-1` is odd, the sequence will start with the first element of `array` and alternate between decrementing and incrementing indices. If `n-1` is even, the sequence will start with the second element of `array` and follow a similar alternating pattern. The final state of `a` will be either `[1, -1]` or `[2, -1]`, depending on the last operation performed during the loop.
    #
    #In summary, `answer` will contain a permutation of the first `n-1` natural numbers, and `a` will be adjusted according to the loop's operations.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads two integers \( n \) and \( k \). It then generates a permutation of the first \( n-1 \) natural numbers based on the parity of \( n-1 \) and prints this permutation. The function does not return any value but prints the generated permutation for each test case.

