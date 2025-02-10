#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 2 \cdot 10^5. The first line of each test case contains a binary string of length n representing the first row of the grid, and the second line contains a binary string of length n representing the second row of the grid. The sum of n over all test cases does not exceed 2 \cdot 10^5.
def func():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = input().strip()
        
        b = input().strip()
        
        ans = ''
        
        i = 0
        
        work = True
        
        while i < len(a):
            if work:
                ans += a[i]
                if i + 1 < len(a) and b[i] < a[i + 1]:
                    work = False
                elif i + 1 == len(a):
                    ans += b[i]
                    break
                else:
                    i += 1
            else:
                ans += b[i]
                i += 1
        
        print(ans)
        
        counter = 1
        
        for j in range(len(a) - 1):
            if a[j + 1] == b[j]:
                counter += 1
            if a[j + 1] == '0' and b[j] == '1':
                counter = 1
        
        print(counter)
        
    #State: Output State: The loop has completed all its iterations with `j` being equal to `len(a) - 1`, `counter` holding the maximum value it reached during the loop execution, `i` being `len(a)`, `t` is 3 (since we only consider up to the third iteration in the given states), `n` is the input integer, `a` is the input string after stripping whitespace, `b` is the new input string after stripping whitespace, `ans` is the final concatenated result based on the conditions inside the loop, and `work` is `False` if the loop terminated because `i + 1` was equal to `len(a)`, or it follows the last condition checked before the loop terminated.
    #
    #This means that after all iterations of the loop have finished, the loop will have processed all inputs `t` times, with each iteration updating the variables according to the specified logic. The final values of `j`, `counter`, `i`, `ans`, and `work` will reflect the outcome of the last iteration or the highest value `counter` reached during any iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two binary strings of equal length. For each test case, it constructs a new string `ans` by alternating characters from the two input strings based on specific conditions. After constructing `ans`, it counts the maximum consecutive occurrences of matching characters between the two input strings and prints both `ans` and the count. The function iterates through all test cases, processing each one independently.

