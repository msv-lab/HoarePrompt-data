#State of the program right berfore the function call: The function `func` is expected to take input from the standard input, where the first line contains a single integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each test case starts with a single integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, followed by a line containing n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the initial number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        s = set()
        
        for i in range(n):
            s.add(arr[i])
        
        s = list(s)
        
        s.sort()
        
        s = [0] + s
        
        ans = 1
        
        n = len(s)
        
        if n == 2:
            print('Alice')
        else:
            for i in range(1, n - 1):
                if s[i] - s[i - 1] > 1:
                    break
                else:
                    ans ^= 1
            if ans:
                print('Alice')
            else:
                print('Bob')
        
    #State: `t` is 0, `n` is the length of `s`, `i` is `n-1`, `arr` is a list of integers provided by the user, `s` is a sorted list containing all unique elements of `arr` in ascending order, with an additional 0 at the beginning, and `ans` is 1 if the loop completed without breaking (indicating that the differences between all pairs of consecutive elements in `s` from index 1 to `n-2` are at most 1) or 0 if the loop broke (indicating that there was at least one difference greater than 1).
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. Each test case consists of the number of piles and the initial number of stones in each pile. For each test case, it determines and prints whether Alice or Bob wins a game based on the uniqueness and consecutive differences of the stone counts. Specifically, if the stone counts in the piles are all unique and the differences between consecutive stone counts (excluding the initial 0) are at most 1, Alice wins; otherwise, Bob wins. The function does not return any values. After processing all test cases, the function concludes, and the state of the program reflects the results printed for each test case.

