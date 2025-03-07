#State of the program right berfore the function call: The function `func` is an interactive function that operates on multiple test cases. Each test case involves a permutation of integers from 0 to n-1, where n is an integer such that 2 ≤ n ≤ 10^4. The function can make at most 3n queries to find two indices i and j (0 ≤ i, j < n) such that the bitwise XOR of p_i and p_j is maximized. The total sum of n over all test cases does not exceed 10^4.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        k = 1
        
        for i in range(2, n):
            print('?', 0, k, 0, i, flush=True)
            res = input()
            if res == '<':
                k = i
        
        best = 0
        
        for i in range(1, n):
            print('?', k, best, k, i, flush=True)
            res = input()
            if res == '<':
                best = i
        
        print('!', k, best, flush=True)
        
    #State: The loop has finished executing for all test cases. For each test case, the function has found two indices `k` and `best` such that the bitwise XOR of `p_k` and `p_best` is maximized, and has printed these indices in the format `! k best`. The variables `n` and `k` have been updated for each test case, and `best` has been updated within each test case. The total number of queries made does not exceed 3n for any test case, and the total sum of n over all test cases does not exceed 10^4.
#Overall this is what the function does:The function `func` processes multiple test cases, each involving a permutation of integers from 0 to n-1, where 2 ≤ n ≤ 10^4. For each test case, it queries the input to find two indices `k` and `best` such that the bitwise XOR of `p_k` and `p_best` is maximized. It prints these indices in the format `! k best` after completing the necessary queries. The function ensures that the total number of queries made for each test case does not exceed 3n, and the total sum of n over all test cases does not exceed 10^4. After processing all test cases, the function concludes without returning any value.

