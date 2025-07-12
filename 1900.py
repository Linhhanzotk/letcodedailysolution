class Solution:
    def earliestAndLatest(self, n: int, fst: int, snd: int) -> List[int]:
        k={fst-1, snd-1}
        data={}
        def cop(a):
            mi=n
            ma=0
            cur=[i for i in range(n) if (a>>i) & 1]
            nex=[a]
            l, r=0, len(cur)-1
            while l<r:
                if cur[l] in k and cur[r] in k:
                    data[a]=(1, 1)
                    return
                for i in range(len(nex)-1, -1, -1):
                    if cur[r] in k:
                        nex[i]=nex[i] & ~(1<<cur[l])
                    elif cur[l] in k:
                        nex[i]=nex[i] & ~(1<<cur[r])
                    else:
                        nex.append(nex[i] & ~(1<<cur[l]))
                        nex[i]=nex[i] & ~(1<<cur[r])

                l+=1
                r-=1
            for i in nex:
                if i not in data: cop(i)
                if 1+data[i][0]<mi:
                    mi=1+data[i][0]
                if 1+data[i][1]>ma:
                    ma=1+data[i][1]
            data[a]=(mi, ma)
        initial=(1<<n)-1
        cop(initial)
        return list(data[initial])
