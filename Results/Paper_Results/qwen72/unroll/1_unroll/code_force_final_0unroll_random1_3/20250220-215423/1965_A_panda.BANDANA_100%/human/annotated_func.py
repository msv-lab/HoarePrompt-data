#State of the program right berfore the function call: The function `func` is expected to take input through standard input (stdin) and provide output through standard output (stdout). The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each test case starts with an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, followed by a line containing n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        l = map(int, input().split())
        
        lis = sorted(set(l))
        
        if 1 not in lis or len(lis) == 1:
            print('Alice')
        else:
            test = True
            for j in range(1, len(lis)):
                if lis[j] - lis[j - 1] > 1:
                    if j % 2 == 1:
                        print('Bob')
                    else:
                        print('Alice')
                    test = False
                    break
            if test == True:
                if len(lis) % 2 == 1:
                    print('Alice')
                else:
                    print('Bob')
        
    #State: The loop has finished executing all iterations, and the output for each test case has been printed to stdout as either 'Alice' or 'Bob' based on the conditions specified in the loop. The variables `t`, `n`, `l`, `lis`, `i`, and `j` are no longer in use and do not retain any specific values after the loop completes.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input, where each test case consists of an integer `n` representing the number of piles and a list of `n` integers representing the number of stones in each pile. It processes each test case and prints the result to standard output as either 'Alice' or 'Bob' based on the conditions specified in the function. Specifically, 'Alice' is printed if the list of unique pile sizes does not contain 1 or if the list has only one unique pile size. Otherwise, 'Bob' or 'Alice' is printed depending on the parity of the index of the first pair of consecutive pile sizes that differ by more than 1, or the parity of the total number of unique pile sizes if no such pair exists. After processing all test cases, the function completes and the output for each test case has been printed to stdout.

