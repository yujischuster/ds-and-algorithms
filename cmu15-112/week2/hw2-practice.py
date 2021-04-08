# 1)
def most_frequent_digit(n):
    best_count = 0
    best_digit = 0
    for x in range(10):
        m = n
        count = 0
        while m > 0:
            digit = m % 10
            m //= 10
            if x == digit:
                count += 1
        if count > best_count:
            best_count = count
            best_digit = x
    return best_digit


def test_most_frequent_digit():
    assert(most_frequent_digit(1123) == 1)
    assert(most_frequent_digit(2211) == 1)
    assert(most_frequent_digit(188822) == 8)
    assert(most_frequent_digit(100000) == 0)
    print("Problem 1: Solved!")

test_most_frequent_digit()


# 2)
def count_digit(num, digit): # counts how many instances of digit there are
    count = 0
    while num > 0:
        d = num % 10
        num //= 10
        if d == digit:
            count += 1
    return count


def is_rotation(x, y):
    for d in range(10):
        if d > 0 and count_digit(x, d) != count_digit(y, d):
            return False
    return True


def test_is_rotation():
    assert(is_rotation(600, 6))
    assert(is_rotation(2088, 828))
    assert(is_rotation(1234, 3241))
    assert(not is_rotation(1024, 24012))
    assert(not is_rotation(1001, 10000))
    print("Problem 2: Solved!")

test_is_rotation()


# 3)
def has_only_odd_digits(n):
    while n > 0:
        digit = n % 10
        n //= 10
        if digit % 2 == 0:
            return False
    return True


def test_has_only_odd_digits():
    assert(has_only_odd_digits(5))
    assert(has_only_odd_digits(79))
    assert(has_only_odd_digits(-131))
    assert(not has_only_odd_digits(435))
    assert(not has_only_odd_digits(484))
    print("Problem 3: Solved!")

test_has_only_odd_digits()


# 4)
def longest_digit_run(n):
    streak = 0
    longest_streak = 0
    temp_digit = n % 10
    best_digit = 10
    while n > 0:
        digit = n % 10
        n //= 10
        if digit == temp_digit:
            streak += 1
        else:
            streak = 1
        if streak > longest_streak or (streak == longest_streak and temp_digit < best_digit):
            longest_streak = streak
            best_digit = temp_digit
        temp_digit = digit
    return best_digit


def test_longest_digit_run():
    assert (longest_digit_run(9) == 9)
    assert(longest_digit_run(14441) == 4)
    assert(longest_digit_run(22441) == 2)
    assert(longest_digit_run(10023) == 0)
    print("Problem 4: Solved!")

test_longest_digit_run()


# 5)
def is_palindrome(n):
    while n > 10:
        right_digit = n % 10
        counter = 0
        left_digit = n
        n //= 10
        while left_digit > 9:
            left_digit //= 10
            counter += 1
        if right_digit != left_digit:
            return False
        n -= left_digit * 10 ** (counter - 1)
    return True


def is_prime(n):
    if n < 2:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


def nth_palindromic_prime(n):
    num = 0
    counter = -1
    while n != counter:
        num += 1
        if is_palindrome(num) and is_prime(num):
            counter += 1
    return num


def test_nth_palindromic_prime():
    assert(nth_palindromic_prime(0) == 2)
    assert(nth_palindromic_prime(2) == 5)
    assert(nth_palindromic_prime(10) == 313)
    assert(nth_palindromic_prime(19) == 929)
    print("Problem 5: Solved!")

test_nth_palindromic_prime()


# 6)
def is_left_truncatable_prime(n):
    num = n
    while num > 0:  # checks if there are zeros
        digit = num % 10
        if digit == 0:
            return False
        num //= 10
    while n > 0:
        if n < 2:
            return False
        for x in range(2, n):
            if n % x == 0:
                return False
        left_digit = n
        counter = 0
        while left_digit > 9:
            left_digit //= 10
            counter += 1
        n -= left_digit * 10 ** counter
    return True


def nth_left_truncatable_prime(n):
    num = 0
    counter = -1
    while n != counter:
        num += 1
        if is_left_truncatable_prime(num):
            counter += 1
    return num


def test_nth_left_truncatable_prime():
    assert(nth_left_truncatable_prime(0) == 2)
    assert(nth_left_truncatable_prime(6) == 23)
    assert(nth_left_truncatable_prime(10) == 53)
    assert(nth_left_truncatable_prime(15) == 113)
    print("Problem 6: Solved!")

test_nth_left_truncatable_prime()


# 7)
"""
def is_powerful_number(n):



def nth_powerful_number(n):
    counter = -1
    num = 0
    while counter != n:
        num += 1
        if is_powerful_number(num):
            counter += 1
    return num


def test_nth_powerful_number():
    assert(nth_powerful_number(0) == 1)
    assert (nth_powerful_number(4) == 16)
    assert (nth_powerful_number(10) == 64)
    assert (nth_powerful_number(19) == 169)
    print("Problem 9: Solved!")

test_nth_powerful_number()"""

# 8a [counting primes problems])


def pi(n):
    counter = 0
    for x in range(n + 1):
        if is_prime(x):
            counter += 1
    return counter


def test_pi():
    assert (pi(1) == 0)
    assert (pi(3) == 2)
    assert (pi(5) == 3)
    assert (pi(100) == 25)
    print("Problem 8a: Solved!")

test_pi()


# 8b)
def almost_equals(d1, d2):
    epsilon = 10 ** -8
    return abs(d1 - d2) < epsilon


def h(n):
    if n == 0:
        return 0
    num = 0
    for x in range(1, n + 1):
        num += 1 / x
    return num


def test_h():
    assert (almost_equals(h(0), 0.0))
    assert (almost_equals(h(1), 1 / 1.0))  # h(1) = 1/1
    assert (almost_equals(h(2), 1 / 1.0 + 1 / 2.0))  # h(2) = 1/1 + 1/2
    assert (almost_equals(h(3), 1 / 1.0 + 1 / 2.0 + 1 / 3.0))  # h(3) = 1/1 + 1/2 + 1/3
    print("Problem 8b: Solved!")

test_h()

# 9)


# 10)
def is_palindromic_number(n):
    


def count_digits(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count


def reverse_digit(n):
    rev_n = 0
    pow1 = count_digits(n) - 1
    while n > 0:
        digit = n % 10
        rev_n += digit * (10 ** pow1)
        n //= 10
        pow1 -= 1
    return rev_n


def is_emirps_prime(n):
    if is_prime(n) and is_prime(reverse_digit(n)):
        return True
    return False


def nth_emirps_prime(n):
    num = 0
    count = -1
    while count != n:
        num += 1
        if is_emirps_prime(num):
            count += 1
    return num


def test_nth_emirps_prime():
    assert(nth_emirps_prime(0) == 13)
    assert(nth_emirps_prime(1) == 17)
    assert(nth_emirps_prime(8) == 107)
    assert(nth_emirps_prime(9) == 113)
    print("Problem 10a: Solved!")

test_nth_emirps_prime()



