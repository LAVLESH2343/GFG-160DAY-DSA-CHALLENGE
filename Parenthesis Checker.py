class Solution:
    def isBalanced(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}  

        for char in s:
            if char in "({[":  
                stack.append(char)  
            else:
                if not stack or stack[-1] != mapping[char]:  
                    return False 
                stack.pop()  
        return len(stack) == 0  
import atexit
import io
import sys
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s = str(input())
        obj = Solution()
        if obj.isBalanced(s):
            print("true")
        else:
            print("false")
        print("~")
