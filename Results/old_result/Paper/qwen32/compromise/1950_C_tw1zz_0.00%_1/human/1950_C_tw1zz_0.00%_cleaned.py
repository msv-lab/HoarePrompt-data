for _ in range(int(input())):
    (h, m) = map(str, input().split(':'))
    (h1, m1) = ('', m)
    time = ''
    if h == '01':
        h1 = '01'
        time = 'AM'
    elif h == '02':
        h1 = '02'
        time = 'AM'
    elif h == '03':
        h1 = '03'
        time = 'AM'
    elif h == '04':
        h1 = '04'
        time = 'AM'
    elif h == '05':
        h1 = '05'
        time = 'AM'
    elif h == '06':
        h1 = '06'
        time = 'AM'
    elif h == '07':
        h1 = '07'
        time = 'AM'
    elif h == '08':
        h1 = '08'
        time = 'AM'
    elif h == '09':
        h1 = '09'
        time = 'AM'
    elif h == '10':
        h1 = '10'
        time = 'AM'
    elif h == '11':
        h1 = '11'
        time = 'AM'
    elif h == '12':
        h1 = '12'
        time = 'AM'
    elif h == '13':
        h1 = '01'
        time = 'PM'
    elif h == '14':
        h1 = '02'
        time = 'PM'
    elif h == '15':
        h1 = '03'
        time = 'PM'
    elif h == '16':
        h1 = '04'
        time = 'PM'
    elif h == '17':
        h1 = '05'
        time = 'PM'
    elif h == '18':
        h1 = '06'
        time = 'PM'
    elif h == '19':
        h1 = '07'
        time = 'PM'
    elif h == '20':
        h1 = '08'
        time = 'PM'
    elif h == '21':
        h1 = '09'
        time = 'PM'
    elif h == '22':
        h1 = '10'
        time = 'PM'
    elif h == '23':
        h1 = '11'
        time = 'PM'
    elif h == '00':
        h1 = '12'
        time = 'PM'
    print(h1, ':', m, ' ', time, sep='')