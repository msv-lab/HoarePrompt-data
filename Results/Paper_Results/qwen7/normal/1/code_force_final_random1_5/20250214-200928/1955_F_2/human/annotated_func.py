#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, p_i is a list of four non-negative integers representing the counts of 1s, 2s, 3s, and 4s in the initial sequence, respectively, such that 0 ≤ p_i ≤ 200.
def func():
    for _ in range(int(input())):
        p = list(map(lambda x: int(x) - int(x) % 2, input().split()))
        
        print((sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2)
        
    #State: t is a positive integer such that \(1 \leq t \leq 10^4\); `p` is a list of integers where each element is the nearest even number to the corresponding input integer, and the loop has executed for all provided test cases.
#Overall this is what the function does:The function processes multiple test cases, each defined by a positive integer \( t \) and a list \( p \) containing four integers representing the counts of 1s, 2s, 3s, and 4s in the initial sequence. For each test case, it calculates and prints the sum of half the total count of elements in the initial sequence plus one if exactly three of the first three elements in \( p \) are odd, otherwise zero. After processing all test cases, the function concludes without returning any value.

