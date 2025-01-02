def compot(x, y, z):
    if (z<4) or (y<2) or (x<1):
        return 0
    else:
        delit = z / 4
        while delit >= 1:
            if ((y / delit) >= 1) and ((x / delit) >= 1):
                return delit

            else:
                delit = delit - 1

if __name__ == '__main__':
    limon = int(raw_input())
    yabl = int(raw_input())
    grush = int(raw_input())
    delit = compot(limon, yabl, grush)
    print(str(delit*7))