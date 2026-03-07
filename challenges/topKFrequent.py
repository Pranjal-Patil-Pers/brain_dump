class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for num in nums:
            dict1[num] = dict1.get(num,0)+1
        freq = [[] for _ in range(len(nums)+1)]
        for val, c in dict1.items():
            freq[c].append(val)

        list1 = []
        for i in range(len(freq)-1,0, -1):
            for j in freq[i]:
                list1.append(j)
                if len(list1)==k:
                    return list1

if __name__=="__main__":
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,2,3,3],k=2)
