#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and y = 0. The vertices Bessie has chosen are represented by x distinct integers from 1 to n, and the sum of x over all test cases does not exceed 2⋅10^5.
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
            
        #State: i is 2*t, x is at least t, ans is the count of pairs (arr[j+1] - arr[j] == 2) for j in range(x-1), t is 0.
    #State: t is 0, x is at least 2*t, ans is the count of pairs (arr[j+1] - arr[j] == 2) for j in range(x-1).
#Overall this is what the function does:The function processes multiple test cases, each involving integers t, n, x, and y. It verifies that t is a positive integer within the range 1 to 10^4, n is an integer between 4 and 10^9, x is an integer between 2 and the minimum of n or 2⋅10^5, and y is always 0. Additionally, it ensures that the sum of x across all test cases does not exceed 2⋅10^5. For each test case, it sorts a list of x integers, appends a specific value to this list, and counts the number of pairs where consecutive elements differ by 2. The function then prints this count for each test case.

