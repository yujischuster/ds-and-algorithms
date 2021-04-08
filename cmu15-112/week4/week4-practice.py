#6 Write the function alternatingSum(a) that takes a list of numbers and returns the alternating sum (where the sign alternates from positive to negative or vice versa). For example, alternatingSum([5,3,8,4]) returns 6 (that is, 5-3+8-4).

def alternatingSum(a):
    total = 0
    for i in range(len(a)):
        if i % 2 == 0:
            total += a[i]
        else:
            total -= a[i]
    return total

def testAlternatingSum():
    print("Testing alternatingSum()...", end="")
    assert(alternatingSum([5,3,8,4]) == 6)
    assert(alternatingSum([4,5,2,6,1]) == -4)
    assert(alternatingSum([5,1,5,2]) == 7)
    print("Passed")

testAlternatingSum()

#7 Write the non-destructive function median(a) that takes a list of floats and returns the median value, which is the value of the middle element, or the average of the two middle elements. If the list is empty, return None.

def median(a):
    a = a.sort()
    if a == []:
        return None
    elif len(a) % 2 == 0:
        return (a[len(a)/2] + a[len(a)/2 - 1]) / 2
    else:
        return a[len(a) // 2]

def testMedian():
    print("Testing median()...", end="")
    assert(median([1,2]) == 1.5)
    assert(median([1,6,3,2,5]) == 3)
    assert(median([]) == None)
    print("Passed!")

testMedian()

#8 Write the function isPalindromicList(a) that takes a list and returns True if it is the same forwards as backwards and False otherwise.

def isPalindromicList(a):
    return

def testIsPalindromicList():
    return
    print("Testing isPalindromicList()...", end="")
    print("Passed!")

#9 Write the function reverse(a) that destructively reverses the list a. So if a equals [2,3,4], then after reverse(a), a should equal [4,3,2]. As is generally true of destructive functions, this function does not return a value (well, technically it returns None, but Python does that for you).

def reverse(a):
    return

def testReverse():
    return
    print("Testing reverse()...", end="")
    print("Passed!")

#10 Write the function vectorSum(a,b) that takes two same-length lists of numbers a and b, and returns a new list c where c[i] is the sum of a[i] and b[i]. For example, vectorSum([2,4],[20,30]) returns [22, 34].

def vectorSum(a, b):
    return

def testVectorSum():
    return
    print("Testing vectorSum()...", end="")
    print("Passed!")

#11 Write the function isSorted(a) that takes a list of numbers and returns True if the list is sorted (either smallest-first or largest-first) and False otherwise. Your function must only consider each value in the list once (so, in terms of big-oh, which we will learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort the list.

def isSorted(a):
    return

def testIsSorted():
    return
    print("Testing isSorted()...", end="")
    print("Passed!")

#12 Background: the 'dot product' of the lists [1,2,3] and [4,5,6] is (1*4)+(2*5)+(3*6), or 4+10+18, or 32. In general, the dot product of two lists is the sum of the products of the corresponding terms. With this in mind, write the function dotProduct(a,b). This function takes two lists and non-destructively returns the dotProduct of those lists. If the lists are not equal length, ignore the extra elements in the longer list.

def dotProduct(a, b):
    return

def testDotProduct():
    return
    print("Testing dotProduct()...", end="")
    print("Passed!")

#13 Write the function nondestructiveRotateList(a, n) which takes a list a and an integer n, and nondestructively modifies the list so that each element is shifted to the right by n indices (including wraparound). The function should then return this new list. For example: nondestructiveRotateList([1,2,3,4], 1) -> [4,1,2,3], nondestructiveRotateList([4,3,2,6,5], 2) -> [6, 5, 4, 3, 2]

#14 This function works the same as the previous function, only here it is destructive. That is, it directly changes the list a, so after the call, that exact list is rotated n indices to the right with wraparound, and a new list is not created. As usual for destructive functions, this function returns None. Also: you may not call the nondestructive version here, and in fact, you may not even create a new list (or tuple or other similar data structure) that is longer than 2 elements! While you must be space-efficient here, we do not expect the most time-efficient approach; anything reasonable (for 15-112) will do.

#15 Write the function moveToBack(a,b) which takes two lists a and b, and destructively modifies a so that each element of a that appears in b moves to the end of a in the order that they appear in b. The rest of the elements in a should still be present in a, in the same order they were originally. The function should return a. Examples: moveToBack([2, 3, 3, 4, 1, 5], [3]) -> [2, 4, 1, 5, 3, 3]

#16 Write the function binaryListToDecimal(a) which takes a list of 1s and 0s, and returns the integer represented by reading the list from left to right as a single binary number. Examples: binaryListToDecmial([1, 0]) -> 2

#17 Write the function smallestDifference(a) that takes a list of integers and returns the smallest absolute difference between any two integers in the list. If the list is empty, return -1.


#18 Write the function split(s, delimiter), without using the builtin split function (of course), that takes a string and a delimiter and returns a list of substrings that are determined by that delimiter. For example, split("ab,cd,efg", ",") returns ["ab", "cd", "efg"].


#19 Write the function join(L, delimiter), without using the builtin join function (of course), that takes a list and a delimiter and returns the string composed of each element in the list separated by the delimiter. So, join(["ab", "cd", "efg"], ",") returns "ab,cd,efg".

#20 Write the function repeatingPattern(a) that takes a list a and returns True if a == b*k for some list b and some value k>1, and False otherwise. For example, repeatingPattern([1,2,3,1,2,3]) returns True (b==[1,2,3] and k=2).

#21 Write the function mostAnagrams(wordList) that takes a possibly-unsorted list of words (all lowercase) and returns the first word alphabetically in the list that contains the most anagrams of itself in the list. If there are ties, still return just the first word alphabetically.

#22 Write the function map(f, a), which does not use the builtin map function, and which takes a function f and a list a, and returns a new list containing f(x) for each value x in a. For example, say you defined a function plus3(x) that returns (x+3). Then, map(plus3, [2,4,7]) returns [5,7,10].

#23 Write the function firstNEvenFibonacciNumbers(n) that takes a non-negative number n and returns a list of the first n even Fibonacci numbers in increasing order. For example, firstNEvenFibonacciNumbers(4) returns [2, 8, 34, 144]. Note that your answer must run in O(n) time, so it cannot repeatedly call nthEvenFibonacciNumber.


#24 Write the function mostCommonName, that takes a list of names (such as ['Jane', 'Aaron', 'Cindy', 'Aaron'], and returns the most common name in this list (in this case, 'Aaron'). If there is more than one such name, return a list of the most common names, in alphabetical order (actually, in whatever order sorted() uses). So mostCommonName(['Jane', 'Aaron', 'Jane', 'Cindy', 'Aaron']) returns the list ['Aaron', 'Jane']. If the list is empty, return None. Also, treat names case sensitively, so 'jane' and 'Jane' are different names.

#25 Write the function histogram(a) that takes a list of integers between 0 and 100, inclusive, representing exam scores, and returns a string representing a histogram of that data. The details can be gleaned from this example: histogram([73, 62, 91, 74, 100, 77]) returns this multi-line string:

"""
60-69: *
70-79: ***
80-89:
90++ : **
"""

#26  Write the function nearestWords(wordList, word) that takes a sorted wordlist and a single word (all words in this problem will only contain lowercase letters). If the word is in the wordlist, then that word is returned. Otherwise, the function returns a list of all the words (in order) in the wordlist that can be obtained by making a single small edit on the given word, either by adding a letter, deleting a letter, or changing a letter. If no such words exist, the function returns None.


#27 Write the function nearestWords(wordList, word) that takes a sorted wordlist and a single word (all words in this problem will only contain lowercase letters). If the word is in the wordlist, then that word is returned. Otherwise, the function returns a list of all the words (in order) in the wordlist that can be obtained by making a single small edit on the given word, either by adding a letter, deleting a letter, or changing a letter. If no such words exist, the function returns None.

#28

"""
Background: in bowling, a bowler gets 2 throws per frame for 10 frames, where each frame begins with 10 pins freshly positioned, and the score is the sum of all the pins knocked down. However, if the bowler knocks down all 10 pins on the first throw of a frame, it is called a "strike", and they do not get a second throw in that frame; also, the number of pins knocked down in the next two throws are added to the score of that frame. Also, if the bowler knocks down the rest of the 10 pins on the second throw in a frame, that is called a "spare", and the number of pins knocked down in the next throw are added to the score of that frame. Finally, if there is a spare or strike in the final frame, then the bowler gets one extra throw in that frame (but if there is a subsequent strike, they still get only that one extra throw). With all this in mind, write the function bowlingScore that takes a list of the number of pins knocked down on each throw and returns the score. Note that throws skipped due to strikes are not listed, so the best possible result is a list of 12 10's (all strikes), which would score 300 points.
"""

#29 Background: we can represent a polynomial as a list of its coefficients. For example, [2, 3, 0, 4] could represent the polynomial 2x3 + 3x2 + 4. With this in mind, write the function evalPolynomial(coeffs, x) that takes a list of coefficients and a value x and returns the value of that polynomial evaluated at that x value. For example, evalPolynomial([2,3,0,4], 4) returns 180 (2*43 + 3*42 + 4 = 2*64 + 3*16 + 4 = 128 + 48 + 4 = 180).

#30 Write the function multiplyPolynomials(p1, p2) which takes two polynomials as defined in the previous problem and returns a third polynomial which is the product of the two. For example, multiplyPolynomials([2,0,3], [4,5]) represents the problem (2x**2 + 3)(4x + 5), and: (2x**22 + 3)(4x + 5) = 8x**3 + 10x**2 + 12x + 15. And so this returns [8, 10, 12, 15].

#31 Write the function polynomialToString(p) that takes a polynomial as defined in the previous problems and returns a string representation of that polynomial, with these rules:
"""
Use "n" as the variable
Use "^" for exponentation (though that means "bitwise-xor" in Python)
Include a space before/after each "+" or "-" sign
Do not include 0 coefficients (unless the entire polynomial equals 0)
So polynomialToString([2,-3,0,4]) returns "2n^3 - 3n^2 + 4"
"""

#32 Write the function areaOfPolygon(L) that takes a list of (x,y) points that are guaranteed to be in either clockwise or counter-clockwise order around a polygon, and returns the area of that polygon, as described here. For example (taken from that text), areaOfPolygon([(4,10), (9,7), (11,2), (2,2)]) returns 45.5 (at least the result is almostEqual to 45.5). Here is a sample test function for you:

def testAreaOfPolygon():
    return
    print("Testing areaOfPolygon()...", end="")
    assert(almostEqual(areaOfPolygon([(4,10), (9,7), (11,2), (2,2)]), 45.5))
    assert(almostEqual(areaOfPolygon([(9,7), (11,2), (2,2), (4, 10)]), 45.5))
    assert(almostEqual(areaOfPolygon([(0, 0), (0.5,1), (1,0)]), 0.5))
    assert(almostEqual(areaOfPolygon([(0, 10), (0.5,11), (1,10)]), 0.5))
    assert(almostEqual(areaOfPolygon([(-0.5, 10), (0,-11), (0.5,10)]), 10.5))
    print("Passed!")
