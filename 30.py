class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        need=len(words)
        data=[-1]*len(s)
        base=[0]*need
        dic={}
        k=len(words[0])
        res=[]
        for i in range(need):
            if words[i] in dic: base[dic[words[i]]]+=1
            else:
                dic[words[i]]=i
                base[i]+=1
        for i in range(len(s)-k+1):
            cur=s[i:i+k]
            if cur in dic:
                data[i]=dic[cur]
        for i in range(k):
            l=r=i
            check=[0]*need
            cnt=0
            while r<len(s):
                if data[r]==-1:
                    while l<r:
                        check[data[l]]-=1
                        l+=k
                    l=r=r+k
                    cnt=0
                else:
                    while check[data[r]]==base[data[r]]:
                        check[data[l]]-=1
                        l+=k
                        cnt-=1
                    check[data[r]]+=1
                    cnt+=1
                    if cnt==need: res.append(l)
                    r+=k
        return res
