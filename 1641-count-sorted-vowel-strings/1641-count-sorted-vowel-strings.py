class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        def rec(n, vowel):
            if n==0:
                return 1
            total=0
            for i in range(vowel,5):
                total+=rec(n-1,i)
            return total
        return rec(n,0)