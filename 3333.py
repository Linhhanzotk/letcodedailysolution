class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        cnt=0
        total=1
        a=[]
        mod=10**9+7
        for i in range(1, len(word)):
            if word[i]==word[i-1]: cnt+=1
            else:
                if cnt>0:
                    total=(total*(cnt+1))%mod
                    a.append(cnt)
                    cnt=0
                k-=1
        if cnt>0:
            total=(total*(cnt+1))%mod
            a.append(cnt)
            cnt=0
        k-=2
        if k<0: return total
        f=[1]*(k+2)
        f[0]=0
        for i in a:
            for j in range (k, 0, -1):
                low=max(j-i, 0)
                f[j+1]=(f[j+1]-f[low]+mod)%mod
            for j in range(k+1):
                f[j+1]=(f[j+1]+f[j])%mod
        return (total-f[k+1]+mod)%mod
