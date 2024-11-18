def func_1(n):
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if 0 <= n <= 9:
        return ones[n]
    elif 11 <= n <= 19:
        return teens[n - 10]
    elif 10 <= n <= 99:
        if n % 10 == 0:
            return tens[n // 10]
        else:
            return tens[n // 10] + '-' + ones[n % 10]
if __name__ == '__main__':
    s = int(input())
    print(func_1(s))