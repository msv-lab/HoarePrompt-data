#State of the program right berfore the function call: n and k are integers such that 1 ≤ n, k ≤ 10^18.**
def func():
    n, k = map(int, input().split())
    seen = set()
    for i in range(1, k + 1):
        remainder = n % i
        
        if remainder in seen:
            print('No')
            exit()
        
        seen.add(remainder)
        
    #State of the program after the  for loop has been executed: `n` and `k` are integers such that 1 ≤ `n`, `k` ≤ 10^18; `seen` is a set containing unique values of `n` modulo `i` where 1 ≤ `i` ≤ `k`; `remainder` is equal to `n` modulo `i` for the last iteration; if `remainder` is already in `seen`, the program would have printed 'No' and exited during that iteration.
    print('Yes')
#Overall this is what the function does:The function `func` reads two integers `n` and `k` from input, iterates from 1 to `k`, calculates the remainder of `n` divided by `i`, and checks if this remainder has been seen before. If a repeated remainder is found, it prints 'No' and exits; otherwise, it continues adding unique remainders to a set. If the loop completes without finding a repeated remainder, it prints 'Yes'. This function does not accept any parameters and does not return any value.

