#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 10000 and 1 ≤ k ≤ 100, and the sum of k integers a_i (1 ≤ a_i ≤ 10000) is less than or equal to 8·n.
def func():
    input = sys.stdin.read

data = input().split()

n = int(data[0])

k = int(data[1])

groups = list(map(int, data[2:]))

max_pairs_per_row = 4 * n

total_pairs_needed = 0
    for soldiers in groups:
        total_pairs_needed += (soldiers + 1) // 2
        
    #State of the program after the  for loop has been executed: `n` is an integer; `k` is an integer; `groups` is a list of `k` integers where each integer is between 1 and 10000 inclusive; `max_pairs_per_row` is 4 * `n`; `total_pairs_needed` is `T + sum((soldier + 1) // 2 for soldier in groups)`; `soldiers` is the last element of the `groups` list (i.e., `groups[-1]` if `groups` has more than one element).
    if (total_pairs_needed <= max_pairs_per_row) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: `n` is an integer, `k` is an integer, `groups` is a list of `k` integers where each integer is between 1 and 10000 inclusive, `max_pairs_per_row` is 4 * `n`, `total_pairs_needed` is `T + sum((soldier + 1) // 2 for soldier in groups)`, and `soldiers` is the last element of the `groups` list (i.e., `groups[-1]` if `groups` has more than one element). If `total_pairs_needed` is less than or equal to `max_pairs_per_row`, no further action is taken. If `total_pairs_needed` is greater than `max_pairs_per_row`, the program continues execution according to the else part.
#Overall this is what the function does:The function accepts two integers `n` and `k` as input, where `1 ≤ n ≤ 10000` and `1 ≤ k ≤ 100`, along with a list of `k` integers `groups` representing the number of soldiers in each of `k` groups, where `1 ≤ a_i ≤ 10000`. It calculates the total number of pairs needed, which is the sum of `(soldiers + 1) // 2` for each group, and compares this total with `4 * n` (the maximum number of pairs per row). If the total number of pairs needed is less than or equal to `4 * n`, the function prints 'YES'. Otherwise, it prints 'NO'.

