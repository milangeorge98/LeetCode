class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total=0
        cur=0
        if(sum(gas) <sum(cost)):
            return -1
        
        for i in range(len(gas)):
            total += (gas[i]-cost[i])
            if total <0:
                total=0
                cur = i+1
        return cur