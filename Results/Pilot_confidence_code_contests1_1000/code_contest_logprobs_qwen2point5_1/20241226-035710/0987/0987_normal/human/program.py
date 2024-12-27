while True:
    try:
        a, b, c, d, e, f = map(float, raw_input().split()) 
        x = (c*e - b*f)/(a*e - b*d)
        y = (c*d - a*f)/(b*d - a*e)
        x = round(1000*x)/1000
        y = round(1000*y)/1000
        print ("%.3f %.3f" % (x, y))
    except:
        break