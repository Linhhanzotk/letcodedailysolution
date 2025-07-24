# trash code
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        res=10**9
        edge=[[] for _ in range(len(nums))]
        depth=[0]*len(nums)
        pa=[[0]*10 for _ in range(len(nums))]
        for i in edges:
            edge[i[0]].append(i[1])
            edge[i[1]].append(i[0])


        def create(x, y, cur):
            for i in edge[y]:
                if i==x: continue
                depth[i]=cur+1
                pa[i][0]=y
                for j in range(1, 10):
                    pa[i][j]=pa[pa[i][j-1]][j-1]
                create(y, i, cur+1)
                nums[y]^=nums[i]
        create(0, 0, 0)



        def check(u, v):
            if depth[u]<depth[v]: u, v = v, u
            k=depth[u]-depth[v]
            for i in range(9, -1, -1):
                if (1<<i)<=k:
                    u=pa[u][i]
                    k-=(1<<i)
            if u==v: return False
            return True

        for id1 in range(len(nums)-2):
            for id2 in range(id1+1, len(nums)-1):
                i=edges[id1]
                if depth[i[0]]>depth[i[1]]:
                    i[0], i[1] = i[1], i[0]
                j=edges[id2]
                if depth[j[0]]>depth[j[1]]:
                    j[0], j[1] = j[1], j[0]
                if check(i[1], j[1]):
                    res=min(res, max(nums[0]^nums[i[1]]^nums[j[1]], nums[i[1]], nums[j[1]])-min(nums[0]^nums[i[1]]^nums[j[1]], nums[i[1]], nums[j[1]]))
                else:
                    if depth[i[0]]>depth[j[0]]:
                        i, j = j, i
                    res=min(res, max(nums[0]^nums[i[1]], nums[i[1]]^nums[j[1]], nums[j[1]])-min(nums[0]^nums[i[1]], nums[i[1]]^nums[j[1]], nums[j[1]]))

        return res
