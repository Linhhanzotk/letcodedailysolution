class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        f=[[] for _ in range(target+1)]
        pre=0
        cnt=0
        for i in candidates:
            if i>target: break
            if i==pre:
                cnt+=1
            else:
                cnt=1
                pre=i
            if i*cnt>target: continue
            for j in range(target, i*cnt, -1):
                for k in f[j-i*cnt]:
                    if k[-1]!=i:
                        f[j].append(k+[i]*cnt)
            f[i*cnt].append([i]*cnt)

        return f[target]
