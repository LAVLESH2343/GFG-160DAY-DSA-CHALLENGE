class Solution:
    def mergeKLists(self, arr):
        if not arr or len(arr) == 0:
            return None
        min_heap = []
        for node in arr:
            if node:
                heapq.heappush(min_heap, node)
        dummy = Node(0)  
        curr = dummy
        while min_heap:
            smallest = heapq.heappop(min_heap)
            curr.next = smallest  
            curr = curr.next  
            if smallest.next:
                heapq.heappush(min_heap, smallest.next)
        return dummy.next 
import heapq
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
    def __lt__(self, other):
        return self.data < other.data
def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lists = []
        for _ in range(n):
            values = list(map(int, input().split()))
            head = None
            temp = None
            for value in values:
                newNode = Node(value)
                if head is None:
                    head = newNode
                    temp = head
                else:
                    temp.next = newNode
                    temp = temp.next
            lists.append(head)

        sol = Solution()
        head = sol.mergeKLists(lists)
        printList(head)
        print("~")
if __name__ == "__main__":
    main()
