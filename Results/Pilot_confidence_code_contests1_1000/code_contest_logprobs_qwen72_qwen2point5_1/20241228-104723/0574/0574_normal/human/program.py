#Codeforces Contest Problems 1281 A Suffix Three

limit = int(input())

for x in range(limit):
    text = raw_input()

    if "po" in text:
        print ("FILIPINO")
    elif "masu" in text:
        print ("JAPANESE")
    elif "desu" in text:
        print ("JAPANESE")
    else:
        print ("KOREAN")
