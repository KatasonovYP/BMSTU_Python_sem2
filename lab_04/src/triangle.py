from math import acos, degrees, sqrt


def length(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) 


def angle(a, b, c):
    if b and c:
        cosA = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
    else:
        cosA = 1
    return degrees(acos(cosA))


def findMaxAngle(a, b, c):
    lenA = length(b, c)
    lenB = length(a, c)
    lenC = length(a, b)
    angleA = angle(lenA, lenB, lenC)
    angleB = angle(lenB, lenA, lenC)
    angleC = angle(lenC, lenA, lenB)
    return max(angleA, angleB, angleC)
