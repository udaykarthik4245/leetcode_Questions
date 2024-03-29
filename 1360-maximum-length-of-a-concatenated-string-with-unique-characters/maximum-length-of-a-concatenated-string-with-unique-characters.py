from itertools import combinations
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        max_length = 0
        max_combination = []

        for r in range(1, len(arr) + 1):
            for combo in combinations(arr, r):
                current_combined = ''.join(combo)
                if len(set(current_combined)) == len(current_combined) and len(current_combined) > max_length:
                    max_length = len(current_combined)
                    max_combination = list(combo)

        return max_length
# using set and bitmanipulation
        
        
        # class Solution:
    # def maxLength(self, arr: List[str]) -> int:
    #     l=[set()]
    #     for i in arr:
    #         if len(set(i)) < len(i):
    #             continue
    #         i = set(i)
    #         for j in l:
    #             if i & j:
    #                 continue
    #             l.append(i | j)
    #     m = 0
    #     for i in l:
    #         if m < len(i):
    #             m = len(i)
    #     return m
        
        