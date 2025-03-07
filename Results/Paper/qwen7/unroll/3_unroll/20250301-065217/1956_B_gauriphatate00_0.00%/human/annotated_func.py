#State of the program right berfore the function call: n is an integer representing half the number of cards, and a is a list of integers where each integer is between 1 and n (inclusive), representing the integers on the cards in your hand. Each integer from 1 to n appears at most twice in the list.
def func_1(n, a):
    counter = Counter(a)
    pairs = sum(1 for count in counter.values() if count == 2)
    return min(pairs, n // 2)
    #The program returns the minimum value between the number of pairs of integers in the list `a` and half the number of cards (`n // 2`).
#Overall this is what the function does:The function accepts two parameters: `n`, representing half the number of cards, and `a`, a list of integers where each integer is between 1 and n (inclusive). It calculates the number of pairs of integers in the list `a` and returns the minimum value between this count and half the number of cards (`n // 2`).

#State of the program right berfore the function call: t is an integer representing the number of test cases, 1 ≤ t ≤ 10^4. n is an integer representing the number of cards in each player's hand, 1 ≤ n ≤ 2⋅10^5. a is a list of n integers representing the integers on the cards in your hand, where each integer from 1 through n appears at most twice in the list.
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
        
    #State: idx is 2 + t * (1 + n), t is an input integer, data is a list of strings, n is an integer representing the number of cards in each player's hand, a is a list of n integers representing the integers on the cards in your hand for each iteration, results is a list of outputs from func_1(n, a) for each iteration.
    for result in results:
        print(result)
        
    #State: idx remains 2 + t * (1 + n), t is an input integer, data is a list of strings, n is an integer representing the number of cards in each player's hand, a is a list of n integers representing the integers on the cards in your hand for each iteration, results is a list of outputs from func_1(n, a) for each iteration, and the console prints each element in the results list.
#Overall this is what the function does:The function processes multiple test cases, where each test case involves a list of integers representing the numbers on cards in a player's hand. For each test case, it calls `func_1(n, a)` to compute a result based on the given list `a` and the number of cards `n`. After processing all test cases, it prints the results of each test case.

