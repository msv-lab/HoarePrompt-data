pa = 0
for i in raw_input():
    pa += i == "1"
pb = 0
for i in raw_input():
    pb += i == "1"

print ["NO", "YES"][pa >= pb]
