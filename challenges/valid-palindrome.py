class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()
        if s=="":
            return True
        cleans = list(filter(lambda x:x.isalnum(),s))
        revs = []
        mid = len(cleans)//2
        for i in range(len(cleans)-1,mid-1,-1):
            revs.append(cleans[i])
        if cleans[:mid] == revs or cleans[:mid]==revs[:-1]:
            return True
        else:
            return False

if __name__=="__main__":
  sol = Solution()
  print(sol.isPalindrome("Pranjal23@jfg"))
