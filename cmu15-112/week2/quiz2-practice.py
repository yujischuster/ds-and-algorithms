import math

# 1[code tracing]
# a) o..x.
#    .ox..
#    oxo.x
#    xo.o.
#    o.o.o
#
# b) 11235


# 2)
def digit_count(n):
    if n == 0:
        return 1
    if n < 0:
        n = abs(n)
    counter = 0
    while n > 0:
        counter += 1
        n //= 10
    return counter


def test_digit_count():
    print("Testing digitCount()...", end="")
    assert(digit_count(3) == 1)
    assert(digit_count(33) == 2)
    assert(digit_count(3030) == 4)
    assert(digit_count(-3030) == 4)
    assert(digit_count(0) == 1)
    print("Passed!")

test_digit_count()


# 3)
def has_consecutive_digits(n):
    if n < 0:
        n = abs(n)
    while n > 0:
        digit1 = n % 10
        n //= 10
        digit2 = n % 10
        if digit1 == digit2:
            return True
    return False


def test_has_consecutive_digits():
    print("Testing hasConsecutiveDigits()...", end="")
    assert(has_consecutive_digits(0) == False)
    assert(has_consecutive_digits(123456789) == False)
    assert(has_consecutive_digits(1212) == False)
    assert(has_consecutive_digits(1212111212) == True)
    assert(has_consecutive_digits(33) == True)
    assert(has_consecutive_digits(-1212111212) == True)
    print("Passed!")

test_has_consecutive_digits()


# 4)
def is_perfect_number(n):
    sum1 = 0
    for i in range(1, int(n / 2 + 1)):
        if n % i == 0:
            sum1 += i
    if sum1 == n:
        return True
    return False


def nth_perfect_number(n):
    num = 5
    count = -1
    while count != n:
        num += 1
        if is_perfect_number(num):
            count += 1
    return num


def test_nth_perfect_number():
    print("Testing nthPerfectNumber()...", end="")
    assert(nth_perfect_number(0) == 6)
    assert(nth_perfect_number(1) == 28)
    assert(nth_perfect_number(2) == 496)
    # assert(nth_perfect_number(3) == 8128)
    print("Passed!")

test_nth_perfect_number()


# 5)
def gcd(x, y):
    while y > 0:
        x1 = y
        y = x % y
    return x1


def test_gcd():
    print("Testing gcd()...", end="")
    assert(gcd(3, 3) == 3)
    assert(gcd(3**6, 3**6) == 3**6)
    assert(gcd(3**6, 2**6) == 1)
    x = 3143448  # 2**3 * 3**6 * 7**2 * 11**1
    y = 1568160  # 2**5 * 3**4 * 5**1 * 11**2
    g = 7128  # 2**3 * 3**4 * 11**1
    assert(gcd(x, y) == g)
    print("Passed!")

test_gcd()


# 6)
def cosine_error(x, k):



def almost_equal(d1, d2):
    epsilon = 10 ** -8
    return abs(d1 - d2) < epsilon


def test_cosine_error():
    print("Testing cosineError()...", end="")
    assert(almost_equal(cosine_error(0, 0), abs(math.cos(0) - 1)))
    assert(almost_equal(cosine_error(1, 0), abs(math.cos(1) - 1)))
    x = 1.2
    guess = 1 - x**2/2 + x**4/(4*3*2)
    error = abs(math.cos(x) - guess)
    assert(almost_equal(cosine_error(x, 2), error))
    x = 0.75
    guess = 1 - x**2/2 + x**4/(4*3*2) - x**6/(6*5*4*3*2)
    error = abs(math.cos(x) - guess)
    assert(almost_equal(cosine_error(x, 3), error))
    print("Passed!")

test_cosine_error()