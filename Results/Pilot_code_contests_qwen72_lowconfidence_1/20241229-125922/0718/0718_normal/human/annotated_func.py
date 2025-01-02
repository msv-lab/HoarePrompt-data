#State of the program right berfore the function call: C, Hr, Hb, Wr, Wb are integers such that 1 ≤ C, Hr, Hb, Wr, Wb ≤ 109.
def func():
    c, h1, h2, w1, w2 = (int(t) for t in sys.stdin.readline().split())
    g = gcd(w1, w2)
    c /= g
    w1 /= g
    w2 /= g
    res = 0
    if (c <= 10 ** 5 * w1) :
        for i in range(c / w1 + 1):
            if res < i * h1 + (c - i * w1) / w2 * h2:
                res = i * h1 + (c - i * w1) / w2 * h2
            
        #State of the program after the  for loop has been executed: `C`, `Hr`, `Hb`, `Wr`, `Wb` are integers such that \(1 \leq C, Hr, Hb, Wr, Wb \leq 10^9\). `c` is an input integer divided by `g`. `h1` is an input integer. `h2` is an input integer. `w1` is an input integer divided by `g`. `w2` is an input integer divided by `g`. `g` is gcd(`w1`, `w2`). `res` is the maximum value of the expression \(i \cdot h1 + \left( \frac{c - i \cdot w1}{w2} \right) \cdot h2\) for \(0 \leq i \leq \left\lfloor \frac{c}{w1} \right\rfloor\). The current value of `c` is less than or equal to \(10^5 \times w1\).
    else :
        if (c <= 10 ** 5 * w2) :
            for i in range(c / w2 + 1):
                if res < i * h2 + (c - i * w2) / w1 * h1:
                    res = i * h2 + (c - i * w2) / w1 * h1
                
            #State of the program after the  for loop has been executed: `C` is an integer such that \(1 \leq C \leq 10^9\), `Hr` is an integer such that \(1 \leq Hr \leq 10^9\), `Hb` is an integer such that \(1 \leq Hb \leq 10^9\), `Wr` is an integer such that \(1 \leq Wr \leq 10^9\), `Wb` is an integer such that \(1 \leq Wb \leq 10^9\), `c` is an integer such that \(10 < c \leq 10^5 \times w2\), `h1` is an input integer, `h2` is an input integer, `w1` is an input integer divided by `g`, `w2` is an input integer divided by `g`, `g` is gcd(w1, w2), `i` is \( \left\lfloor \frac{c}{w2} \right\rfloor + 1 \), `res` is the maximum value of \( i * h2 + (c - i * w2) / w1 * h1 \) for all \( i \) in the range \( 0 \) to \( \left\lfloor \frac{c}{w2} \right\rfloor \).
        else :
            if (h1 * w2 < h2 * w1) :
                h1, h2 = h2, h1
                w1, w2 = w2, w1
            #State of the program after the if block has been executed: *`C, Hr, Hb, Wr, Wb` are integers such that 1 ≤ C, Hr, Hb, Wr, Wb ≤ 109, `c` is an input integer divided by `g`, `h1` is an input integer, `h2` is an input integer, `w1` is an input integer divided by `g`, `w2` is an input integer divided by `g`, `g` is gcd(w1, w2), `res` is 0, and `c` is greater than 10. If `h1 * w2 < h2 * w1`, `w1` and `w2` are swapped, so `w1` becomes the original `w2` and `w2` becomes the original `w1`. Otherwise, `w1` and `w2` retain their original values.
            for i in range(10 ** 5):
                if res < i * h2 + (c - i * w2) / w1 * h1:
                    res = i * h2 + (c - i * w2) / w1 * h1
                
            #State of the program after the  for loop has been executed: `i` is 10^5 - 1, `res` is the maximum value of `i * h2 + (c - i * w2) / w1 * h1` for all `i` from 0 to 10^5 - 1, where `c`, `h1`, `h2`, `w1`, and `w2` are the original values, and `w1` and `w2` may have been swapped based on the initial condition.
        #State of the program after the if-else block has been executed: *C, Hr, Hb, Wr, Wb are integers such that \(1 \leq C, Hr, Hb, Wr, Wb \leq 10^9\), `c` is an integer such that \(10 < c\), `h1` is an input integer, `h2` is an input integer, `w1` is an input integer divided by `g`, `w2` is an input integer divided by `g`, `g` is gcd(w1, w2), `res` is 0, and `c` is greater than 10. If \( c \leq 10^5 \times w2 \), then `i` is \( \left\lfloor \frac{c}{w2} \right\rfloor + 1 \) and `res` is the maximum value of \( i * h2 + (c - i * w2) / w1 * h1 \) for all \( i \) in the range \( 0 \) to \( \left\lfloor \frac{c}{w2} \right\rfloor \). Otherwise, `i` is \(10^5 - 1\) and `res` is the maximum value of \( i * h2 + (c - i * w2) / w1 * h1 \) for all \( i \) from 0 to \(10^5 - 1\), where `c`, `h1`, `h2`, `w1`, and `w2` are the original values, and `w1` and `w2` may have been swapped based on the initial condition.
    #State of the program after the if-else block has been executed: C, Hr, Hb, Wr, Wb are integers such that \(1 \leq C, Hr, Hb, Wr, Wb \leq 10^9\). `c` is an input integer divided by `g`. `h1` is an input integer. `h2` is an input integer. `w1` is an input integer divided by `g`. `w2` is an input integer divided by `g`. `g` is gcd(`w1`, `w2`). `res` is 0 initially. If `c` is less than or equal to \(10^5 \times w1\), `res` is the maximum value of the expression \(i \cdot h1 + \left( \frac{c - i \cdot w1}{w2} \right) \cdot h2\) for \(0 \leq i \leq \left\lfloor \frac{c}{w1} \right\rfloor\). If `c` is greater than \(10^5 \times w1\), and if \( c \leq 10^5 \times w2 \), then `res` is the maximum value of \( i * h2 + (c - i * w2) / w1 * h1 \) for all \( i \) in the range \( 0 \) to \( \left\lfloor \frac{c}{w2} \right\rfloor \). Otherwise, if \( c > 10^5 \times w2 \), `res` is the maximum value of \( i * h2 + (c - i * w2) / w1 * h1 \) for all \( i \) from 0 to \(10^5 - 1\).
    print(res)
#Overall this is what the function does:The function `func` implicitly accepts five integer parameters `C`, `Hr`, `Hb`, `Wr`, and `Wb`, each within the range 1 to 10^9, from standard input. It calculates the greatest possible value of a linear combination of two terms, where the coefficients and constants are derived from the input parameters. Specifically, it computes the maximum value of the expression \(i \cdot h1 + \left( \frac{c - i \cdot w1}{w2} \right) \cdot h2\) or \(i \cdot h2 + \left( \frac{c - i \cdot w2}{w1} \right) \cdot h1\), depending on the conditions. The function prints this maximum value and does not return any value. The final state of the program includes the following: `C`, `Hr`, `Hb`, `Wr`, and `Wb` remain unchanged; `c`, `h1`, `h2`, `w1`, and `w2` are modified during computation but do not affect the global state outside the function; and the maximum value is printed to the console. Potential edge cases include when `c` is very large or when the division results in non-integer values, which could lead to truncation errors.

