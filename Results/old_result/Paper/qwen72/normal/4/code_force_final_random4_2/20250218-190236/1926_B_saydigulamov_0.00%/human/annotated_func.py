#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases. Each test case includes an integer `n` (2 ≤ n ≤ 10) representing the size of the grid, and a list of `n` strings, each string containing `n` characters (either '0' or '1'). The grid contains exactly one triangle or one square, and the shape cannot consist of exactly one '1'.
def func():
    a = int(input())
    for i in range(a):
        k = []
        
        for _ in range(int(input())):
            b = input()
            if '1' in b:
                k.append(b.count('1'))
        
        if k[0] == k[1]:
            print(k)
        
    #State: `a` is 0, `i` is `a` (which is 0), `k` is a list containing the count of '1' characters for each input string `b` that contains at least one '1' from all iterations, and the length of `k` is equal to the number of input strings that contained at least one '1' across all iterations. If the first element of `k` is equal to the second element of `k`, then this relationship holds true.
#Overall this is what the function does:The function `func` reads an integer `a` from the input, which represents the number of test cases. For each test case, it reads an integer `n` (2 ≤ n ≤ 10) and then reads `n` strings, each containing `n` characters ('0' or '1'). It counts the number of '1' characters in each string that contains at least one '1' and stores these counts in a list `k`. If the first and second elements of `k` are equal, it prints the list `k`. The function does not return any value. After the function concludes, `a` is 0, `i` is `a` (which is 0), and `k` is a list containing the counts of '1' characters for each input string that contained at least one '1' across all iterations.

