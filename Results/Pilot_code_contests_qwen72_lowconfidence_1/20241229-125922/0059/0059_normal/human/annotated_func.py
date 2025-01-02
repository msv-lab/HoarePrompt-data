#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 30, and for each of the n teams, hi and ai are distinct integers where 1 ≤ hi, ai ≤ 100, representing the colors of the home and guest uniforms, respectively.
def func():
    n = input()
    dom, vyezd = Counter(), Counter()
    for i in range(n):
        a, b = map(int, raw_input().split())
        
        dom[a] += 1
        
        vyezd[b] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ n ≤ 30, `dom` is a Counter object with counts of each `a` value read from input, `vyezd` is a Counter object with counts of each `b` value read from input, `hi` and `ai` are distinct integers for each of the n teams, where 1 ≤ hi, ai ≤ 100, and the total number of entries in `dom` and `vyezd` combined is `n`.
    otv = 0
    for i in dom:
        otv += vyezd[i]
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ n ≤ 30, `dom` is a Counter object with counts of each `a` value read from input, `vyezd` is a Counter object with counts of each `b` value read from input, `hi` and `ai` are distinct integers for each of the n teams, where 1 ≤ hi, ai ≤ 100, the total number of entries in `dom` and `vyezd` combined is `n`, `otv` is the sum of `vyezd[i]` for all keys `i` in `dom`.
    print(otv)
#Overall this is what the function does:The function reads the number of teams `n` (where 2 ≤ n ≤ 30) and then reads `n` pairs of integers representing the home and away uniform colors for each team. It ensures that the home and away uniform colors are distinct integers within the range 1 to 100. The function calculates the total number of conflicts, where a conflict occurs when the home uniform color of one team matches the away uniform color of another team. The final state of the program is that the total number of conflicts (`otv`) is printed. The function does not return any value. If the input values do not meet the specified constraints (e.g., `n` is out of range, or `hi` and `ai` are not distinct), the behavior of the function is undefined and may lead to incorrect results.

