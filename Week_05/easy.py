#191位1的个数
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while(n>0):
            count +=1
            n = n & (n-1)
    
        return count

#231 2的幂
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n != 0 and  (n & (n-1)) == 0

#190 颠倒二进制
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        power = 31
        while n:
            res += (n &1) << power
            n = n >>1
            power -= 1
        return res

#70 爬楼梯
class Solution:
    def climbStairs(self, n: int) -> int:
        f1 = 1
        f2 = 2
        if (n== 1): 
            return 1
        if (n==2):
             return 2
        for x in range(3,n+1):
            f3 = f1 + f2
            f1, f2 = f2, f3 
        return f3


