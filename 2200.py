class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        a=[]
        last=0
        for i in range(len(nums)):
            if nums[i]==key:
                first=max(last, i-k)
                last=min(i+k+1, len(nums))
                while first<last:
                    a.append(first)
                    first+=1
        return a
