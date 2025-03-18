#State of the program right berfore the function call: The function operates in an environment where it can interactively query a system to compare bitwise OR results of elements from a hidden permutation of integers from 0 to n-1, and it must find a pair of indices (i, j) that maximize the bitwise XOR of the elements at those indices, using at most 3n queries. The function handles multiple test cases, each with a different permutation of size n, where 2 ≤ n ≤ 10^4, and the sum of n across all test cases does not exceed 10^4.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        mak = 0
        
        for i in range(1, n):
            print('?', mak, mak, i, i)
            sys.stdout.flush()
            if str(input()) == '<':
                mak = i
        
        mak2 = mak
        
        pans = []
        
        for i in range(n):
            print('?', mak, mak2, i, mak2)
            sys.stdout.flush()
            s = str(input())
            if s == '<':
                mak = i
                pans = [i]
            elif s == '=':
                pans.append(i)
        
        mak = 0
        
        for i in range(1, len(pans)):
            print('?', pans[mak], pans[mak], pans[i], pans[i])
            sys.stdout.flush()
            if str(input()) == '>':
                mak = i
        
        print('!', mak2, pans[mak])
        
        sys.stdout.flush()
        
    #State: _ is equal to the number of test cases minus 1, `n` is the input positive integer for the last test case, `i` is `len(pans) - 1`, `mak` is the index of the last element in `pans` for which the user input was `>`, `mak2` is the highest value of `i` for which the user input was `<`, and `pans` is a list containing all values of `i` for which the user input was `=` or `<`. The loop has completed all its iterations, and the output buffer has been flushed.
#Overall this is what the function does:The function processes multiple test cases, each involving a hidden permutation of integers from 0 to n-1. For each test case, it interacts with a system to query bitwise OR results and identifies a pair of indices (i, j) that maximize the bitwise XOR of the elements at those indices, using at most 3n queries. After processing all test cases, the function outputs the identified pairs for each test case. The final state of the program includes the completion of all test cases, with the output buffer flushed, and the indices (i, j) that maximize the bitwise XOR for each test case printed.

