#State of the program right berfore the function call: N and H are integers where 1 ≤ N ≤ 10^5 and 1 ≤ H ≤ 10^9. There are N pairs of integers (a_i, b_i) where 1 ≤ a_i ≤ b_i ≤ 10^9, representing the damage dealt by wielding and throwing each katana, respectively.
def func():
    n, h = [int(e) for e in raw_input().split()]
    kl = []
    for i in range(0, n):
        a, b = [int(e) for e in raw_input().split()]
        
        kl.append((b, 0))
        
        kl.append((a, 1))
        
    #State of the program after the  for loop has been executed: `n` is an integer within the range 1 ≤ `n` ≤ 10^5, `h` is an integer within the range 1 ≤ `h` ≤ 10^9, there are `n` pairs of integers (a_i, b_i) where 1 ≤ a_i ≤ b_i ≤ 10^9, `kl` is a list containing 2 * `n` tuples, each pair (a_i, b_i) contributes two tuples `(b_i, 0)` and `(a_i, 1)` to the list, `i` is `n - 1`.
    kl.sort(reverse=True)
    n = 0
    i = 0
    while h > 0:
        k = kl[i]
        
        if k[1] == 0:
            h -= k[0]
            i += 1
            n += 1
        else:
            n = n + (h + k[0] - 1) / k[0]
            break
        
    #State of the program after the loop has been executed: `n` is the final count of processed elements, `h` is reduced to 0 or a non-positive integer, `kl` remains the same list of tuples as initially, `i` is the index of the last processed element in `kl` plus one, if the loop breaks due to `k[1] == 1`, `n` is updated to `n + (h + k[0] - 1) / k[0]` and `i` is the index of the tuple where `k[1] == 1`.
    sys.stdout.write('%d\n' % n)
    sys.stdout.flush()
#Overall this is what the function does:The function `func` reads input values for `n` and `h`, where `n` is the number of katanas and `h` is the initial health of a monster. It then reads `n` pairs of integers `(a_i, b_i)` representing the damage dealt by wielding and throwing each katana, respectively. The function constructs a list `kl` containing tuples `(b_i, 0)` and `(a_i, 1)` for each katana, sorts this list in descending order of damage, and processes the list to determine the minimum number of katanas required to reduce the monster's health to 0 or less. If the damage is dealt by throwing a katana (`k[1] == 0`), the health `h` is reduced by the damage value, and the count `n` of used katanas is incremented. If the damage is dealt by wielding a katana (`k[1] == 1`), the function calculates the remaining number of katanas needed to finish the monster and updates `n` accordingly. Finally, the function prints the total number of katanas used and flushes the output buffer. The function does not return any value but outputs the result directly. Edge cases include scenarios where the initial health `h` is already 0 or negative, or when the damage from the first katana in the sorted list is sufficient to defeat the monster. Missing functionality includes handling invalid input (e.g., non-integer inputs or out-of-range values).

