from collections import deque
class Solution:
    def maxLength(self, s):
        stack = deque()
        count = 0
        s = list(s.split())
        for i in  s:
            x , y = i
            if x == "(" and y==")":
                stack.appendleft(x)
                stack.appendleft(y)
                count += 1
        return count
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        print(ob.maxLength(S))
        print("~")
