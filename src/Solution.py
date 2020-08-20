class Solution(object):
    def isPalindrome(self, x):
        temp = str(x)
        return temp == temp[::-1]