class Solution:
    def isPalindrome(self, x: int) -> bool:
        for i in range(len(str(x))):
            if str(x)[i] != str(x)[-1 - i]:
                return False
        return True