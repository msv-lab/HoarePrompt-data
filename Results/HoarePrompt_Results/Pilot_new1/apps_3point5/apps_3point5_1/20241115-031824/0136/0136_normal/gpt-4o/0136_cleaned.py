input = sys.stdin.read

def func_1():
    data = input().split()
    a = data[0].lstrip('0')
    b = data[1].lstrip('0')
    if not a:
        a = '0'
    if not b:
        b = '0'
    if len(a) < len(b):
        print('<')
    elif len(a) > len(b):
        print('>')
    elif a < b:
        print('<')
    elif a > b:
        print('>')
    else:
        print('=')
func_1()