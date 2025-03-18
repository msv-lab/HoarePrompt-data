#State of the program right berfore the function call: The function is expected to handle multiple test cases. Each test case includes a single integer n (2 ≤ n ≤ 10) representing the size of the grid, followed by n lines each containing n characters ('0' or '1'). The grid contains exactly one triangle or one square that includes all the '1's, and the shape's size is greater than 1.
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
        
    #State: `a` is greater than or equal to 0, `i` is equal to `a`, and `k` is a list containing the count of '1' characters in each input string `b` where `b` contains at least one '1'. The length of `k` is equal to the number of input strings `b` that contained '1' characters. If the first element of `k` is equal to the second element of `k`, the program retains this state.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads an integer `n` (2 ≤ n ≤ 10) representing the size of a grid, followed by `n` lines of `n` characters ('0' or '1'). It counts the number of '1's in each line that contains at least one '1' and stores these counts in a list `k`. If the first and second elements of `k` are equal, it prints the list `k`. The function does not return any value.

