#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of lists, where each inner list contains n integers (1 ≤ n ≤ 2·10^5) representing the number of stones in each pile for a test case. Each integer a_i in the inner lists satisfies 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: The loop will have finished executing, and for each test case, it will have printed either 'Alice' or 'Bob' based on the conditions described in the loop. The variables `t`, `n`, and `arr` will retain their initial values, but the variables `s` and `ans` will have been modified and reset for each test case. After the loop, `s` will be a sorted list of unique elements from the last test case, with a 0 prepended, and `ans` will be either 0 or 1, depending on the last test case's result.
#Overall this is what the function does:The function reads input from the user, processes multiple test cases, and prints 'Alice' or 'Bob' for each test case based on the number of stones in the piles. It does not return any value. For each test case, the function determines if the piles of stones can be manipulated such that Alice wins the game, and if so, it prints 'Alice'; otherwise, it prints 'Bob'. The function modifies and resets internal variables for each test case, but the input variables `t` and the list of lists are not altered.

