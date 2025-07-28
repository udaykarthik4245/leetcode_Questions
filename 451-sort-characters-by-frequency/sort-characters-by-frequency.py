from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i not in d:
                d[i]=1 
            else:
                d[i]+=1 
        print(d)
        print()
        ss=""
        res=dict(sorted(d.items(),key=lambda i: i[1],reverse=True))
        for i,j in res.items():
            ss=ss+(i*j)  
        print(ss)
        print(res)
        return ss
            
                    #                               small solution
# class Solution:
#     def frequencySort(self, s: str) -> str:
#         count = Counter(s)
#         buckets = ["" for _ in range(len(s)+1)]

#         for c, f in count.items():
#             buckets[f] += (c*f)
        
#         return "".join(buckets[::-1])


        