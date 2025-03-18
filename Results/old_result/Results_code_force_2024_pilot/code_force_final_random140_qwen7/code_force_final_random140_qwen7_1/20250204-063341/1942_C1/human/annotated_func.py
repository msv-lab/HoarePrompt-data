#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and y = 0; the vertices Bessie has chosen are represented by x distinct integers from 1 to n; the sum of x over all test cases does not exceed 2⋅10^5.
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
            
        #State: Output State: After all iterations of the loop have finished, `i` will be `x + 1`, `x` will remain the same as it was initially, and `ans` will be the initial value of `x - 2` plus the number of times the condition `arr[i] - arr[i - 1] == 2` was true during the loop's execution.
        #
        #In simpler terms, after the loop has completed all its iterations, the variable `i` will be one more than `x`, `x` will stay the same as it was at the start, and `ans` will reflect the initial count of `x - 2` plus any additional increments due to the condition `arr[i] - arr[i - 1]` being exactly 2 throughout the loop's execution.
    #State: `i` will be `x + 1`, `x` will remain the same as it was initially, and `ans` will be the initial value of `x - 2` plus the number of times the condition `arr[i] - arr[i - 1] == 2` was true during the loop's execution.
#Overall this is what the function does:The function processes a series of test cases, where for each test case, it reads integers \( n \), \( x \), and \( y \) (with specific constraints), and a list of \( x \) distinct integers representing vertices. It then calculates and prints the number of gaps of size 2 between consecutive elements in the sorted list of vertices, starting from the first element and wrapping around to the last element. The function returns nothing but prints the result for each test case.

