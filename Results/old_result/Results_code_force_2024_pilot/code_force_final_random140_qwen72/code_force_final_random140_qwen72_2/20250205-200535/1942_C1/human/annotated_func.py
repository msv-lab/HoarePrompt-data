#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 4 ≤ n ≤ 10^9, x is an integer such that 2 ≤ x ≤ min(n, 2 · 10^5), y is an integer such that y = 0, and the second line consists of x distinct integers from 1 to n, representing the vertices Bessie has chosen.
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
            
        #State: After the loop executes all the iterations, `t` is 0, `n` is the last first integer from the input, `x` is the last second integer from the input and must be greater than or equal to 1, `y` is the last third integer from the input, `arr` is a sorted list of `x` distinct integers from 1 to `n` with an additional element `n + arr[0]` appended to it, and `ans` is `x - 2` plus the number of times the difference between consecutive elements in `arr` (from index 1 to `x`) is exactly 2.
    #State: *`t` is 0, `n` is the last first integer from the input, `x` is the last second integer from the input and must be greater than or equal to 1, `y` is the last third integer from the input, `arr` is a sorted list of `x` distinct integers from 1 to `n` with an additional element `n + arr[0]` appended to it, and `ans` is `x - 2` plus the number of times the difference between consecutive elements in `arr` (from index 1 to `x`) is exactly 2.
#Overall this is what the function does:The function reads multiple sets of inputs, where each set includes three integers `n`, `x`, and `y`, followed by a list of `x` distinct integers. For each set, it processes the list to count the number of pairs of consecutive elements (including a wrapped-around pair) that have a difference of 2, and prints this count adjusted by subtracting 2 from `x`. After processing all sets, the function terminates with `t` being 0, and the last processed values of `n`, `x`, `y`, and the modified list `arr` remaining in memory.

