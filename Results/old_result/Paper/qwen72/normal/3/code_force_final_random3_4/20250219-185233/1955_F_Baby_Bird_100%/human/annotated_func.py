#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and each of the four integers p_i in the sequence is an integer such that 0 <= p_i <= 200.
def func():
    print('\n'.join([str(sum(3 * (x // 2) + x % 2 * (i < 3) for i, x in
    enumerate(map(int, input().split()))) // 3) for _ in range(int(input()))]))
    #This is printed: - The result of the formula for each test case is printed on a new line.
    #
    #### Detailed Calculation:
    #- For each integer \(x\) in the sequence:
    #  - If \(x\) is even, `x % 2` is 0, so the formula simplifies to:
    #    \[
    #    3 \left(\left\lfloor \frac{x}{2} \right\rfloor \right)
    #    \]
    #  - If \(x\) is odd, `x % 2` is 1, so the formula becomes:
    #    \[
    #    3 \left(\left\lfloor \frac{x}{2} \right\rfloor \right) + 1 \cdot (i < 3)
    #    \]
    #    - This means for \(i < 3\), an additional 1 is added to the sum if \(x\) is odd.
    #    - For \(i = 3\), no additional 1 is added.
    #
    #- The sum of these values for all four integers in the sequence is then divided by 3 using integer division.
    #
    #### Example Calculation:
    #- Suppose the input is:
    #  - `t = 2`
    #  - For the first test case: `p_0 = 4, p_1 = 5, p_2 = 6, p_3 = 7`
    #  - For the second test case: `p_0 = 0, p_1 = 1, p_2 = 2, p_3 = 3`
    #
    #- For the first test case:
    #  - \(p_0 = 4\): \(3 \left(\left\lfloor \frac{4}{2} \right\rfloor \right) + 0 = 3 \cdot 2 + 0 = 6\)
    #  - \(p_1 = 5\): \(3 \left(\left\lfloor \frac{5}{2} \right\rfloor \right) + 1 = 3 \cdot 2 + 1 = 7\)
    #  - \(p_2 = 6\): \(3 \left(\left\lfloor \frac{6}{2} \right\rfloor \right) + 0 = 3 \cdot 3 + 0 = 9\)
    #  - \(p_3 = 7\): \(3 \left(\left\lfloor \frac{7}{2} \right\rfloor \right) + 0 = 3 \cdot 3 + 0 = 9\)
    #  - Sum: \(6 + 7 + 9 + 9 = 31\)
    #  - Result: \(31 // 3 = 10\)
    #
    #- For the second test case:
    #  - \(p_0 = 0\): \(3 \left(\left\lfloor \frac{0}{2} \right\rfloor \right) + 0 = 3 \cdot 0 + 0 = 0\)
    #  - \(p_1 = 1\): \(3 \left(\left\lfloor \frac{1}{2} \right\rfloor \right) + 1 = 3 \cdot 0 + 1 = 1\)
    #  - \(p_2 = 2\): \(3 \left(\left\lfloor \frac{2}{2} \right\rfloor \right) + 0 = 3 \cdot 1 + 0 = 3\)
    #  - \(p_3 = 3\): \(3 \left(\left\lfloor \frac{3}{2} \right\rfloor \right) + 0 = 3 \cdot 1 + 0 = 3\)
    #  - Sum: \(0 + 1 + 3 + 3 = 7\)
    #  - Result: \(7 // 3 = 2\)
    #
    #### Final Output:
    #- The code will print the results of the formula for each test case, one result per line.
    #
    #Output:
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads a sequence of four integers `p_i` (0 <= p_i <= 200) from the input. It then calculates a value based on a formula that depends on whether each `p_i` is even or odd, and whether the index `i` is less than 3. The result of this formula for each test case is printed on a new line. The function does not return any value.

