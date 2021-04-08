# 1)
def most_frequent_digit(n):
    best_count = 0
    best_digit = 0
    for i in range(10):
        m = n 
        count = 0
        while m > 0:
            digit = m % 10
            m //= 10
            if i == digit:
                count += 1
        if count > best_count:
            best_count = count
            best_digit = i
    return best_digit
        

def test_most_frequent_digit():
    assert(most_frequent_digit(1123) == 1)
    assert(most_frequent_digit(2211) == 1)
    assert(most_frequent_digit(188822) == 8)
    assert(most_frequent_digit(100000) == 0)
    print("Problem 1: Solved!")

test_most_frequent_digit()


# 2)
def count_digit(num, digit):
    count = 0
    while num > 0:
        d = num % 10
        num //= 10
        if d == digit:
            count += 1
    return count


def is_rotation(a, b):
    for i in range(1, 10):
        if count_digit(a, i) != count_digit(b, i):
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
        d = n % 10
        n //= 10
        if d % 2 == 0:
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
    longest_streak = 1
    best_digit = n
    while n > 0:
        digit = n % 10
        n //= 10
        m = n
        while m > 0:
            temp_digit = m % 10
            m //= 10
            if temp_digit == digit:
                streak += 1
                if streak > longest_streak:
                    best_digit = digit
                elif streak == longest_streak and digit < best_digit:
                    best_digit = digit
            else:
                break
    return best_digit


def test_longest_digit_run():
    assert(longest_digit_run(9) == 9)
    assert(longest_digit_run(14441) == 4)
    assert(longest_digit_run(22441) == 2)
    assert(longest_digit_run(10023) == 0)
    print("Problem 4: Solved!")

test_longest_digit_run()


# 5)
def is_palindrome(n):
    original_num = n
    while count_digits(n) != (count_digits(original_num) // 2):
        right_digit = n % 10
        print("right = " + str(right_digit))
        left_digit = n // (10 ** (count_digits(n) - 1))
        print("left = " + str(left_digit))
        if right_digit != left_digit:
            return False
        n //= 10
        print(n)
        # m = (n % (10 ** (count_digits(n) - 1)))
        print(n)
    return True

print(is_palindrome(12321))
