#State of the program right berfore the function call: n, m, k, x, and y are integers such that 1 ≤ n, m ≤ 100, 1 ≤ k ≤ 10^18, and 1 ≤ x ≤ n, 1 ≤ y ≤ m.
def func():
    n, m, k, x, y = map(int, input().split())
    max_asked = (k + (n - 1)) // (2 * n)
    min_asked = max(1, max_asked - (n - 1))
    sergei_asked = (k + x - 1) // (2 * n) + ((k + x - 1) % (2 * n) >= n - x + 1)
    print(max_asked, min_asked, sergei_asked)
#Overall this is what the function does:The function processes five integers \( n \), \( m \), \( k \), \( x \), and \( y \) with given constraints and prints three values: \( \text{max\_asked} \), \( \text{min\_asked} \), and \( \text{sergei\_asked} \). The values are calculated using the formulae: \( \text{max\_asked} = \left\lfloor \frac{k + (n - 1)}{2 \cdot n} \right\rfloor \), \( \text{min\_asked} = \max(1, \text{max\_asked} - (n - 1)) \), and \( \text{sergei\_asked} = \left\lfloor \frac{k + x - 1}{2 \cdot n} \right\rfloor + \left( \frac{k + x - 1}{2 \cdot n} \right) \mod 1 \geq \frac{n - x + 1}{2 \cdot n} \). The function reads these integers from standard input and does not return any value.

