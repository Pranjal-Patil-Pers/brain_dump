class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        cursum = 0
        dict1 = {0:1}
        for num in nums:
            cursum +=num
            diff = cursum-k
            if diff in dict1:
                count+=dict1[diff]
            dict1[cursum] = dict1.get(cursum, 0) + 1
        return count
