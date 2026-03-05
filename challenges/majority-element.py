class Solution():
    def majorityElement(self,nums):
        dict1 = {}
        maxOcc=0
        me = float("-inf")
        for num in nums:
            print(dict1)
            if num in dict1:
                dict1[num] = dict1[num]+1
            else:
                dict1[num]=1
            if maxOcc < dict1[num]:
                maxOcc = dict1[num]
                me = num
        return me
            
if __name__== '__main__':
    sol = Solution()
    print("output:",sol.majorityElement([2,3,4,2]))
