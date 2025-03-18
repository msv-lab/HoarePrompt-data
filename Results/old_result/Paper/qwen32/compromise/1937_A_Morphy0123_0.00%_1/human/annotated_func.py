#State of the program right berfore the function call: The function receives an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, it receives an integer n (1 ≤ n ≤ 10^9) which is the length of the array a. Initially, the array a is defined such that a_i = i for each 1 ≤ i ≤ n. The function should perform the swap operation for each i from 2 to n in order and find the position j such that a_j = 1 after all operations.
def func():
    n_cases = int(input())
    for i in range(n_cases):
        n = int(input())
        
        if n == 1:
            print(1)
        else:
            power = 1
            while power < log2(n):
                power += 1
            if power == n:
                print(2 ** power)
            else:
                power -= 1
                print(2 ** power)
        
    #State: `i` is equal to `n_cases`, and all test cases have been processed and their corresponding outputs have been printed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it receives an integer `n` and determines the highest power of 2 that is less than or equal to `n`. It then prints this power of 2. If `n` is a power of 2, it prints `n` itself.

