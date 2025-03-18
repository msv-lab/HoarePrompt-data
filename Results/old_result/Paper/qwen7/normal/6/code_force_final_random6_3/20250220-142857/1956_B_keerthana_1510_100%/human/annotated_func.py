#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5; the second line of each test case contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ n and each integer from 1 through n appears in the sequence a_1, a_2, ..., a_n at most 2 times; the sum of n over all test cases does not exceed 2 ⋅ 10^5.
def func():
    for line in [*open(0)][2::2]:
        print(len((tokens := line.split())) - len({*tokens}))
        
    #State: t is an integer such that \(1 \leq t \leq 10^4\), and the loop has executed all its iterations.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer t (1 ≤ t ≤ 10^4), an integer n (1 ≤ n ≤ 2 ⋅ 10^5), and a sequence of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) such that each integer from 1 through n appears at most twice. For each test case, it calculates and prints the number of unique integers in the sequence, which is the length of the sequence minus the number of distinct integers in the sequence. After processing all test cases, it does not return any value.

