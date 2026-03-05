class Solution():
    def majorityElement(self, nums):
        lead = 0
        count =0 
        for num in nums:
            if count ==0:
                lead = num
            if num != lead:
                count-=1
            elif num == lead:
                count+=1
        return lead

if __name__== '__main__':
    sol = Solution()
    print("output:",sol.majorityElement([2,3,4,2]))
