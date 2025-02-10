#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4; for each test case, n, x, and y are integers where 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2 * 10^5), and y = 0; the second line of each test case contains x distinct integers from 1 to n, representing the vertices Bessie has chosen.
def func():
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            [n, x, y] = map(int, input().split())
            
            arr = input().split()
            
            arr = [int(arr[i]) for i in range(x)]
            
            arr.sort()
            
            arr.append(n + arr[0])
            
            ans = x - 2
            
            for i in range(1, x + 1):
                if arr[i] - arr[i - 1] == 2:
                    ans += 1
            
            print(ans)
            
        #State: `t` is 0, `n` is the last input integer from the last iteration, `x` is the last second integer from the last iteration, `y` is the last third integer from the last iteration, `arr` is a sorted list of the last `x` distinct integers from 1 to `n`, with an additional element `n + arr[0]` appended to it, `i` is `x + 1`, and `ans` is the initial value `x - 2` plus the number of times the difference between consecutive elements in `arr` is 2 for the last iteration.
    #State: *If the program is executed as the main module, `t` is 0, `n` is the last input integer from the last iteration, `x` is the last second integer from the last iteration, `y` is the last third integer from the last iteration, `arr` is a sorted list of the last `x` distinct integers from 1 to `n`, with an additional element `n + arr[0]` appended to it, `i` is `x + 1`, and `ans` is the initial value `x - 2` plus the number of times the difference between consecutive elements in `arr` is 2 for the last iteration. If the program is not executed as the main module, the variables remain unchanged.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. Each test case consists of three integers `n`, `x`, and `y`, followed by a list of `x` distinct integers. The function processes each test case by sorting the list of integers, appending `n + arr[0]` to the list, and calculating the number of pairs of consecutive elements in the list that have a difference of 2. It then prints the result for each test case. After processing all test cases, the function leaves `t` as 0, and the last processed values of `n`, `x`, `y`, `arr`, and `ans` reflect the state of the last test case.

