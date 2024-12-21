def func_1():
    import sys
    input = sys.stdin.read
    (x, y, z) = map(float, input().split())
    expressions = [(x ** y ** z, 'x^y^z'), (x ** z ** y, 'x^z^y'), ((x ** y) ** z, '(x^y)^z'), ((x ** z) ** y, '(x^z)^y'), (y ** x ** z, 'y^x^z'), (y ** z ** x, 'y^z^x'), ((y ** x) ** z, '(y^x)^z'), ((y ** z) ** x, '(y^z)^x'), (z ** x ** y, 'z^x^y'), (z ** y ** x, 'z^y^x'), ((z ** x) ** y, '(z^x)^y'), ((z ** y) ** x, '(z^y)^x')]
    (max_value, max_expr) = max(expressions, key=lambda pair: pair[0])
    print(max_expr)
if __name__ == '__main__':
    func_1()