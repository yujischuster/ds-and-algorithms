import math

def almostEqual(d1, d2):
    epsilon = 10**-8
    return (abs(d2 - d1) < epsilon)

# 1)
print("1. ", end="")

def nearestBusStop(street):
    n = street // 8 * 8
    if (street % 8 > 4):
        n += 8
    return n

def testNearestBusStop():
    print("Testing nearestBusStop()...", end="")
    assert(nearestBusStop(0) == 0)
    assert(nearestBusStop(4) == 0)
    assert(nearestBusStop(5) == 8)
    assert(nearestBusStop(12) == 8)
    assert(nearestBusStop(13) == 16)
    assert(nearestBusStop(20) == 16)
    assert(nearestBusStop(21) == 24)
    print("Passed. (Add more tests to be more sure!)")

testNearestBusStop()

# 2)
print("2. ", end="")

def setKthDigit(n, k, d):
    # set 0 before digit
    a = n - int(n / (10 ** (k + 1))) * (10 ** (k + 1))
    # set 0 after digit
    b = int(a / (10 ** k)) * (10 ** k)
    c = d * (10 ** k) 
    return n - b + c

def testSetKthDigit():
    print("Testing setKthDigit()...", end="")
    assert(setKthDigit(468, 0, 1) == 461)
    assert(setKthDigit(468, 1, 1) == 418)
    assert(setKthDigit(468, 2, 1) == 168)
    assert(setKthDigit(468, 3, 1) == 1468)
    assert(setKthDigit(572, 4, 4) == 40572)
    assert(setKthDigit(700, 5, 7) == 700700)
    assert(setKthDigit(991, 6, 2) == 2000991)
    print("Passed. (Add more tests to be more sure!)")

testSetKthDigit()

# 3)
print("3. ", end="")

def cosineZerosCount(r):
    if (r > 0):
        n = round(r / (math.pi / 2))
        if (r < n * math.pi / 2):
            return round((n - 1) / 2)
        else:
            return round((n - 1) / 2 + 1)
    else:
        n = round(r / (-math.pi / 2))
        if (r > n * -math.pi / 2):
            return round((n - 1) / 2)
        else:
            return round((n - 1) / 2 + 1)

def testCosineZerosCount():
    print("Testing cosineZerosCount()...", end="")
    assert(type(cosineZerosCount(0)) == int)
    assert(cosineZerosCount(0) == 0)
    assert(cosineZerosCount(math.pi/2 - 0.0001) == 0)
    assert(cosineZerosCount(math.pi/2 + 0.0001) == 1)
    assert(cosineZerosCount(3*math.pi/2 - 0.0001) == 1)
    assert(cosineZerosCount(3*math.pi/2 + 0.0001) == 2)
    assert(cosineZerosCount(5*math.pi/2 - 0.0001) == 2)
    assert(cosineZerosCount(5*math.pi/2 + 0.0001) == 3)
    assert(cosineZerosCount(-math.pi/2 - 0.0001) == 1) #original had a typo
    assert(cosineZerosCount(-math.pi/2 + 0.0001) == 0)
    print("Passed. (Add more tests to be more sure!)")

testCosineZerosCount()

# 4)
print("4. ", end="")

def riverCruiseUpstreamTime(totalTime, totalDistance, riverCurrent):
    speed = (totalDistance + math.sqrt(totalDistance ** 2 - 4 * totalTime ** 2 * -riverCurrent ** 2)) / (2 * totalTime)
    return 15 / (speed - riverCurrent)

def testRiverCruiseUpstreamTime():
    print("Testing riverCruiseUpstreamTime()...", end="")
    # example from the source notes:
    totalTime = 3 # hours
    totalDistance = 30 # 15km up, 15km back down
    riverCurrent = 2 # km/hour
    assert(almostEqual(riverCruiseUpstreamTime(totalTime, totalDistance, riverCurrent), 1.7888736053508778)) # 1.79 in notes
    # another simple example
    totalTime = 3 # hours
    totalDistance = 30 # 15km up, 15km back down
    riverCurrent = 0 # km/hour
    assert(almostEqual(riverCruiseUpstreamTime(totalTime, totalDistance, riverCurrent), 1.5))
    print("Passed. (Add more tests to be more sure!)")

testRiverCruiseUpstreamTime()

# 5)
print("5. ", end="")

