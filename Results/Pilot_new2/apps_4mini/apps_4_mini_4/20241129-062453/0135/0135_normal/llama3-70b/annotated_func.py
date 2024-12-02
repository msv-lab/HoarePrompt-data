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
        
    #State of the program after the  for loop has been executed: `n` is an integer, `k` is greater than or equal to 1, `i` is `k + 1`, `seen` is a set containing all unique remainders from `n % 1` to `n % k`, and `remainder` is equal to `n % k`.
    print('Yes')
#Overall this is what the function does:The function accepts two integers, `n` and `k`, read from standard input. It checks if all remainders of `n` when divided by integers from 1 to `k` are unique. If any remainder is repeated, it prints 'No' and exits. If all remainders are unique, it prints 'Yes'. The function does not return any values.

