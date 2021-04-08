# 4)
def selection_sort(a):
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a


def test_selection_sort():
    assert selection_sort([4, 2, 4, 1, 3]) == [1, 2, 3, 4, 4]
    assert selection_sort([3, 3, 5, 1]) == [1, 3, 3, 5]
    assert selection_sort([1, 3, 5, 2, 5, 1, 1]) == [1, 1, 1, 2, 3, 5, 5]
    assert selection_sort([9, 2, 3]) == [2, 3, 9]
    print("Problem 4: Solved!")

test_selection_sort()


# 5)
def bubble_sort(a):
    end = len(a)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, end):
            if a[i - 1] > a[i]:
                a[i - 1], a[i] = a[i], a[i - 1]
                swapped = True
        end -= 1
    return a


def test_bubble_sort():
    assert bubble_sort([4, 2, 4, 1, 3]) == [1, 2, 3, 4, 4]
    assert bubble_sort([3, 3, 5, 1]) == [1, 3, 3, 5]
    assert bubble_sort([1, 3, 5, 2, 5, 1, 1]) == [1, 1, 1, 2, 3, 5, 5]
    assert bubble_sort([9, 2, 3]) == [2, 3, 9]
    print("Problem 5: Solved!")

test_bubble_sort()
