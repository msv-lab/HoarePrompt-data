#State of the program right berfore the function call: Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). Each of the following t lines contains one integer n (1 ≤ n ≤ 10^9) which represents the length of the array a.
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
        
    #State: For each test case, the output will be the largest power of 2 that is less than or equal to the given integer n. If n is 1, the output will be 1.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n`. For each test case, it outputs the largest power of 2 that is less than or equal to `n`. If `n` is 1, it outputs 1.

