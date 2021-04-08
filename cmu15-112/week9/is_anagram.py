def letter_counts(s):
    counts = dict()
    for ch in s.upper():
        if ((ch >= "A") and (ch <= "Z")):
            counts[ch] = counts.get(ch, 0) + 1
    return counts


def is_anagram(s1, s2):
    return (letter_counts(s1) == letter_counts(s2))


def test_is_anagram():
    print("Testing is_anagram()...", end="")
    assert(is_anagram("", "") == True)
    assert(is_anagram("abCdabCd", "abcdabcd") == True)
    assert(is_anagram("abcdaBcD", "AAbbcddc") == True)
    assert(is_anagram("abcdaabcd", "aabbcddcb") == False)
    print("Passed!")


test_is_anagram()
