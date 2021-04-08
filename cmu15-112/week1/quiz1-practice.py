#1 code tracing

# 3 0.8 6

# B C D G

# 1 3 5 4 8 9 6

# 6 14 6

#2
def isFactor(f, n):
    if (f == 0 or n == 0):
        return not (f == 0 and n != 0)
    else:
        return max(f, n) % min(f, n) == 0

def testIsFactor():
    print("Testing isFactor()...", end="")
    assert(isFactor(2, 2))
    assert(isFactor(2, 4))
    assert(not isFactor(2, 5))
    assert(not isFactor(0, 6))
    assert(isFactor(6, 0))
    assert(isFactor(0, 0))
    assert(isFactor(-2, 4))
    print("Passed!")

testIsFactor()

#3
def kthDigit(n, k):
    n = abs(n)
    before = int(n / 10 ** (k + 1)) * 10 ** (k + 1)
    x = int(n / 10 ** k) * 10 ** k
    if (x == 0):
        return 0
    after = n % x
    return (n - before - after) / 10 ** k
        
def testKthDigit():
    print("Testing kthDigit()...", end="")
    assert(kthDigit(0,0) == 0)
    assert(kthDigit(789, 0) == 9)
    assert(kthDigit(789, 1) == 8)
    assert(kthDigit(789, 2) == 7)
    assert(kthDigit(789, 3) == 0)
    assert(kthDigit(-1234, 3) == 1)
    assert(kthDigit(-3, 1) == 0)
    print("Passed!")

testKthDigit()

#4
def isAlmostInteger(n):
    return round(n) - 0.0001 <= n <= round(n) + 0.0001

def testIsAlmostInteger():
    print("Testing isAlmostInteger()...", end="")
    assert(isAlmostInteger(5) == True)
    assert(isAlmostInteger(5.0001) == True)
    assert(isAlmostInteger(4.9999) == True)
    assert(isAlmostInteger(5.00011) == False)
    assert(isAlmostInteger(4.99989) == False)
    assert(isAlmostInteger(-4.9999) == True)
    assert(isAlmostInteger(-5.00011) == False)
    print("Passed.")

testIsAlmostInteger()

#5
import math

def isPerfectSquare(n):
    return n >= 0 and math.sqrt(n) % 1 == 0

def testIsPerfectSquare():
    print("Testing isPerfectSquare...", end="")
    assert(isPerfectSquare(16) == True)
    assert(isPerfectSquare(32) == False)
    assert(isPerfectSquare(0) == True)
    assert(isPerfectSquare(15) == False)
    assert(isPerfectSquare(-16) == False)
    print("Passed!")

testIsPerfectSquare()

#6
import math

def fabricExcess(fabricInches):
    if (fabricInches == 0 or fabricInches % 36 == 0):
        return 0
    else:
        return 36 - fabricInches % 36

def almostEqual(d1, d2):
    epsilon = 0.00001
    return abs(d1-d2) <= epsilon

def testFabricExcess():
    print("Testing fabricExcess()...", end="")
    assert(fabricExcess(0) == 0)
    assert(fabricExcess(1) == 35)
    assert(fabricExcess(35) == 1)
    assert(fabricExcess(36) == 0)
    assert(fabricExcess(37) == 35)
    # use almostEqual when comparing floats
    assert(almostEqual(fabricExcess(35.5), 0.5))
    assert(almostEqual(fabricExcess(36.5), 35.5))
    print("Passed.")

testFabricExcess()

#7
def distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def triangleArea(x1, y1, x2, y2, x3, y3):
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x1, y1, x3, y3)
    s = 0.5 * (a + b + c)
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def almostEqual(d1, d2):
    epsilon = 0.00001
    return abs(d1-d2) <= epsilon

def testTriangleArea():
    print("Testing triangleArea...", end="")
    assert(almostEqual(triangleArea(0, 0, 0, 2, 2, 0), 2.0))
    assert(almostEqual(triangleArea(0, 0, 4, 0, 2, 6), 12.0))
    assert(almostEqual(triangleArea(0, 0, -4, 0, -2, -6), 12.0))
    print("Passed!")

testTriangleArea()
