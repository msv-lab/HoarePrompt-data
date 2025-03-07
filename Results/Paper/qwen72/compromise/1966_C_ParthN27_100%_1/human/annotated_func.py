#State of the program right berfore the function call: The function should take two parameters: an integer t representing the number of test cases, and a list of lists, where each inner list contains the integers n and a list of integers a_1, a_2, ..., a_n representing the number of stones in each pile. t satisfies 1 ≤ t ≤ 10^4, n satisfies 1 ≤ n ≤ 2·10^5, and each a_i satisfies 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: The loop will iterate t times, and for each iteration, it will read n and a list of integers, process the list to determine if the game is won by Alice or Bob, and print the winner. After all iterations, the variables t, n, arr, s, ans, and i will be in their final states as determined by the last iteration of the loop, but the specific values will depend on the input provided for the last test case. The list s will be a sorted list of unique elements from the last arr list, with 0 prepended, and ans will be 1 if the last game is won by Alice, or 0 if won by Bob.
#Overall this is what the function does:The function reads input from the user to process multiple test cases. For each test case, it reads the number of piles `n` and a list of integers representing the number of stones in each pile. It then determines the winner of a game based on the stones in the piles and prints 'Alice' or 'Bob' accordingly. The function does not return any value; it only prints the results. After processing all test cases, the final state of the program includes the variables `t`, `n`, `arr`, `s`, `ans`, and `i` being in their respective states as determined by the last test case, but the specific values depend on the input provided for the last test case. The list `s` will be a sorted list of unique elements from the last `arr` list, with 0 prepended, and `ans` will be 1 if the last game is won by Alice, or 0 if won by Bob.

