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
        
    #State of the program after the  for loop has been executed: `n` is an input integer where 1 ≤ n ≤ 10^18, `k` is an input integer where 1 ≤ k ≤ 10^18, `i` is equal to `k`, `remainder` is equal to `n % k`, `seen` contains the unique remainders of `n % i` for all `i` from 1 to `k` without any duplicates.
    print('Yes')
#Overall this is what the function does:The function accepts two integers `n` and `k`, checks for duplicates among the remainders of `n` when divided by each integer from 1 to `k`, prints 'No' if a duplicate is found, and prints 'Yes' if all remainders are unique.

