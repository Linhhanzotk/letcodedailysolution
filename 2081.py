class Solution:
    def kMirror(self, k: int, n: int) -> int:
        count=0
        i=2
        total=0
        f=[[""], [str(x) for x in range(k)]]
        def check(s: str):
            if s[0]=='0': return False
            nonlocal total, count
            y=int(s, k)
            if y%10==0: return False
            z=0
            t=y
            while y>z:
                z=z*10+y%10
                y//=10
            if z==y or z//10==y:
                count+=1
                total+=t
            return count==n


        for j in f[1][1:]:
            if check(j):
                return total
                
        def generate(m):
            f.append([])
            for j in range(k):
                for l in f[m-2]:
                    f[m].append(str(j)+l+str(j))
                    if check(f[m][-1]): return
        while count<n:
            generate(i)
            i+=1
        return total
