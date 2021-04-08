import string


# 1)
def patterned_message(message, pattern):
    no_space_msg = ""
    for s1 in message:
        if not s1.isspace():
            no_space_msg += s1
    patterned_msg = ""
    n1 = 0
    for s1 in pattern:
        if s1 == "*":
            patterned_msg += no_space_msg[n1]
            n1 += 1
            if n1 == len(no_space_msg):
                n1 = 0
        else:
            patterned_msg += s1
    return patterned_msg


def test_patterned_message():
    assert patterned_message("Go Pirates!!!", """
***************
******   ******
***************
""") == """
GoPirates!!!GoP
irates   !!!GoP
irates!!!GoPira
"""
    assert patterned_message("Three Diamonds!", """
  *     *     *
 ***   ***   ***
***** ***** *****
 ***   ***   ***
  *     *     *
""") == """
  T     h     r
 eeD   iam   ond
s!Thr eeDia monds
 !Th   ree   Dia
  m     o     n
"""
    print("Problem 1: Solved!")


test_patterned_message()


# 2)
def rev_string(s):
    return s[::-1]


def encode_right_left_cipher(message, rows):
    encoded_msg = ""
    columns = round(len(message) / rows + 0.4999)
    for i in range(columns):  # make patterned message
        for j in range(i, len(message), columns):
            encoded_msg += message[j]
        encoded_msg += "\n"
    encoded_msg = encoded_msg[:len(encoded_msg) - 1]  # erase excess \n at end of encoded_msg
    encoded_msg2 = ""
    n1 = 1
    for s1 in encoded_msg.splitlines():  # add lowercase alphabets to open spaces
        if len(s1) < rows:
            encoded_msg2 += s1 + string.ascii_lowercase[-n1] + "\n"
            n1 += 1
        else:
            encoded_msg2 += s1 + "\n"
    encoded_msg3 = str(rows)
    n2 = 1
    for s1 in encoded_msg2.splitlines():  # snake encoded_msg2
        if n2 % 2 == 0:
            encoded_msg3 += rev_string(s1)
        else:
            encoded_msg3 += s1
        n2 += 1
    return encoded_msg3


# still doesn't work under these conditions:
#   - if original message contains spaces (if problem wants me to fill in lowercase alphabets)
def test_encode_right_left_cipher():
    assert encode_right_left_cipher("WEATTACKATDAWN", 4) == "4WTAWNTAEACDzyAKT"
    assert encode_right_left_cipher("HELLOWORLD", 2) == "2HWOELRLLOD"
    print("Problem 2: Solved!")

test_encode_right_left_cipher()


# 3)
def decode_right_left_cipher(encoded_msg):
    columns = int(encoded_msg[0])
    encoded_msg = encoded_msg[1:]
    decoded_msg = ""
    n1 = 0
    for i in range(0, len(encoded_msg), columns):
        if i / columns % 2 == 0:
            decoded_msg += encoded_msg[n1:i + columns]
        else:
            decoded_msg += rev_string(encoded_msg[n1:i + columns])
        n1 += columns
    decoded_msg2 = ""
    for i in range(columns):
        for j in range(i, len(decoded_msg), columns):
            if decoded_msg[j] in string.ascii_uppercase:
                decoded_msg2 += decoded_msg[j]
    return decoded_msg2


def test_decode_right_left_cipher():
    assert decode_right_left_cipher("4WTAWNTAEACDzyAKT") == "WEATTACKATDAWN"
    assert decode_right_left_cipher("2HWOELRLLOD") == "HELLOWORLD"
    print("Problem 3: Solved!")

test_decode_right_left_cipher()


# 4)
def best_student_and_avg(gradebook):
    best_avg = 0
    name = ""
    best_name = ""
    for s1 in gradebook.splitlines():
        if not s1.isspace():
            n1 = 0  # how many strings split by commas
            total = 0
            for s2 in s1.split(","):
                if n1 == 0:
                    name = s2
                else:
                    total += int(s2)
                n1 += 1
            if n1 > 1:
                avg = total // (n1 - 1)
                if avg > best_avg:
                    best_avg = avg
                    best_name = name
    return best_name + ":" + str(best_avg)


def test_best_student_and_avg():
    gradebook = """
# ignore  blank lines and lines starting  with  #'s
wilma,91,93
fred,80,85,90,95,100
betty,88
"""
    assert best_student_and_avg(gradebook) == "wilma:92"
    print("Problem 4: Solved!")

test_best_student_and_avg()


# 5)
def top_level_function_names(code):
    return None


def test_top_level_function_names():
    # f is redefined
    code = """\
def f(x): return x+42
def g(x): return x+f(x)
def f(x): return x-42
"""
    assert top_level_function_names(code) == "f.g"
    # g() is in triple-quotes (""")
    code = '''\
def f(): return """
def g(): pass"""
'''
    assert top_level_function_names(code) == "f"
    print("Problem 5: Solved!")

# test_top_level_function_names()