# 1)
def look_and_say(arr):
    said = []
    output = []
    for i in range(len(arr)):
        if arr[i] not in said:
            said.append(arr[i])
            output += [(arr.count(arr[i]), arr[i])]
    return output


def test_look_and_say():
    assert look_and_say([]) == []
    assert look_and_say([1, 1, 1]) == [(3, 1)]
    assert look_and_say([-1, 2, 7]) == [(1, -1), (1, 2), (1, 7)]
    assert look_and_say([3, 3, 8, -10, -10, -10]) == [(2, 3), (1, 8), (3, -10)]
    print("Problem 1: Solved!")

test_look_and_say()


# 2)
def inverse_look_and_say(arr):
    output = []
    for t1 in arr:
        for i in range(t1[0]):
            output.append(t1[1])
    return output


def test_inverse_look_and_say():
    assert inverse_look_and_say([]) == []
    assert inverse_look_and_say([(3, 1)]) == [1, 1, 1]
    assert inverse_look_and_say([(1, -1), (1, 2), (1, 7)]) == [-1, 2, 7]
    assert inverse_look_and_say([(2, 3), (1, 8), (3, -10)]) == [3, 3, 8, -10, -10, -10]
    print("Problem 2: Solved!")

test_inverse_look_and_say()