class Solution:
    def gcd(a,b):
            if b==0:
                return a
            else:
                gcd(b,a%b)
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd=n*n
        sumEven=n*(n+1)
        return gcd(sumOdd,sumEven)
