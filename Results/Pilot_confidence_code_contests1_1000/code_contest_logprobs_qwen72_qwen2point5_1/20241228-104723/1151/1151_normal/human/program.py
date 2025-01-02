while 1:
    input = raw_input()
    output = ""

    for i in input:
        if i.islower():
            output += i.upper()
        elif i.isupper():
            output += i.lower()
    
    print(output)