#State of the program right berfore the function call: n is an integer representing the number of rubles Kolya has, and a, b, and c are integers representing the cost of one plastic liter bottle, the cost of one glass liter bottle, and the money one can get back by returning an empty glass bottle, respectively.
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
        #State of the program after the if-else block has been executed: *`n`, `a`, `b`, `c`, `k`, and `remaining_rubles` are integers. If `remaining_rubles` is less than `b`, the output of the print statement is `k + remaining_rubles // a`. Otherwise, the output of the print statement is `k + 1`.
    #State of the program after the if-else block has been executed: *`n`, `a`, `b`, `c`, and `k` are integers. If `a` is less than or equal to `b - c`, the value of `n // a` is printed. Otherwise, if `remaining_rubles` is less than `b`, the output of the print statement is `k + remaining_rubles // a`. Otherwise, the output of the print statement is `k + 1`.
#Overall this is what the function does:The function `func` accepts four parameters: `n`, `a`, `b`, and `c`, where `n` is an integer representing the number of rubles Kolya has, and `a`, `b`, and `c` are integers representing the cost of one plastic liter bottle, the cost of one glass liter bottle, and the money one can get back by returning an empty glass bottle, respectively. The function calculates the maximum number of liters Kolya can buy using both plastic and glass bottles, taking into account the refund for glass bottles.

If `a` is greater than `b - c`, the function calculates the number of plastic bottles Kolya can buy directly (`n // a`). If `a` is less than or equal to `b - c`, the function calculates the maximum number of liters Kolya can buy by first determining how many full sets of glass bottles and refunds he can use (`k = (n - b) // (b - c) + 1`). Then, it calculates the remaining rubles after buying these sets of glass bottles (`remaining_rubles = n - k * (b - c)`). If the remaining rubles are not enough to buy another glass bottle (`remaining_rubles < b`), the function returns the total number of liters Kolya can buy as `k + remaining_rubles // a`. Otherwise, the function returns `k + 1`.

This function handles the case where Kolya might have enough remaining rubles to buy one more plastic bottle after using the refund from the last glass bottle. The function considers all possible scenarios and provides the maximum number of liters Kolya can purchase given his rubles and the costs and refund rates of the bottles.

