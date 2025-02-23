import heapq
class Solution:
    def getMedian(self, arr):
        min_heap = [] 
        max_heap = []  
        medians = []
        for num in arr:
            heapq.heappush(max_heap, -num)
            if max_heap and min_heap and (-max_heap[0] > min_heap[0]):
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            if len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
            if len(max_heap) == len(min_heap):
                medians.append((-max_heap[0] + min_heap[0]) / 2)
            else:
                medians.append(-max_heap[0])
        return medians
def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.getMedian(nums)
        print(" ".join(f"{x:.1f}" for x in ans))
if __name__ == "__main__":
    main()
