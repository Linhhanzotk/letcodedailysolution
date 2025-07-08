class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.append([0, 0, 0])
        n=len(events)
        f=[[0]*(k+1) for _ in range(n)]
        events.sort(key=lambda x: x[1])
        for i in range(1, n):
            l, r=1, i-1
            pre=0
            while l<=r:
                mid=(l+r)//2
                if events[mid][1]<events[i][0]:
                    l=mid+1
                    pre=mid
                else:
                    r=mid-1
            for j in range(1, min(i, k)+1):
                f[i][j]=max(f[pre][j-1]+events[i][2], f[i-1][j], f[i][j-1])
        return f[n-1][k]
