class Solution:
    
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s:str):
            if s == s[::-1]:
                return True
            else:
                return False

        if isPalindrome(s):
            return True

        left, right = 0, len(s) - 1

        while s[left] == s[right]:
            left += 1
            right -= 1
                

        return isPalindrome(s[:left] + s[left+1:]) or isPalindrome(s[:right] + s[right+1:])



