def repeats(L):
    # return a sorted list of the repeat elements in the list L
    seen = set()
    repeats = set()
    for elem in L:
        if elem in seen:
            repeats.add(elem)
        seen.add(elem)
    return sorted(repeats)


def test_repeats():
    print("Testing repeats()...", end="")
    assert(repeats([1, 2, 3, 2, 1]) == [1, 2])
    assert(repeats([1, 2, 3, 2, 2, 4]) == [2])
    assert(repeats(list(range(100))) == [])
    assert(repeats(list(range(100))*5) == list(range(100)))
    print("Passed!")


test_repeats()
