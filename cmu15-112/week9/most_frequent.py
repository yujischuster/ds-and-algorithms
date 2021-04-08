def most_frequent(L):
    # Return most frequent element in L, resolving ties arbitrarily.
    max_value = None
    max_count = 0
    counts = dict()
    for element in L:
        count = 1 + counts.get(element, 0)
        counts[element] = count
        if (count > max_count):
            max_count = count
            max_value = element
    return max_value


def test_most_frequent():
    print("Testing most_frequent()... ", end="")
    assert(most_frequent([2, 5, 3, 4, 6, 4, 2, 4, 5]) == 4)
    assert(most_frequent([2, 3, 4, 3, 5, 3, 6, 3, 7]) == 3)
    assert(most_frequent([42]) == 42)
    assert(most_frequent([]) == None)
    print("Passed!")


test_most_frequent()
