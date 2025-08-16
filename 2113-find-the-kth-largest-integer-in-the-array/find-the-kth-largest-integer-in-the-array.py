class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        min_heap=[]
        for  i in nums:
            if len(min_heap)<k:
                heapq.heappush(min_heap,int(i))
            else:
               if int(i)>min_heap[0]:
                    heapq.heapreplace(min_heap,int(i))
        return str(min_heap[0]) 
        