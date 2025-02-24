class Solution:
    def calculateSpan(self, arr):
        n = len(arr)
        ans = []
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            span = i - stack[-1] if stack else i + 1
            ans.append(span)
            stack.append(i)  # Store the index, not the value
        return ans
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.calculateSpan(arr)
        print(*ans)
        print("~")
        t -= 1
