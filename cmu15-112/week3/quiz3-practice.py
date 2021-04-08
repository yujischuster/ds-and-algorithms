import string


# 2)
def vowel_count(s):
    n1 = 0
    for s1 in s:
        if (s1 == "A" or
            s1 == "E" or
            s1 == "I" or
            s1 == "O" or
            s1 == "U" or
            s1 == "a" or
            s1 == "e" or
            s1 == "i" or
            s1 == "o" or
            s1 == "u"
        ):
            n1 += 1
    return n1


def test_vowel_count():
    print("Testing vowelCount()...", end="")
    assert vowel_count("abcdefg") == 2
    assert vowel_count("ABCDEFG") == 2
    assert vowel_count("") == 0
    assert vowel_count("This is a test.  12345.") == 4
    assert vowel_count(string.ascii_lowercase) == 5
    assert vowel_count(string.ascii_lowercase*100) == 500
    assert vowel_count(string.ascii_uppercase) == 5
    assert vowel_count(string.punctuation) == 0
    assert vowel_count(string.whitespace) == 0
    print("Passed!")

test_vowel_count()


# 3)
def interleave(str1, str2):
    interleaved = ""
    shorter = min(len(str1), len(str2))
    if shorter == len(str1):
        longer = str2
    else:
        longer = str1
    for i in range(shorter):
        interleaved += str1[i] + str2[i]
    return interleaved + longer[shorter:]


def test_interleave():
    print("Testing interleave()...", end="")
    assert interleave("abcdefg", "abcdefg") == "aabbccddeeffgg"
    assert interleave("abcde", "abcdefgh") == "aabbccddeefgh"
    assert interleave("abcdefgh", "abcde") == "aabbccddeefgh"
    assert interleave("Smlksgeneg n a!", "a ie re gsadhm") == "Sam likes green eggs and ham!"
    assert interleave("", "") == ""
    print("Passed!")

test_interleave()


# 4)
def most_frequent_letters(s):
    max_count = 0
    max_letter = ""
    if s == "":
        return max_letter
    for i in range(26):
        count = 0
        for s1 in s:
            if s1 == string.ascii_lowercase[i] or s1 == string.ascii_uppercase[i]:
                count += 1
        if count > max_count:
            max_count = count
            max_letter = string.ascii_uppercase[i]
        elif count == max_count:
            max_letter += string.ascii_uppercase[i]
    return max_letter


def test_most_frequent_letters():
    print("Testing mostFrequentLetters()...", end="")
    assert most_frequent_letters("Cat") == 'ACT'
    assert most_frequent_letters("A cat") == 'A'
    assert most_frequent_letters("A cat in the hat") == 'AT'
    assert most_frequent_letters("This is a test") == 'ST'
    assert most_frequent_letters("This is an I test?") == 'IST'
    assert most_frequent_letters("") == ""
    print("Passed!")

test_most_frequent_letters()


# 5)
def split_parentheses(s):
    split = ""
    for s1 in s.split("()"):
        split += s1
    return split


def has_balanced_parentheses(s):
    if len(s) % 2 == 1:
        return False
    while "()" in s:
        s = split_parentheses(s)
    if s != "":
        return False
    return True


def test_has_balanced_parentheses():
    print("Testing hasBalancedParentheses()...", end="")
    assert has_balanced_parentheses("()") == True
    assert has_balanced_parentheses("") == True
    assert has_balanced_parentheses("())") == False
    assert has_balanced_parentheses("()(") == False
    assert has_balanced_parentheses(")(") == False
    assert has_balanced_parentheses("(()())") == True
    assert has_balanced_parentheses("((()())(()(()())))") == True
    assert has_balanced_parentheses("((()())(()((()())))") == False
    assert has_balanced_parentheses("((()())(((()())))") == False
    print("Passed!")

test_has_balanced_parentheses()


# 6)
def are_anagrams(str1, str2):
    for s1 in str1:
        if (str1.count(s1.lower()) + str1.count(s1.upper()) !=
            str2.count(s1.lower()) + str2.count(s1.upper())
        ):
            return False
    return True


def test_are_anagrams():
    print("Testing areAnagrams()...", end="")
    assert are_anagrams("", "") == True
    assert are_anagrams("abCdabCd", "abcdabcd") == True
    assert are_anagrams("abcdaBcD", "AAbbcddc") == True
    assert are_anagrams("abcdaabcd", "aabbcddcb") == False
    print("Passed!")

test_are_anagrams()


# 7)
def rotate_string_left(s, k):
    rotated = ""
    n1 = 0
    j = k % len(s)
    for i in range(j, len(s) + j):
        if i < len(s):
            rotated += s[i]
        else:
            rotated += s[n1]
            n1 += 1
    return rotated


def test_rotate_string_left():
    print("Testing rotateStringLeft()...", end="")
    assert rotate_string_left("abcde", 0) == "abcde"
    assert rotate_string_left("abcde", 1) == "bcdea"
    assert rotate_string_left("abcde", 2) == "cdeab"
    assert rotate_string_left("abcde", 3) == "deabc"
    assert rotate_string_left("abcde", 4) == "eabcd"
    assert rotate_string_left("abcde", 5) == "abcde"
    assert rotate_string_left("abcde", 25) == "abcde"
    assert rotate_string_left("abcde", 28) == "deabc"
    print("Passed!")

test_rotate_string_left()


# 8)
def rotate_string_right(s, k):
    rotated = ""
    n1 = 0
    j = k % len(s)
    for i in range(-j, len(s) - j):
        if i < len(s):
            rotated += s[i]
        else:
            rotated += s[n1]
            n1 += 1
    return rotated


def test_rotate_string_right():
    print("Testing rotateStringRight()...", end="")
    assert rotate_string_right("abcde", 0) == "abcde"
    assert rotate_string_right("abcde", 1) == "eabcd"
    assert rotate_string_right("abcde", 2) == "deabc"
    assert rotate_string_right("abcde", 3) == "cdeab"
    assert rotate_string_right("abcde", 4) == "bcdea"
    assert rotate_string_right("abcde", 5) == "abcde"
    assert rotate_string_right("abcde", 25) == "abcde"
    assert rotate_string_right("abcde", 28) == "cdeab"
    print("Passed!")

test_rotate_string_right()


# 9)
def collapse_whitespace(s):
    collapsed = ""
    if s[0].isspace():
        collapsed += " "
    for i in range(len(s)):
        if not s[i].isspace():
            collapsed += s[i]
        elif s[i].isspace() and not s[i - 1].isspace():
            collapsed += " "
    return collapsed


def test_collapse_whitespace():
    print("Testing collapseWhitespace()...", end="")
    assert collapse_whitespace("   a\n\n\nb ") == " a b "
    assert collapse_whitespace("a\n   \t    b  ") == "a b "
    assert collapse_whitespace("a\n   \t    b  \n\n  \t\t\t c   ") == "a b c "
    print("Passed!")

test_collapse_whitespace()