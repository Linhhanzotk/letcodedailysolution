class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        val=0
        cnt=0
        for i in s[::-1]:
            if i=='0': 
                cnt+=1
            elif cnt<k.bit_length() and val+(1<<cnt)<=k:
                val+=1<<cnt
                cnt+=1
        return cnt
