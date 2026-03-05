class Solution():
    def majorityElement(self, nums):
        nums.sort()
        mid = nums[int(len(nums)/2)]
        return mid
            
if __name__== '__main__':
    sol = Solution()
    print("output:",sol.majorityElement([2,3,4,2]))
