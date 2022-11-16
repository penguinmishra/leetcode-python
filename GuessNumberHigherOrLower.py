# https://leetcode.com/problems/guess-number-higher-or-lower/

# dummy guess function,
# this function is provided by problem
def guess(num):
    pass



def guessNumber(self, n):
        s = 1
        while s <= n:
            middle = s + (n - s) // 2
            a = guess(middle) # provided by problem
            if a < 0:
                n = middle - 1
            elif a > 0:
                s = middle + 1
            else:
                return middle