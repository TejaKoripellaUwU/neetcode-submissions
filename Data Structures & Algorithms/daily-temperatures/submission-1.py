class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        q = deque()
        res = [0]*len(temperatures)
        for index,val in enumerate(temperatures):
            while len(q) != 0 and val>q[-1][0]:  
                v,i = q.pop()
                res[i] = index-i
            q.append([val,index])
        return res        
