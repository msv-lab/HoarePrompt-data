#State of the program right berfore the function call: n is an integer representing half the number of cards, and a is a list of integers where each integer is between 1 and n (inclusive), representing the integers on the cards in your hand. Each integer from 1 to n appears at most twice in the list a.
def func_1(n, a):
    counter = Counter(a)
    pairs = sum(1 for count in counter.values() if count == 2)
    return min(pairs, n // 2)
    #The program returns the minimum value between the number of elements in `counter` whose count is exactly 2 and half the number of cards (`n`).
#Overall this is what the function does:The function accepts two parameters: `n`, representing half the number of cards, and `a`, a list of integers from 1 to `n` (each appearing at most twice). It calculates the minimum value between the number of pairs (integers appearing exactly twice) in the list `a` and half the number of cards (`n`). The function returns this minimum value.

#State of the program right berfore the function call: t is an integer representing the number of test cases, 1 ≤ t ≤ 10^4; n is an integer representing the number of cards in each player's hand, 1 ≤ n ≤ 2⋅10^5; a is a list of integers representing the integers on the cards in your hand, 1 ≤ a_i ≤ n and each integer from 1 through n appears in the list a at most 2 times.
def func_2():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        
        idx += 1
        
        a = list(map(int, data[idx:idx + n]))
        
        idx += n
        
        results.append(func_1(n, a))
        
    #State: idx is 2 + 2 * t, t is unchanged, data is unchanged, n is an integer obtained from int(data[0]), a is a list of integers obtained from data starting from idx + t to idx + 2 * t, results is a list of outputs from func_1(n, a) for each iteration.
    for result in results:
        print(result)
        
    #State: idx is 2 + 2 * t, t is unchanged, data is unchanged, n is an integer obtained from int(data[0]), a is a list of integers obtained from data starting from idx + t to idx + 2 * t, results is a list of outputs from func_1(n, a) for each iteration, no change in the value of results as the loop only prints the values but does not modify them.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads the number of cards `n` and the list of card values `a`. It then calls `func_1(n, a)` to determine some outcome for each test case. After processing all test cases, it prints the results for each case. The final state includes the unchanged `idx`, `t`, and `data`, and `results` containing the outcomes from `func_1(n, a)` for each test case.

