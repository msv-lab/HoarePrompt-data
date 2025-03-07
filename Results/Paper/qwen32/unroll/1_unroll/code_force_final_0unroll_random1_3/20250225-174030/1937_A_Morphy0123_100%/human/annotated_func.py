#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the following t lines contains a single integer n (1 ≤ n ≤ 10^9) representing the length of the array a.
def func():
    n_cases = int(input())
    for i in range(n_cases):
        n = int(input())
        
        if n == 1:
            print(1)
        else:
            power = 1
            n = log2(n)
            while power < n:
                power += 1
            if power == n:
                print(2 ** power)
            else:
                power -= 1
                print(2 ** power)
        
    #State: The variables `n` and `power` do not have a single final value; they take on a series of values during the loop's execution, and the loop prints a series of values based on the input values.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n`. For each `n`, it calculates the largest power of 2 that is less than or equal to `n` and prints that power of 2.