def rectanglesOverlap(left1, top1, width1, height1, left2, top2, width2, height2):
    if (left1 > left2):
        if (abs(left1 - left2) <= height2):
            a = 1
        else:
            a = 0
    else:
        if (abs(left2 - left1) <= height1):
            a = 1
        else:
            a = 0
    if (top1 > top2):
        if (abs(top1 - top2) <= width2):
            b = 1
        else:
            b = 0
    else:
        if (abs(top2 - top1) <= width1):
            b = 1
        else:
            b = 0
    if (a == 1 and b == 1):
        return True
    else:
        return False
            
def testRectanglesOverlap():
    print("Testing rectanglesOverlap()...", end="")
    assert(type(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2)) == bool)
    assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3, 3, 1, 1) == True) 
    assert(rectanglesOverlap(1, 1, 2, 2, 3.1, 3, 1, 1) == False)
    assert(rectanglesOverlap(1, 1, 2, 2, -2, -2, 6, 6) == True)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 1.9) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 2, 0.2) == True)
    
    print("Passed. (Add more tests to be more sure!)")

testRectanglesOverlap()

# 6)
print("6. ", end="")

def lineIntersection(m1, b1, m2, b2):
    if (m1 != m2):
        return -((b2 - b1) / (m2 - m1))

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def triangleArea(s1, s2, s3):
    s = 0.5 * (s1 + s2 + s3)
    return math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

def threeLinesArea(m1, b1, m2, b2, m3, b3):
    x1 = lineIntersection(m1, b1, m2, b2)
    x2 = lineIntersection(m2, b2, m3, b3)
    x3 = lineIntersection(m1, b1, m3, b3)
    y1 = m1 * x1 + b1
    y2 = m2 * x2 + b2
    y3 = m3 * x3 + b3
    if ((x1 or x2 or x3) == None):
        return 0
    else:
        return triangleArea(distance(x1, y1, x2, y2), distance(x2, y2, x3, y3), distance(x1, y1, x3, y3))

def testLineIntersection():
    print("Testing lineIntersection()...", end="")
    assert(lineIntersection(2.5, 3, 2.5, 11) == None)
    assert(lineIntersection(25, 3, 25, 11) == None)
    # y=3x-5 and y=x+5 intersect at (5,10)
    assert(almostEqual(lineIntersection(3,-5,1,5), 5))
    # y=10x and y=-4x+35 intersect at (2.5,25)
    assert(almostEqual(lineIntersection(10,0,-4,35), 2.5))
    print("Passed. (Add more tests to be more sure!)")

def testDistance():
    print("Testing distance()...", end="")
    assert(almostEqual(distance(0, 0, 1, 1), 2**0.5))
    assert(almostEqual(distance(3, 3, -3, -3), 6*2**0.5))
    assert(almostEqual(distance(20, 20, 23, 24), 5))
    print("Passed. (Add more tests to be more sure!)")

def testTriangleArea():
    print("Testing triangleArea()...", end="")
    assert(almostEqual(triangleArea(3,4,5), 6))
    assert(almostEqual(triangleArea(2**0.5, 1, 1), 0.5))
    assert(almostEqual(triangleArea(2**0.5, 2**0.5, 2), 1))
    print("Passed. (Add more tests to be more sure!)")

def testThreeLinesArea():
    print("Testing threeLinesArea()...", end="")
    assert(almostEqual(threeLinesArea(1, 2, 3, 4, 5, 6), 0))
    assert(almostEqual(threeLinesArea(0, 7, 1, 0, -1, 2), 36))
    assert(almostEqual(threeLinesArea(0, 3, -.5, -5, 1, 3), 42.66666666666))
    assert(almostEqual(threeLinesArea(1, -5, 0, -2, 2, 2), 25))
    assert(almostEqual(threeLinesArea(0, -9.75, -6, 2.25, 1, -4.75), 21))
    print("Passed. (Add more tests to be more sure!)")

testLineIntersection()
print("   ", end="")
testDistance()
print("   ", end="")
testTriangleArea()
print("   ", end="")
testThreeLinesArea()

# 7) (Bonus)
print("7. ", end="")

def BonusFindIntRootsOfCubis(a, b, c, d):
    return None

def testBonusFindIntRootsOfCubic():
    # only test the bonus if they tried it...
    if ("findIntRootsOfCubic" not in globals()): return
    print("Testing findIntRootsOfCubic()...", end="")
    testFindIntRootsOfCubicCase(5, 1, 3,  2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    print("Passed. (Add more tests to be more sure!)")

# testBonusFindIntRootsOfCubic()
