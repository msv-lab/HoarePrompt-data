def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def find_integer_solutions(a1, b1, a2, b2, L, R):
    A = a1
    B = -a2
    C = b2 - b1

    gcd, x0, y0 = gcd_extended(abs(A), abs(B))
    
    if C % gcd != 0:
        return -1
    
    x0 *= C // gcd
    y0 *= C // gcd
    
    if A < 0:
        x0 = -x0
    if B < 0:
        y0 = -y0
    
    a1_div_gcd = a1 // gcd
    a2_div_gcd = a2 // gcd
    
    def adjust_solution(x, y, a1_div_gcd, a2_div_gcd, sign_a1, sign_a2):
        if sign_a1 > 0:
            k = (L - (b1 + a1 * x)) // (a1 * a1_div_gcd)
            x += k * a2_div_gcd
            y -= k * a1_div_gcd
        else:
            k = (R - (b1 + a1 * x)) // (a1 * a1_div_gcd)
            x += k * a2_div_gcd
            y -= k * a1_div_gcd
        
        if b1 + a1 * x < L:
            x += a2_div_gcd
            y -= a1_div_gcd
        if b1 + a1 * x > R:
            x -= a2_div_gcd
            y += a1_div_gcd
        
        return x, y
    
    x0, y0 = adjust_solution(x0, y0, a1_div_gcd, a2_div_gcd, 1, -1)
    
    count = 0
    while True:
        val = a1 * x0 + b1
        if val > R:
            break
        if L <= val <= R:
            count += 1
        x0 += a2_div_gcd
        y0 -= a1_div_gcd
    
    return count

# Input
a1, b1, a2, b2, L, R = map(int, input().split())

# Output
print(find_integer_solutions(a1, b1, a2, b2, L, R))
