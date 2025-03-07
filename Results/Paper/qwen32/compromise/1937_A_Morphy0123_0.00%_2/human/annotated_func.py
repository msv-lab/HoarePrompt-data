#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 10^4), which is the number of test cases. Each of the following t lines contains a single integer n (1 ≤ n ≤ 10^9), representing the length of the array a.
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
        
    #State: i is equal to n_cases, n is the last input value processed, and n_cases remains unchanged. The program has printed the appropriate values for each input n.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n`. For each `n`, it prints the highest power of 2 that is less than or equal to `n`. If `n` is 1, it directly prints 1.

