#State of the program right berfore the function call: n and k are integers such that 1 ≤ k ≤ n ≤ 2 ⋅ 10^5. Each of the next n lines contains three integers t_i, a_i, and b_i, where 1 ≤ t_i ≤ 10^4 and 0 ≤ a_i, b_i ≤ 1.
def func():
    n, k = list(map(int, sys.stdin.readline().strip().split(' ')))
    t = []
    a = []
    b = []
    for _ in range(n):
        ti, ai, bi = list(map(int, sys.stdin.readline().strip().split(' ')))
        
        t.append(ti)
        
        a.append(ai)
        
        b.append(bi)
        
    #State of the program after the  for loop has been executed: `n` and `k` are integers read from the input, 1 ≤ k ≤ n ≤ 2 ⋅ 10^5, `t` is a list containing `n` elements where each element is an integer `ti` read from the input, `a` is a list containing `n` elements where each element is an integer `ai` read from the input, `b` is a list containing `n` elements where each element is an integer `bi` read from the input.
    alice_only = []
    alice = 0
    bob = 0
    bob_only = []
    taken = [(0) for i in range(n)]
    ts = sorted(enumerate(t), key=lambda x: x[1])
    for (i, ti) in ts:
        if a[i] and b[i]:
            if alice == k and bob == k:
                if alice_only and bob_only:
                    if ti < alice_only[-1] + bob_only[-1]:
                        taken[alice_only.pop()] = 0
                        taken[bob_only.pop()] = 0
                        taken[i] = 1
                continue
            if alice == k:
                if alice_only:
                    j = alice_only.pop()
                    taken[j] = 0
            else:
                alice += 1
            if bob == k:
                if bob_only:
                    j = bob_only.pop()
                    taken[j] = 0
            else:
                bob += 1
            taken[i] = 1
            continue
        
        if a[i] and alice < k:
            alice += 1
            alice_only.append(i)
            taken[i] = 1
        
        if b[i] and bob < k:
            bob += 1
            bob_only.append(i)
            taken[i] = 1
        
    #State of the program after the  for loop has been executed: `n` and `k` are integers with \(1 \leq k \leq n \leq 2 \cdot 10^5\), `t`, `a`, and `b` are lists containing `n` elements each. `alice` is the number of items chosen for Alice, and `bob` is the number of items chosen for Bob, both of which are at most `k`. `alice_only` is a list containing indices of items chosen exclusively for Alice, and `bob_only` is a list containing indices of items chosen exclusively for Bob. `taken` is a list of `n` integers where `taken[i]` is 1 if the item at index `i` has been chosen for either Alice or Bob, and 0 otherwise. If `alice` and `bob` are both `k`, and there are items that could potentially replace items in `alice_only` and `bob_only` to reduce the total time, such replacements have been made.
    if (alice != k or bob != k) :
        print(-1)
    else :
        ans = 0
        for (i, ti) in ts:
            if taken[i]:
                ans += ti
            
        #State of the program after the  for loop has been executed: `n` and `k` are integers with \(1 \leq k \leq n \leq 2 \cdot 10^5\), `t`, `a`, and `b` are lists containing `n` elements each, `alice` is `k`, `bob` is `k`, `alice_only` is a list containing indices of items chosen exclusively for Alice, `bob_only` is a list containing indices of items chosen exclusively for Bob, `taken` is a list of `n` integers where `taken[i]` is 1 if the item at index `i` has been chosen for either Alice or Bob, and 0 otherwise, `ans` is the sum of `ti` for all indices `i` in `ts` where `taken[i]` is 1. If `ts` is empty or no `i` in `ts` satisfies `taken[i] == 1`, `ans` remains 0.
        print(ans)
    #State of the program after the if-else block has been executed: *`n` and `k` are integers with \(1 \leq k \leq n \leq 2 \cdot 10^5\), `t`, `a`, and `b` are lists containing `n` elements each. `alice` is the number of items chosen for Alice, and `bob` is the number of items chosen for Bob, both of which are at most `k`. `alice_only` is a list containing indices of items chosen exclusively for Alice, and `bob_only` is a list containing indices of items chosen exclusively for Bob. `taken` is a list of `n` integers where `taken[i]` is 1 if the item at index `i` has been chosen for either Alice or Bob, and 0 otherwise. If `alice` is not equal to `k` or `bob` is not equal to `k`, `-1` has been printed. Otherwise, if `alice` and `bob` are both `k`, `ans` is the sum of `ti` for all indices `i` in `ts` where `taken[i]` is 1. If `ts` is empty or no `i` in `ts` satisfies `taken[i] == 1`, `ans` remains 0. The value of `ans` has been printed.
#Overall this is what the function does:The function `func` reads two integers `n` and `k` from the input, followed by `n` lines each containing three integers `t_i`, `a_i`, and `b_i`. It then processes these inputs to select up to `k` items for Alice and up to `k` items for Bob, ensuring that the total time (sum of `t_i` values) is minimized. The function prints the minimum total time if exactly `k` items can be selected for both Alice and Bob; otherwise, it prints `-1`. The function handles the following edge cases and ensures the following final state: 

- If `n` and `k` do not satisfy the constraints \(1 \leq k \leq n \leq 2 \cdot 10^5\), the behavior is undefined.
- If there are not enough items that can be selected for both Alice and Bob to reach `k` items each, the function prints `-1`.
- If there are multiple ways to select items such that both Alice and Bob get `k` items, the function ensures that the total time is minimized by replacing higher time items with lower time items when possible.
- The final state of the program includes:
  - `n` and `k` are integers with \(1 \leq k \leq n \leq 2 \cdot 10^5\).
  - `t`, `a`, and `b` are lists containing `n` elements each.
  - `alice` and `bob` are the number of items chosen for Alice and Bob, respectively, both of which are at most `k`.
  - `alice_only` and `bob_only` are lists containing indices of items chosen exclusively for Alice and Bob, respectively.
  - `taken` is a list of `n` integers where `taken[i]` is 1 if the item at index `i` has been chosen for either Alice or Bob, and 0 otherwise.
  - If `alice` is not equal to `k` or `bob` is not equal to `k`, `-1` is printed.
  - Otherwise, `ans` is the sum of `t_i` for all indices `i` in `ts` where `taken[i]` is 1, and this value is printed.

