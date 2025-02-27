class Solution:
    def getMaxArea(self, arr):
        n = len(arr)
        stack = []  
        max_area = 0  
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                height = arr[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                max_area = max(max_area, height * width)
            stack.append(i)
        while stack:
            height = arr[stack.pop()]
            width = n - stack[-1] - 1 if stack else n
            max_area = max(max_area, height * width)
        return max_area
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.getMaxArea(arr)
        print(res)
        print("~")
        t -= 1
