import sys
input = sys.stdin.read

def compare_large_numbers():
    data = input().split()
    a = data[0].lstrip('0')
    b = data[1].lstrip('0')
    
    # If both a and b become empty after stripping leading zeros, they are zero
    if not a:
        a = '0'
    if not b:
        b = '0'
    
    if len(a) < len(b):
        print('<')
    elif len(a) > len(b):
        print('>')
    else:
        if a < b:
            print('<')
        elif a > b:
            print('>')
        else:
            print('=')

compare_large_numbers()
