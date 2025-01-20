#State of the program right berfore the function call: n, m, min, max are integers where 1 ≤ m < n ≤ 100 and 1 ≤ min < max ≤ 100. The list of m temperatures, t_i, consists of m integers where 1 ≤ t_i ≤ 100.
def func():
    n, m, min_temp, max_temp = map(int, input().split())

temperatures = list(map(int, input().split()))

contains_min = min_temp in temperatures

contains_max = max_temp in temperatures

additional_needed = n - m
    if (contains_min and contains_max) :
        print('Correct')
    else :
        if (additional_needed >= 2 or additional_needed == 1 and (contains_min or
    contains_max)) :
            print('Correct')
        else :
            print('Incorrect')
        #State of the program after the if-else block has been executed: *`n` is an integer (1 ≤ n ≤ 100), `m` is an integer (1 ≤ m < n), `min_temp` is an integer (1 ≤ min_temp < max_temp ≤ 100), `max_temp` is an integer (1 ≤ min_temp < max_temp ≤ 100), `temperatures` is a list of `m` integers (1 ≤ t_i ≤ 100), `contains_min` is True if `min_temp` is in `temperatures` else False, `contains_max` is True if `max_temp` is in `temperatures` else False, `additional_needed` is `n - m`, and either `contains_min` is False or `contains_max` is False. If `additional_needed` is greater than or equal to 2, or if `additional_needed` is 1 and at least one of `contains_min` or `contains_max` is True, the current state remains unchanged. If `additional_needed` is less than 2 and not equal to 1, or if `additional_needed` is 1 and neither `contains_min` nor `contains_max` is True, the current state also remains unchanged.
    #State of the program after the if-else block has been executed: *`n` is an integer (1 ≤ n ≤ 100), `m` is an integer (1 ≤ m < n), `min_temp` is an integer (1 ≤ min_temp < max_temp ≤ 100), `max_temp` is an integer (1 ≤ min_temp < max_temp ≤ 100), `temperatures` is a list of `m` integers (1 ≤ t_i ≤ 100), `contains_min` is True if `min_temp` is in `temperatures` else False, `contains_max` is True if `max_temp` is in `temperatures` else False, and `additional_needed` is `n - m`. If `contains_min` and `contains_max` are both True, the state remains unchanged. If either `contains_min` or `contains_max` is False, the state remains unchanged under the following conditions: `additional_needed` is greater than or equal to 2, or if `additional_needed` is 1 and at least one of `contains_min` or `contains_max` is True. If `additional_needed` is less than 2 and not equal to 1, or if `additional_needed` is 1 and neither `contains_min` nor `contains_max` is True, the state also remains unchanged.
#Overall this is what the function does:The function reads input values for `n`, `m`, `min_temp`, `max_temp`, and a list of `m` temperatures. It checks if the `min_temp` and `max_temp` are present in the `temperatures` list. Based on whether these temperatures are present and the number of additional temperatures needed (`n - m`), it prints 'Correct' if the conditions are met, otherwise it prints 'Incorrect'. The function does not return any value; it only prints the result based on the conditions. The final state of the program includes the original inputs and the printed output, which indicates whether the conditions for `min_temp` and `max_temp` being present or the possibility of adding them are satisfied.

