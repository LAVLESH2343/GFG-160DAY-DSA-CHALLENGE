class Solution:
    def nextLargerElement(self, arr):
        stack = []  
        result = [-1] * len(arr)  
        for i in range(len(arr) - 1, -1, -1):  
            while stack and stack[-1] <= arr[i]:
                stack.pop()  
            if stack:
                result[i] = stack[-1]  
            stack.append(arr[i])  
        return result
t = int(input())  
for _ in range(t):
    arr = list(map(int, input().split()))  
    s = Solution().nextLargerElement(arr) 
    if s:
        print(" ".join(map(str, s))) 
    else:
        print("[]") 
    print("~")
