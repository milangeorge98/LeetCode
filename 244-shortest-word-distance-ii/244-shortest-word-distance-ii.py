from collections import defaultdict
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.locations=defaultdict(list)
        
        for i,w in enumerate(wordsDict):
            self.locations[w].append(i)
        

    def shortest(self, word1: str, word2: str) -> int:
        loc1=self.locations[word1]
        loc2=self.locations[word2]
        l1,l2=0,0
        minDiff=float("inf")
        
        while l1<len(loc1) and l2<len(loc2):
            minDiff=min(minDiff,abs(loc1[l1]-loc2[l2]))
            if(loc1[l1]<loc2[l2]):
                l1+=1
            else:
                l2+=1
        return minDiff
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)