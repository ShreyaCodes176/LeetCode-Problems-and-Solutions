class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)
        b=n//8
        r=n%8
        return (b*(b+1)*4)+(n%8)*(b+1)