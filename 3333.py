class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        a=[]
        cnt=1
        total=1
        mod=10**9+7
        for i in range(1, len(word)):
            if word[i]==word[i-1]:
                cnt+=1
            else:
                a.append(cnt)
                total=(total*cnt)%mod
                cnt=1
        total=(total*cnt)%mod
        a.append(cnt)
        if k<=len(a): return total
        print (total)
        f=[0]*(k+1)
        f[1]=1
        for i in range(len(a)):
            cur=[0]*(k+1)
            for j in range(1, k):
                f[j]=(f[j]+f[j-1])%mod
                if j>i:
                    low=max(i, j-a[i])
                    cur[j+1]=(f[j]-f[low]+mod)%mod
            f=cur
        invalid=0
        for i in f: invalid+=i
        return (total-invalid+mod)%mod
