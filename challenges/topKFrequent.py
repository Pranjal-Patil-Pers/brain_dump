class Solution:
    def topKFrequent(self, nums, k) :
        dict1={}
        for num in nums:
            if num in dict1:
                dict1[num]+=1
            else:
                dict1[num]=1
        dict1 = sorted(dict1.items(), key=lambda x:x[1], reverse = True)
        list1 = []
        for i in range(k):
            list1.append(dict1[i][0])
        return list1

if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3],k=2))
