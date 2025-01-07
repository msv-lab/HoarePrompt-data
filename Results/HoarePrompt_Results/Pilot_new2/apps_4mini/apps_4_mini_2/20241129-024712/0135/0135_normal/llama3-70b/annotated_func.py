#State of the program right berfore the function call: n and k are integers such that 1 ≤ n, k ≤ 10^18.
def func():
    n, k = map(int, input().split())
    seen = set()
    for i in range(1, k + 1):
        remainder = n % i
        
        if remainder in seen:
            print('No')
            exit()
        
        seen.add(remainder)
        
    #State of the program after the  for loop has been executed: `n` is an integer, `k` is a positive integer, `i` is `k + 1`, `seen` is a set containing all unique remainders from `n % 1` to `n % k`, `remainder` is equal to `n % k`.
    print('Yes')
#Overall this is what the function does:The function accepts two integers `n` and `k` via user input, checks if the remainders of `n` divided by each integer from 1 to `k` are unique, and prints "No" if any remainder is repeated, or "Yes" if all remainders are unique.

