#State of the program right berfore the function call: x_p, y_p, x_v, y_v are non-negative integers such that 0 ≤ x_p, y_p, x_v, y_v ≤ 10^5, (x_p, y_p) ≠ (x_v, y_v), and (x_p, y_p) ≠ (0, 0) and (x_v, y_v) ≠ (0, 0).
def func():
    x_p, y_p, x_v, y_v = map(int, input().split())

polycarp_distance = max(x_p, y_p)

vasiliy_distance = max(x_v, y_v)
    if (polycarp_distance <= vasiliy_distance) :
        print('Polycarp')
    else :
        print('Vasiliy')
    #State of the program after the if-else block has been executed: *x_p, y_p, x_v, y_v are non-negative integers such that 0 ≤ x_p, y_p, x_v, y_v ≤ 10^5, (x_p, y_p) ≠ (x_v, y_v), and (x_p, y_p) ≠ (0, 0) and (x_v, y_v) ≠ (0, 0). polycarp_distance is max(x_p, y_p), and vasiliy_distance is max(x_v, y_v). If polycarp_distance is less than or equal to vasiliy_distance, the program does not print anything. If polycarp_distance is greater than vasiliy_distance, 'Vasiliy' is printed.
#Overall this is what the function does:The function `func` reads four non-negative integer values `x_p`, `y_p`, `x_v`, and `y_v` from user input, where each value is between 0 and 10^5, inclusive, and the pairs `(x_p, y_p)` and `(x_v, y_v)` are distinct and non-zero. The function calculates the maximum of `x_p` and `y_p` (referred to as `polycarp_distance`) and the maximum of `x_v` and `y_v` (referred to as `vasiliy_distance`). It then compares these two distances and prints 'Polycarp' if `polycarp_distance` is less than or equal to `vasiliy_distance`, otherwise it prints 'Vasiliy'. After the function executes, the variables `x_p`, `y_p`, `x_v`, `y_v`, `polycarp_distance`, and `vasiliy_distance` retain their final computed values, and the program has printed either 'Polycarp' or 'Vasiliy' to the console.

