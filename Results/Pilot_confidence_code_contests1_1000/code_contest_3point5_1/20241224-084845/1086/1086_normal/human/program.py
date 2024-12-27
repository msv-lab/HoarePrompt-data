def vanya(numberOfFriends, heightOfWall, heightArray):
    if len(heightArray) == numberOfFriends:
        widthCount=0
        for i in heightArray:
            if i <= heightOfWall:
                widthCount+=1
            else:
                widthCount+=2
    return widthCount