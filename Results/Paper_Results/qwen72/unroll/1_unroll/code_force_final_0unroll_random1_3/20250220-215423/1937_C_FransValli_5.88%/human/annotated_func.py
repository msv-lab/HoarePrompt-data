#State of the program right berfore the function call: The function operates in an interactive environment with a hidden permutation p of integers from 0 to n-1, where n is an integer such that 2 ≤ n ≤ 10^4. The function can make at most 3n queries to compare bitwise OR results of pairs of elements from the permutation. The number of test cases t is an integer such that 1 ≤ t ≤ 10^3, and the sum of n over all test cases does not exceed 10^4.
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
        
    #State: The loop has finished executing for all test cases. For each test case, the variables `k` and `best` have been updated to the indices of the elements in the hidden permutation `p` such that `p[k]` is the largest element and `p[best]` is the second largest element in the permutation. The final output for each test case is in the format `! k best`, where `k` and `best` are the indices of the largest and second largest elements, respectively.
#Overall this is what the function does:The function `func` interacts with an environment that has a hidden permutation `p` of integers from 0 to n-1, where n is between 2 and 10,000. It processes up to 1,000 test cases, with the total sum of n across all test cases not exceeding 10,000. For each test case, the function determines and outputs the indices of the largest and second largest elements in the permutation `p`. The final state after the function concludes is that for each test case, the indices of the largest and second largest elements have been identified and printed in the format `! k best`, where `k` is the index of the largest element and `best` is the index of the second largest element.

