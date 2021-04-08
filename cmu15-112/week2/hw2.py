# 1a[happy numbers])
def sum_of_squares_of_digits(n):
    num = 0
    while n > 0:
        digit = n % 10
        num += digit ** 2
        n //= 10
    return num


def test_sum_of_squares_of_digits():
    assert(sum_of_squares_of_digits(5) == 25)  # 5**2 = 25
    assert(sum_of_squares_of_digits(12) == 5)  # 1**2 + 2**2 = 1+4 = 5
    assert(sum_of_squares_of_digits(234) == 29)  # 2**2 + 3**2 + 4**2 = 4 + 9 + 16 = 29
    print("Problem 1a: Solved!")

test_sum_of_squares_of_digits()


# 1b)
def is_happy_number(n):
    if n < 1:
        return False
    while n != 1:
        n = sum_of_squares_of_digits(n)
        if n == 4:  # if 4, it always loops: 4, 16, 37, 58, 89, 145, 42, 20, 4
            return False
    return True


def test_is_happy_number():
    assert(is_happy_number(-7) == False)
    assert(is_happy_number(1) == True)
    assert(is_happy_number(2) == False)
    assert(is_happy_number(97) == True)
    assert(is_happy_number(98) == False)
    assert(is_happy_number(404) == True)
    assert(is_happy_number(405) == False)
    print("Problem 1b: Solved!")

test_is_happy_number()


# 1c)
def nth_happy_number(n):
    found = -1
    num = 0
    while found != n:
        num += 1
        if is_happy_number(num):
            found += 1
    return num


def test_nth_happy_number():
    assert(nth_happy_number(0) == 1)
    assert(nth_happy_number(1) == 7)
    assert(nth_happy_number(2) == 10)
    assert(nth_happy_number(3) == 13)
    assert(nth_happy_number(4) == 19)
    assert(nth_happy_number(5) == 23)
    assert(nth_happy_number(6) == 28)
    assert(nth_happy_number(7) == 31)
    print("Problem 1c: Solved!")

test_nth_happy_number()


# 1d)
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_factor = round(n ** 0.5)
    for i in range(3, max_factor + 1, 2):
        if n % i == 0:
            return False
    return True


def is_happy_prime(n):
    if is_happy_number(n) and is_prime(n):
        return True
    return False


def nth_happy_prime(n):
    found = -1
    num = 0
    while found != n:
        num += 1
        if is_happy_prime(num):
            found += 1
    return num


def test_nth_happy_prime():
    assert(nth_happy_prime(0) == 7)
    assert(nth_happy_prime(1) == 13)
    assert(nth_happy_prime(2) == 19)
    assert(nth_happy_prime(3) == 23)
    print("Problem 1d: Solved!")

test_nth_happy_prime()


# 2)
def is_kaprekar_number(n):
    count = 0
    num1 = n ** 2
    while num1 > 0:
        num1 //= 10
        count += 1
    right_half = n ** 2 % (10 ** int(0.5 + count / 2))
    left_half = n ** 2 // (10 ** int(0.5 + count / 2))
    if right_half + left_half == n:
        return True
    return False


def nearest_kaprekar_number(n):
    bigger = n
    smaller = n
    counter_up = 0
    counter_down = 0
    while not is_kaprekar_number(bigger):
        bigger += 1
        counter_up += 1
    while not is_kaprekar_number(smaller):
        smaller -= 1
        counter_down += 1
    if counter_up < counter_down:
        return bigger
    else:
        return smaller


def test_nearest_kaprekar_number():
    assert(nearest_kaprekar_number(8) == 9)
    assert(nearest_kaprekar_number(50) == 45)
    assert(nearest_kaprekar_number(150) == 99)
    assert(nearest_kaprekar_number(2000) == 2223)
    print("Problem 2: Solved!")

test_nearest_kaprekar_number()


# 3)
def nth_carol_prime(n):
    counter = -1
    i = 0
    while counter != n:
        i += 1
        carol = (2 ** i - 1) ** 2 - 2
        if is_prime(carol):
            counter += 1
    return carol


def test_nth_carol_prime():
    assert(nth_carol_prime(0) == 7)
    assert(nth_carol_prime(1) == 47)
    assert(nth_carol_prime(6) == 16769023)
    assert(nth_carol_prime(9) == 274876858367)
    print("Problem 3: Solved!")

test_nth_carol_prime()


# 4)
def carryless_add(x, y):
    counter = -1
    sum2 = 0
    while max(x, y) > 0:
        counter += 1
        num1 = x % 10
        num2 = y % 10
        sum1 = (num1 + num2) % 10
        sum2 += sum1 * (10 ** counter)
        x //= 10
        y //= 10
    return sum2


def test_carryless_add():
    assert(carryless_add(785, 376) == 51)
    print("Problem 4: Solved!")

test_carryless_add()


# 5)
def carryless_multiply(x, y):
    counter1 = -1
    num1 = 0
    while y > 0:
        counter1 += 1
        digit1 = y % 10
        y //= 10
        sub_x = x
        counter2 = -1
        i = 0
        while sub_x > 0:
            counter2 += 1
            digit2 = sub_x % 10
            i += digit1 * digit2 % 10 * (10 ** counter2)
            sub_x //= 10
        num2 = i * (10 ** counter1)
        result = carryless_add(num1, num2)
        num1 = num2
    return result


def test_carryless_multiply():
    assert(carryless_multiply(643, 59) == 417)
    print("Problem 5: Solved!")

test_carryless_multiply()


# 6)
def integral(f, a, b, N):
