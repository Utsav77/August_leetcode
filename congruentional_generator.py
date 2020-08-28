# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def __init__(self):
        self.pre=0
    def rand10(self):
        """
        :rtype: int
        """
        cur=(self.pre*7+rand7())%10+1
        self.pre=cur
        return cur
        