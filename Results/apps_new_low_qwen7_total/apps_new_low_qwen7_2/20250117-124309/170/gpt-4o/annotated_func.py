#State of the program right berfore the function call: n is a non-negative integer representing the number of rubles Kolya has, and a, b, and c are positive integers representing the cost of a plastic liter bottle, the cost of a glass liter bottle, and the amount of money Kolya gets back for returning an empty glass bottle, respectively, with the condition that 1 ≤ n ≤ 10^18, 1 ≤ a ≤ 10^18, 1 ≤ c < b ≤ 10^18.
def func():
    n = int(input())

a = int(input())

b = int(input())

c = int(input())
    if (a <= b - c) :
        print(n // a)
    else :
        k = (n - b) // (b - c) + 1

remaining_rubles = n - k * (b - c)
        if (remaining_rubles < b) :
            print(k + remaining_rubles // a)
        else :
            print(k + 1)
        #State of the program after the if-else block has been executed: *`n` is `n - remaining_rubles`, `remaining_rubles` is `n - k * (b - c)`, `k` is `(n - b) // (b - c) + 1`, `a` is `a`, `b` is `b`, `c` is `c`. If `remaining_rubles < b`, the function prints `k`. Otherwise, the function prints `k + 1`.
    #State of the program after the if-else block has been executed: *`n` is the value of the first input, `a` is the value of the second input, `b` is the value of the third input, `c` is the value of the fourth input. If `a <= b - c`, the function prints `n // a`. Otherwise, `remaining_rubles` is calculated as `n - k * (b - c)`, where `k` is `(n - b) // (b - c) + 1`. If `remaining_rubles < b`, the function prints `k`. Otherwise, the function prints `k + 1`.
#Overall this is what the function does:The function accepts four parameters: `n` (the number of rubles Kolya has), `a` (the cost of a plastic liter bottle), `b` (the cost of a glass liter bottle), and `c` (the amount of money Kolya gets back for returning an empty glass bottle). It calculates and returns the maximum number of liters of water Kolya can buy. Specifically, the function determines whether it is more cost-effective for Kolya to buy plastic bottles or to buy glass bottles and return them for refunds. If buying plastic bottles directly is cheaper (`a <= b - c`), the function returns the number of plastic bottles Kolya can buy. Otherwise, it calculates the number of glass bottles Kolya can initially buy and return, and then adds the additional plastic bottles he can buy with the refunded money. The function handles all possible values within the given constraints (1 ≤ n ≤ 10^18, 1 ≤ a ≤ 10^18, 1 ≤ c < b ≤ 10^18). Edge cases such as when `n` is very large or when `a`, `b`, and `c` have extreme values are also considered.

