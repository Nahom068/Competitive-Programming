class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        lst=[]
        ans=[]
        for i in points:
            dist=((i[0]**2)+(i[1]**2))**(1/2)
            lst.append([dist,i])
        lst.sort()
        for i in range(0,k):
            ans.append(lst[i][1])
        return ans
