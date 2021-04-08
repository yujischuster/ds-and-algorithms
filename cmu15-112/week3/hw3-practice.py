import string


# 1)
def same_chars(s1, s2):
    for i in s1:  # loop through s1
        found = 0
        for j in s2:  # loop through s2
            if i == j:
                found += 1
            if found > 0:  # if one match is found exit loop
                break
        if found < 1:  # if char from s1 does not exist in s2 return false
            return False
    return True


def test_same_chars():
    assert same_chars("abcd", "aabbccdd")
    assert same_chars("abCD12", "211baDCD")
    assert same_chars("$#hhH", "hHH$#")
    assert same_chars("yuuuuji", "yuji")
    print("Problem 1: Solved!")

test_same_chars()


# 2)
def word_wrap(text, width):
    t = ""
    count1 = 0
    for s1 in text:  # create string t with spaces still at the end
        t += s1
        count1 += 1
        if count1 == len(text):
            break
        if count1 % width == 0:
            t += "\n"
    u = ""
    count2 = 0
    for str1 in t.split("\n"):  # string u = erased spaces at beg/ends of each line
        n1 = 0
        while str1[n1].isspace():
            str1 = str1[n1 + 1:]
            n1 += 1
        count2 += 1
        n2 = 1
        while len(str1) < width:
            str1 += " "
        while str1[width - n2].isspace():
            str1 = str1[:width - n2]
            n2 += 1
        u += str1 + "\n"
    v = ""
    for s3 in u:  # string v = spaces in between replaced with dashes
        if s3 == " ":
            v += "-"
        else:
            v += s3
    if v[-1] == "\n":  # remove \n at end of string
        v = v[:len(v) - 1]
    return v


def test_word_wrap():
    assert word_wrap("abcdefghij", 4) == "abcd\nefgh\nij"
    assert word_wrap("a b c de fg", 4) == "a-b\nc-de\nfg"
    assert word_wrap(" Yuji is totally awesome!", 7) == "Yuji-i\ns-total\nly-awes\nome!"
    assert word_wrap("this class is kinda boring", 10) == "this-class\nis-kinda\nboring"
    print("Problem 2: Solved!")

test_word_wrap()


# 3)
def largest_number(text):
    count1 = 0
    for s1 in string.digits:  # check if there are any digits in the string
        if s1 in text:
            max_num = 0
        else:
            count1 += 1
    if count1 == 10:
        return None
    n = 1
    for s2 in range(len(text)):  # find max number
        if text[s2].isdigit():
            temp_num = text[s2]
            if s2 != len(text) - 1:  # if s2 is not last index of string, check for adjacent digit
                while text[s2 + n].isdigit():
                    temp_num += text[s2 + n]
                    n += 1
                temp_num = int(temp_num)
                if temp_num > max_num:
                    max_num = temp_num
    return max_num


def test_largest_number():
    assert largest_number("I saw 3 dogs, 17 cats, and 14 cows!") == 17
    assert largest_number("0 2 2") == 2
    assert largest_number("There is only 0") == 0
    assert largest_number("One person ate two hot dogs!") is None
    print("Problem 3: Solved!")

test_largest_number()


# 4)
def is_palindrome(s):
    return s == s[::-1]


def compare_length(str1, str2):
    if len(str1) > len(str2):
        return str1
    elif len(str1) < len(str2):
        return str2
    else:
        for s1 in str1:
            for s2 in str2:
                if ord(s1) > ord(s2):
                    return str1
                else:
                    return str2


def longest_subpalindrome(s):
    longest = ""
    while len(s) > 1:
        str1 = ""
        for s1 in s:
            str1 += s1
            if is_palindrome(str1):
                any_palindrome = str1
                longest = compare_length(any_palindrome, longest)
        s = s[1:]  # s = s - first index
    return longest


def test_longest_subpalindrome():
    assert longest_subpalindrome("ab-4-be!!!") == "b-4-b"
    assert longest_subpalindrome("abcbce") == "cbc"
    assert longest_subpalindrome("yuji") == "y"
    assert longest_subpalindrome("poop") == "poop"
    print("Problem 4: Solved!")

test_longest_subpalindrome()


# 5)
def longest_common_substring(str1, str2):
    longest = ""
    for i in range(len(str1) - 1):  # loop through str1 and set sub_str1 from index i to end
        sub_str1 = str1[i:]
        for j in range(len(str2) - 1):  # loop through str2 and set sub_str2 from index j to end
            sub_str2 = str2[j:]
            k = 0
            l = 0
            common = ""  # any common substring
            while sub_str1[k] == sub_str2[l]:  # compute substrings
                common += sub_str1[k]
                if len(common) > len(longest):  # set 'longest' to longest substring
                    longest = compare_length(common, longest)
                k += 1
                l += 1
                if k == len(sub_str1) - 1 or l == len(sub_str2) - 1:  # to prevent index out of range error
                    break
    return longest


