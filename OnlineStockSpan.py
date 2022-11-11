# https://leetcode.com/problems/online-stock-span/
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        v = 1
        while self.stack and self.stack[-1][0] <= price:
            last = self.stack.pop()
            v += last[1]
        self.stack.append([price, v])
        return v


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)