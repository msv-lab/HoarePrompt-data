#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the following t lines contains a single integer n (1 ≤ n ≤ 10^9), which is the length of the array a.
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
        
    #State: The output state will consist of `n_cases` lines, each containing the largest power of 2 that is less than or equal to the `n` value provided for that test case. The variables `n_cases` and `t` remain unchanged as they are not modified within the loop. The variable `n` changes with each iteration as it is read from the input for each test case. The variable `power` is a temporary variable used within each iteration and does not persist after the loop.
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`. For each test case, it outputs the largest power of 2 that is less than or equal to `n`.

