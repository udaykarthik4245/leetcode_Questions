from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        l=list(s)
        a=[]
        i=0
        j=1
        a.append(l[0])
        for i in range(j,len(l)):
            if l[i]!=[j]:

                a.append(l[i])
                j+=1
            # if l[i]==l[j]:
            else:
                a.append(l[i])
                a.append(l[j])
        # a.sort(reverse=True)
        # return a[::-1]
        a_count=Counter(a)
        sor_a=sorted(a_count.items(),key=lambda x:x[1],reverse=True)
        r=[]
        for char,count in sor_a:
            r.extend([char]*count)
            print(f"{char} - {count}")
        return(r)