def test_longest_common_substring():
    assert longest_common_substring("abcdef", "abqrcdest") == "cde"
    assert longest_common_substring("abcdef", "ghi") == ""
    assert longest_common_substring("", "yujis") == ""
    assert longest_common_substring("ktera425", "425terka") == "ter"
    print("Problem 5: Solved!")

test_longest_common_substring()


# 6)
def lowercase_alpha(s):
    str1 = ""
    for s1 in s:
        if s1 in string.ascii_lowercase:
            str1 += s1
        elif s1 in string.ascii_uppercase:
            str1 += s1.lower()
    return str1


def least_frequent_letters(s):
    str1 = lowercase_alpha(s)
    letter = ""
    min_count = len(s)
    for s1 in string.ascii_lowercase:
        count = 0
        for s2 in str1:
            if s1 == s2:
                count += 1
        if count == 0:
            pass
        elif count < min_count:
            letter = s1
            min_count = count
        elif count == min_count:
            letter += s1
    return letter


def test_least_frequent_letters():
    assert least_frequent_letters("aDq efQ? FB'daf!!!") == "be"
    assert least_frequent_letters("aaabbc") == "c"
    assert least_frequent_letters("DdCcBbAa") == "abcd"
    assert least_frequent_letters("122445!!!!") == ""
    print("Problem 6: Solved!")

test_least_frequent_letters()


# 7)
def replace(str1, s2, s3):
    str2 = ""
    for s1 in str1:
        if s1 == s2:
            str2 += s3
        else:
            str2 += s1
    return str2


def test_replace():
    assert replace("yuji", "j", "r") == "yuri"
    assert replace("wooooow", "o", "e") == "weeeeew"
    assert replace("o", "o", "t") == "t"
    assert replace("17177711", "7", "4") == "14144411"
    print("Problem 7: Solved!")

test_replace()


# 8a)
def uppercase_alpha(s):
    str1 = ""
    for s1 in s:
        if s1 in string.ascii_uppercase:
            str1 += s1
        elif s1 in string.ascii_lowercase:
            str1 += s1.upper()
    return str1


def encrypt(str1, password):
    for p1 in password:
        if p1 not in string.ascii_lowercase:
            return "password must be all lowercase"
    encrypted = ""
    n = 0
    str2 = uppercase_alpha(str1)
    password = password.upper()
    for s1 in str2:
        position = ord(password[n]) - 65
        shift = (ord(s1) - 65 + position) % 26
        encrypted += string.ascii_uppercase[shift]
        n += 1
        if n == len(password):
            n = 0
    return encrypted


def test_encrypt():
    assert encrypt("Go Team!", "azby") == "GNUCAL"
    assert encrypt("143wow", "jesus") == "FSO"
    assert encrypt("Hello World!", "ajdsjd") == "HNODXZOAOV"
    assert encrypt("Yuji Schuster", "D3ff") == "password must be all lowercase"
    print("Problem 8a: Solved!")

test_encrypt()


def decrypt(ciphertext, password):
    for p1 in password:
        if p1 not in string.ascii_lowercase:
            return "password must be all lowercase"
    decrypted = ""
    n = 0
    password = password.upper()
    for s1 in ciphertext:
        position = ord(password[n]) - 65
        shift = (ord(s1) - 65 - position) % 26
        decrypted += string.ascii_uppercase[shift]
        n += 1
        if n == len(password):
            n = 0
    return decrypted


def test_decrypt():
    assert decrypt("GNUCAL", "azby") == "GOTEAM"
    assert decrypt("FSO", "jesus") == "WOW"
    assert decrypt("HNODXZOAOV", "ajdsjd") == "HELLOWORLD"
    assert decrypt("Yuji Schuster", "D3ff") == "password must be all lowercase"
    print("Problem 8b: Solved!")


test_decrypt()


# 9)
def encode_offset(s, d):
    encoded = ""
    for s1 in s:
        if s1 in string.ascii_lowercase:
            encoded += string.ascii_lowercase[(ord(s1) + d - 71) % 26]
        elif s1 in string.ascii_uppercase:
            encoded += string.ascii_uppercase[(ord(s1) + d - 91) % 26]
        else:
            encoded += s1
    return encoded


