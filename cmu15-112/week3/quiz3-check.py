# 1)
def w(n):
    x = 0
    while (x**2 < n):
        print("x is", x)
        x += 2


def my_w(n):
    for x in range(0, n ** 2, 2):
        print("x is", x)

# w(n)
# my_w(n)


# 2)
def ct1(n):
    x = n
    k = 0
    while (x > 0):
        total = 0
        y = n
        for i in range(k):
            total += y%10
            y //= 10
        print(k, total)
        x //= 10
        k += 1

# print(ct1(1234))


# 3)
def f(x, y):
    assert((type(x) == int) and (type(y) == int))
    if ((x <= 50) or (y > 25)): z = 3
    elif (x%10 + y%10 > 0): z = 42
    elif (x == y + 40): z = 10
    else: z = 5
    return (z == 2**5//3)

# print(f(60, 20))


# 4)
def is_stepping_number(n):
    n1 = 0
    if n == 0:
        return True
    elif n == 11:
        return False
    while n > 9:
        digit = n % 10
        if digit <= n1:
            return False
        n1 = digit
        n //= 10
    return True

print(is_stepping_number(0))


def nth_stepping_number(n):
    n1 = 0
    n2 = -1
    while n2 != n:
        n1 += 1
        if is_stepping_number(n1):
            n2 += 1
    return n1

print(nth_stepping_number(0))

def test_nth_stepping_number():
    assert nth_stepping_number(0) == 0
    assert nth_stepping_number(10) == 12
    assert nth_stepping_number(433) == 145679
    print("Problem 4: Solved!")

test_nth_stepping_number()
