class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count=0
        hours.sort()
        for i in range(len(hours)):
            if hours[i]>=target:
                count+=1
            else:
                count+=0
        return count