def test_encode_offset():
    assert encode_offset("ACB", 2) == "CED"
    assert encode_offset("XYZ", 1) == "YZA"
    assert encode_offset("Abc", -27) == "Zab"
    assert encode_offset("A2b#c", -27) == "Z2a#b"
    print("Problem 9: Solved!")

test_encode_offset()


# 10)
def decode_offset(s, d):
    decoded = ""
    for s1 in s:
        if s1 in string.ascii_lowercase:
            decoded += string.ascii_lowercase[(ord(s1) - d - 71) % 26]
        elif s1 in string.ascii_uppercase:
            decoded += string.ascii_uppercase[(ord(s1) - d - 91) % 26]
        else:
            decoded += s1
    return decoded


def test_decode_offset():
    assert decode_offset("CED", 2) == "ACB"
    assert decode_offset("YZA", 1) == "XYZ"
    assert decode_offset("Zab", -27) == "Abc"
    assert decode_offset("Z2a#b", -27) == "A2b#c"
    print("Problem 10: Solved!")


test_decode_offset()


# 11a)
def is_valid_hand(s):
    n = 0
    for s1 in s:
        if n % 3 == 0:
            if (s1 == "T" or
                s1 == "J" or
                s1 == "Q" or
                s1 == "K" or
                s1 == "A" or
                s1 == "2" or
                s1 == "3" or
                s1 == "4" or
                s1 == "5" or
                s1 == "6" or
                s1 == "7" or
                s1 == "8" or
                s1 == "9"
            ):
                pass
            else:
                return False
        elif (n == 1 or
                n == 4 or
                n == 7 or
                n == 10 or
                n == 13
        ):
            if (s1 == "D" or
                s1 == "S" or
                s1 == "H" or
                s1 == "C"
            ):
                pass
            else:
                return False
        elif (n == 2 or
            n == 5 or
            n == 8 or
            n == 11
        ):
            if not s1.isspace():
                return False
        n += 1
        if n == 14:
            return True


def test_is_valid_hand():
    assert is_valid_hand("KD KD KD KD KD")
    assert is_valid_hand("JD JS TH 2D 5C")
    assert not is_valid_hand("KD J5 6S 8S 2C")
    assert not is_valid_hand("KC QT 5S 5S 3H")
    print("Problem 11a: Solved!")

test_is_valid_hand()


# 11b)
def is_flush(s):
    if not is_valid_hand(s):
        return False
    else:
        if ((s[1] == "D" and s[4] == "D" and s[7] == "D" and s[10] == "D" and s[13] == "D") or
            (s[1] == "H" and s[4] == "H" and s[7] == "H" and s[10] == "H" and s[13] == "H") or
            (s[1] == "S" and s[4] == "S" and s[7] == "S" and s[10] == "S" and s[13] == "S") or
            (s[1] == "C" and s[4] == "C" and s[7] == "C" and s[10] == "C" and s[13] == "C")
        ):
            return True
        return False


def test_is_flush():
    assert is_flush("KD KD KD KD KD")
    assert is_flush("5H 4H 3H QH JH")
    assert not is_flush("KH KS QH JH KH")
    assert not is_flush("KD KS KC KS KS")
    print("Problem 11b: Solved!")

test_is_flush()


# 11c)
def is_royal_flush(s):
    if not is_valid_hand(s) or not is_flush(s):
        return False
    else:
        if "K" not in s or "Q" not in s or "J" not in s or "A" not in s or "T" not in s:
            return False
        return True


def test_is_royal_flush():
    assert is_royal_flush("KH QH JH TH AH")
    assert is_royal_flush("QC JC TC KC AC")
    assert not is_royal_flush("KC KC KD KD KD")
    assert not is_royal_flush("AD QD KD 2D JD")
    print("Problem 11c: Solved!")

test_is_royal_flush()


# 11d)
def has_pair(s):
    if not is_valid_hand(s):
        return False
    else:
        if (s[0] == s[3] or
            s[0] == s[6] or
            s[0] == s[9] or
            s[0] == s[12] or
            s[3] == s[6] or
            s[3] == s[9] or
            s[3] == s[12] or
            s[6] == s[9] or
            s[6] == s[12] or
            s[9] == s[12]
        ):
            return True


def test_has_pair():
    assert has_pair("KH KC QC 2D 3D")
    assert has_pair("2S 8S 8S 8H TD")
    assert not has_pair("KC QC AD 3S 4C")
    assert not has_pair("KH QH JH TH AH")
    print("Problem 11d: Solved!")

test_has_pair()