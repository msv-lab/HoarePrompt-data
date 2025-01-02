def func_1(digits):
    pair9s = {}
    for i in range(10):
        pair9s[i] = 9 - i
    baseCounts = [0] * 10
    for digit in digits:
        baseCounts[int(digit)] += 1
    iTen = -1
    mxZeros = 0
    for i in range(1, 6):
        countsa = baseCounts[:]
        countsb = baseCounts[:]
        zeros = 0
        i10 = 10 - i
        mn9s = [0] * 10
        mni10 = min(1, countsa[i], countsb[i10])
        print(dict(i=i, countsa=countsa, countsb=countsb, mxZeros=mxZeros, mni10=mni10))
        if mni10 > 0:
            countsa[i] -= 1
            countsb[i10] -= 1
            zeros = 1
            for j in range(10):
                j9 = pair9s[j]
                mn = min(countsa[j], countsb[j9])
                if mn > 0:
                    countsa[j] -= mn
                    countsb[j9] -= mn
                    zeros += mn
                    mn9s[j] = mn
        mn0 = min(countsa[0], countsb[0])
        countsa[0] -= mn0
        countsb[0] -= mn0
        zeros += mn0
        if mxZeros < zeros:
            mxZeros = zeros
            mxZString = [''] * 2
            for j in range(10):
                mxZString[0] += str(j) * countsa[j]
                mxZString[1] += str(j) * countsb[j]
            for j in range(10):
                mxZString[0] += str(j) * mn9s[j]
                mxZString[1] += str(9 - j) * mn9s[j]
            mxZString[0] += str(i) * mni10 + '0' * mn0
            mxZString[1] += str(i10) * mni10 + '0' * mn0
            print(dict(v=2, mxZString=mxZString))
    if mxZeros == 0:
        return (digits, digits)
    return tuple(mxZString)
if __name__ == '__main__':
    digits = sys.stdin.readline().strip('\n\r ')
    print('%s\n%s' % func_1(digits))