import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
    #using max heap because we are doing - symbol 
        # heap=[-n for n in nums]
        # heapq.heapify(heap)

        # for _ in range(k-1):
        #     heapq.heappop(heap)
        # return -heapq.heappop(heap)

    #using min heap 
        heap=[]
        for i in nums:
            if len(heap)<k:
                heapq.heappush(heap,i)
            elif i>heap[0]:
                heapq.heapreplace(heap,i)
        return heap[0]