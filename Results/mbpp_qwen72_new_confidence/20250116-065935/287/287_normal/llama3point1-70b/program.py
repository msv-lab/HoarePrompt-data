import math
def wind_chill(velocity,temp):
    if temp > 0 or velocity < 3:
        return temp
    else:
        return math.ceil(13.12 + 0.6215 * temp - 11.37 * (velocity ** 0.16) + 0.3965 * temp * (velocity ** 0.16))
