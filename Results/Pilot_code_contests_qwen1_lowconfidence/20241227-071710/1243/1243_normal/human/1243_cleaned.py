line = stdin.readline()
array = line.split('/')
str = ''
for word in array:
    if word != '':
        str = str + '/' + word.strip()
stdout.write(str)