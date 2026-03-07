class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0:
            return False
        else:
            num =x
            new_num=0
            
            while num>0:
                new_num=(new_num*10)+num%10
                num=num//10
            if (new_num)==x:
                return True
            else :
                return False

if __name__=="__main__":
  sol = Solution()
  print(sol.isPalindrome(121))
