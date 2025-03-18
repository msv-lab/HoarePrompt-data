#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, and for each test case, n and k are integers satisfying 2 <= k <= n <= 2 * 10^5 with k being even.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        array = list(range(1, n + 1))
        
        answer = [1]
        
        a = [1, -1]
        
        for i in range(1, n):
            if (-1) ** i == -1:
                answer.append(array[a[-1]])
                a[-1] -= 1
            else:
                answer.append(array[a[0]])
                a[0] += 1
        
        print(*answer)
        
    #State: For each test case, the output is a sequence of numbers starting with 1, followed by alternating elements from the beginning and end of the array [1, 2, ..., n], until the entire array is traversed.
#Overall this is what the function does:For each test case, the function reads two integers \( n \) and \( k \), constructs an array from 1 to \( n \), and then generates a sequence starting with 1, followed by alternating elements from the beginning and end of the array, until the entire array is traversed. This sequence is printed for each test case.

