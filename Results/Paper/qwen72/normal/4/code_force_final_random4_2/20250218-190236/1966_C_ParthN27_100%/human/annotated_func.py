#State of the program right berfore the function call: The function should take two parameters: an integer t representing the number of test cases, and a list of lists, where each inner list contains integers a_1, a_2, ..., a_n representing the number of stones in each pile for a test case. t satisfies 1 ≤ t ≤ 10^4, and for each test case, n satisfies 1 ≤ n ≤ 2·10^5, and each a_i satisfies 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: `t` is a positive integer (1 ≤ t ≤ 10^4), `n` is the length of `s`, `arr` is a list of integers provided by the user, `s` is a sorted list containing all unique elements from `arr` for each test case, with an additional 0 at the beginning, and `ans` is 1 or 0 depending on the parity of the number of consecutive elements in `s` (from index 1 to `n-1`) where the difference is exactly 1. If `n` is 2, the output is 'Alice'. If `n` is greater than 2, the output is 'Alice' if there is at least one consecutive pair of elements in `s` (from index 1 to `n-1`) where the difference is 1, or the loop did not break early due to a difference greater than 1. If `ans` is 0, the output is 'Bob', indicating there are no consecutive pairs of elements in `s` (from index 1 to `n-1`) where the difference is 1, and the loop did break early due to a difference greater than 1.
#Overall this is what the function does:The function `func` reads input from the user, processes multiple test cases, and prints the winner of a game ('Alice' or 'Bob') for each test case. Each test case involves a list of integers representing the number of stones in each pile. The function determines the winner based on the unique, sorted values of the stones in each pile, with an additional 0 prepended to the list. If the list of unique stones has only two elements, 'Alice' wins. Otherwise, the function checks if there is at least one consecutive pair of elements (excluding the first element, which is 0) where the difference is exactly 1. If such a pair exists, 'Alice' wins; otherwise, 'Bob' wins. The function does not return any value, but it prints the result for each test case.

