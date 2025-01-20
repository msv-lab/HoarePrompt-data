#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10000, k is an integer such that 1 ≤ k ≤ 100, and the list a is a list of k integers where each a_i satisfies 1 ≤ a_i ≤ 10000 and the sum of all a_i's is less than or equal to 8*n.
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
        
    #State of the program after the  for loop has been executed: `groups` is an empty list, `soldiers` is not used as the variable is only declared within the loop, `total_pairs_needed` is the sum of `(soldiers + 1) // 2` for each element in the original `groups`.
    if (total_pairs_needed <= max_pairs_per_row) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`groups` is an empty list, `soldiers` is not used as the variable is only declared within the loop. If `total_pairs_needed` is less than or equal to `max_pairs_per_row`, no specific action is taken (implied). If `total_pairs_needed` is greater than `max_pairs_per_row`, 'NO' is printed to the console.
#Overall this is what the function does:The function reads input from standard input, processes a list of integers representing groups of soldiers, and determines whether the total number of pairs needed, where each pair consists of at least one soldier, can fit within a maximum limit. It then prints 'YES' if the total number of pairs is less than or equal to four times the value of \( n \), otherwise it prints 'NO'. The function takes no explicit parameters but relies on values read from standard input, and returns no explicit value. After execution, the `groups` list is empty, and the program prints either 'YES' or 'NO' based on the condition. Potential edge cases include when the input does not conform to the specified constraints (e.g., invalid integers or lengths).

