def is_permutation(L):
    # return True if L is a permutation of [0,...,n-1]
    # and False otherwise
    return (set(L) == set(range(len(L))))


def test_is_permutation():
    print("Testing is_permutation()...", end="")
    assert(is_permutation([0, 2, 1, 4, 3]) == True)
    assert(is_permutation([1, 3, 0, 4, 2]) == True)
    assert(is_permutation([1, 3, 5, 4, 2]) == False)
    assert(is_permutation([1, 4, 0, 4, 2]) == False)
    print("Passed!")


test_is_permutation()
