#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, p_i is a list of four non-negative integers representing the counts of 1s, 2s, 3s, and 4s in the initial sequence, where 0 ≤ p_i[0] + p_i[1] + p_i[2] + p_i[3] ≤ 200.
def func():
    for _ in range(int(input())):
        p = list(map(lambda x: int(x) - int(x) % 2, input().split()))
        
        print((sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2)
        
    #State: `t` is a positive integer such that \(1 \leq t \leq 10^4\) and \(t = \text{initial\_t} - n\), `p` is a list of integers where each element is the largest even number less than or equal to the corresponding input integer, the input is processed and converted into a list of integers where each element is the largest even number less than or equal to the corresponding input integer, and the loop has executed `n` times, where `n` is the total number of test cases provided.
#Overall this is what the function does:The function processes a series of test cases, where for each test case, it takes a list of four integers (representing counts of 1s, 2s, 3s, and 4s) and computes a value based on specific conditions. It prints a result for each test case, indicating whether the sum of the odd counts of 1s, 2s, and 3s equals 3 and adding half the sum of all elements in the list. The function effectively reduces the count of test cases and updates the internal state by processing each input list and printing the computed value.

